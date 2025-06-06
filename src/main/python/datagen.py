import logging
from time import perf_counter
from typing import Dict, List

from tinkerswood.cache import CachedOutput
from tinkerswood.logger import setupLogging

# see tinkerswood/wood.py for a list of all wood variants
from woods import WOODS

from tinkerswood.render_infos import RenderInfoGenerator
from tinkerswood.tags import TagGenerator
from tinkerswood.recipes import RecipeGenerator

ROOT_PATH = "../../generated"
"""Target folder for datagen"""

LOG_PATH = "../../../run/logs"
"""Path to create log files for datagen, set to None to skip"""

MOD_ID = "tinkers_wood"
"""Mod ID for all resources generated"""

if __name__ == "__main__":
    # setup datagen, run everything below these lines
    startTime = perf_counter()
    setupLogging(LOG_PATH, debug=False)
    cache = CachedOutput(ROOT_PATH)
    # end setup, start of mod specific code
    
    # fill in commonly used data in the woods list
    for wood in WOODS:
        mod = wood["mod_id"]
        name = wood["name"]
        # material variant suffix for Tinkers' Construct
        variant = name if mod == "minecraft" else f"{mod}_{variant}"
        wood["variant"] = variant
        wood["material"] = f"tconstruct:wood#{variant}"
        
        # generate IDs if not set
        if "planks_id" not in wood:
            wood["planks_id"] = f"{mod}:{name}_planks"
        if "log_tag" not in wood:
            wood["log_tag"] = f"{mod}:{name}_logs"
    
    # material render infos
    with RenderInfoGenerator(cache) as gen:
        for wood in WOODS:
            gen.wood(wood["variant"], wood["palette"])
    
    # colors is pretty simple, just do it directly
    colors = {
        "material.tconstruct.wood": {
          data["variant"]: "#" + data["palette"][234] for data in WOODS
        }
    }
    cache.saveJson(colors, f"assets/{MOD_ID}/mantle/colors")
    
    # tags ensure wood does not count default variant
    with TagGenerator(cache) as gen:
        gen.add("items", "tconstruct", "wood_variants/planks", *[wood["planks_id"] for wood in WOODS])
        logs = ["#" + wood["log_tag"] for wood in WOODS if not wood["override_log"]]
        if len(logs) > 0:
            gen.add("items", "tconstruct", "wood_variants/logs", *logs)
    
    # add all 3 relevant recipes
    with RecipeGenerator(cache) as gen:
        # determine how many times each mod shows up
        modCount: Dict[str, int] = {}
        for wood in WOODS:
            mod = wood["mod_id"]
            modCount[mod] = modCount.get(mod, 0) + 1
        
        # add all woods
        for wood in WOODS:
            localPath: str
            mod = wood["mod_id"]
            variant = wood["variant"]
            localPath = variant if modCount[mod] == 1 else f"{mod}/{wood['name']}"
            
            # planks to material variant
            gen.material(wood["material"], {"item": wood["planks_id"]}, MOD_ID, "planks", localPath)
            
            # logs to material variant, might need to override a tconstruct recipe
            logPath: List[str]
            if wood["override_log"]:
                logPath = ["tconstruct", "tools/materials/wood/logs", variant]
            else:
                logPath = [MOD_ID, "logs", localPath]
            gen.material(wood["material"], {"tag": wood["log_tag"]}, *logPath, value=4, leftover=wood["planks_id"])
            # planks to embellishment
            gen.woodEmbellishment(wood["material"], wood["planks_id"], MOD_ID, "embellishment", localPath)
            
    
    # end of datagen, save the cache file
    cache.finalize()
    logging.info(f"Finished running datagen in {perf_counter() - startTime} seconds")