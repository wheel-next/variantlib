import importlib.metadata
import logging
import sys

__version__ = importlib.metadata.version("variantlib")

VARIANT_HASH_LEN = 8

logger = logging.getLogger("variantlib")
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.INFO)
