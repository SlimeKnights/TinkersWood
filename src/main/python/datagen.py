import logging
from time import perf_counter
from tinkerswood.cache import CachedOutput
from tinkerswood.logger import setupLogging

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
    
    # end of datagen, save the cache file
    cache.finalize()
    logging.info(f"Finished running datagen in {perf_counter() - startTime} seconds")