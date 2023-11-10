from pathlib import Path
from box import Box 
import yaml
import os
from CementStrength import logger

"""def read_yaml(path: Path):
    with open(path,'r') as file:
        config_load = Box(yaml.safe_load(file))
        logger.info("yaml file read completed successfully")
        return config_load"""

def create_directories(path: Path):
    dir = os.path.join(path)
    os.makedirs(dir,exist_ok=True)
    logger.info("directory created")



def read_yaml(path_to_yaml: Path):
    with open(path_to_yaml) as yaml_file:
        content = Box(yaml.safe_load(yaml_file))
        logger.info(f"yaml file: {path_to_yaml} loaded successfully")
        return (content)
    e