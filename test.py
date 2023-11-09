from src.CementStrength import logger
logger.info("logging test")
from src.CementStrength.utils.common import read_yaml,create_directories
from src.CementStrength.constants import *

read_yaml(CONFIG_FILE_PATH)
logger.info("yaml read complete")