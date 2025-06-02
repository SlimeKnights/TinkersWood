import logging
from time import perf_counter
from .cache import CachedOutput
from typing import Dict

ASSETS = "assets"
FOLDER = "tinkering/materials"

class RenderInfoGenerator:
    """
    Handles the material render info definitions
    """
    
    cache: CachedOutput
    """Cache instance for saving files"""
       
    def __init__(self, cache: CachedOutput):
        self.cache = cache
        self.materials = 0
        self.time = 0
    
    def __enter__(self) -> "BlockGenerator":
        logging.info("Starting material render info generation")
        self.time = perf_counter()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        self.time = perf_counter() - self.time
        logging.info(f"Generated {self.materials} material render infos in {self.time} seconds")
        return False
    
    
    # Methods for datagen root to call
    
    def wood(self, variant: str, paletteMap: Dict[int,str]) -> None:
        palette = [{ "color": f"FF{color}", "grey": grey } for grey, color in paletteMap.items()]
        palette.append({ "color": "FF000000", "grey": 0 })
        palette = sorted(palette, key=lambda c: c["grey"])
        data = {
          "color": "FF" + paletteMap[216],
          "fallbacks": [
            "wood",
            "stick",
            "primitive"
          ],
          "generator": {
            "supported_stats": [
              "tconstruct:head",
              "tconstruct:handle",
              "tconstruct:binding",
              "tconstruct:repair_kit",
              "tconstruct:limb",
              "tconstruct:grip",
              "tconstruct:shield_core",
              "tconstruct:wood"
            ],
            "transformer": {
              "type": "tconstruct:recolor_sprite",
              "color_mapping": {
                "type": "tconstruct:grey_to_color",
                "palette": palette
              }
            },
            "variant": True
          }
        }
        self.cache.saveJson(data, ASSETS, "tconstruct", FOLDER, "wood", variant)
        self.materials += 1
        