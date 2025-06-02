import logging
from time import perf_counter
from typing import Dict, List
from .cache import CachedOutput

DATA = "data"
FOLDER = "recipes"

class RecipeGenerator:
    """
    Handles the material render info definitions
    """
    
    cache: CachedOutput
    """Cache instance for saving files"""
       
    def __init__(self, cache: CachedOutput):
        self.cache = cache
        self.recipes = 0
        self.time = 0
    
    def __enter__(self) -> "BlockGenerator":
        logging.info("Starting recipe generation")
        self.time = perf_counter()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        self.time = perf_counter() - self.time
        logging.info(f"Generated {self.recipes} recipes in {self.time} seconds")
        return False
    
    
    # Methods for datagen root to call
    def material(self, material: str, ingredient: Dict, mod_id: str, *path: str, needed: int = 1, value: int = 1, leftover: str = None) -> None:
        """Creates a material recipe at the given path"""
        data = {
          "type": "tconstruct:material",
          "ingredient": ingredient,
          "material": material,
          "needed": needed,
          "value": value
        }
        # only set leftover if used
        if leftover is not None:
            data["leftover"] = leftover
        self.cache.saveJson(data, DATA, mod_id, FOLDER, *path)
        self.recipes += 1
        
    # Methods for datagen root to call
    def embellishment(self, material: str, inputs: List[Dict], tools: Dict, mod_id: str, path: List[str]) -> None:
        """Creates a material recipe at the given path"""
        self.cache.saveJson({
          "type": "tconstruct:swappable_modifier",
          "allow_crystal": False,
          "inputs": inputs,
          "result": {
            "name": "tconstruct:embellishment",
            "value": material
          },
          "tools": tools,
          "variant_formatter": "tconstruct:material"
        }, DATA, mod_id, FOLDER, *path)
        self.recipes += 1
    
    def woodEmbellishment(self, material: str, planks_id: str, mod_id: str, *path: str) -> None:
        self.embellishment(
          material=material,
          inputs=[
            { "item": planks_id },
            { "item": "tconstruct:pattern" },
            { "item": planks_id },
          ],
          tools={ "tag": "tconstruct:modifiable/embellishment/wood"},
          mod_id=mod_id,
          path=path
        )