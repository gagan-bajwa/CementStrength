from CementStrength.entity import TrainingConfig,DbOperationsConfig
from CementStrength import logger
from CementStrength.utils import read_yaml,create_directories
import shutil



class DbOperations:
    def __init__(self,config: TrainingConfig):
        self.config = config

    def copy_training_file(self):
        create_directories(self.config.training_dir)
        shutil.copy(self.config.source_dir,self.config.local_training_file)
        logger.info("file copied")