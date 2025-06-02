import logging
from time import perf_counter
from tinkerswood.cache import CachedOutput
from tinkerswood.logger import setupLogging

# see tinkerswood/wood.py for a list of all wood variants
from tinkerswood.woods import WOODS

from tinkerswood.render_infos import RenderInfoGenerator

ROOT_PATH = "../../generated"
"""Target folder for datagen"""

LOG_PATH = "../../../run/logs"
"""Path to create log files for datagen, set to None to skip"""

MOD_ID = "tinkerswood"
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
    
    with RenderInfoGenerator(cache) as gen:
        for wood in WOODS:
            gen.wood(wood["variant"], wood["palette"])
    
    # colors is pretty simple, just do it directly
    colors = {
        "material.tconstruct.wood": {
          data["variant"]: "#" + data["palette"][234] for data in WOODS
        }
    }
    cache.saveJson(colors, f"assets/{MOD_ID}/mantle/colors", sortKeys=False)
    
    # end of datagen, save the cache file
    cache.finalize()
    logging.info(f"Finished running datagen in {perf_counter() - startTime} seconds")