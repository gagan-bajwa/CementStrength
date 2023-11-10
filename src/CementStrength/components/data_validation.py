from CementStrength.entity import DataValidationConfig
from CementStrength import logger
import shutil,re,os
from CementStrength.utils import read_yaml,create_directories
import pandas as pd


class DataValidation:
    def __init__(self,config: DataValidationConfig):
        self.config = config

    def file_name_check(self):
        logger.info("file name check started")
        create_directories(self.config.good_dir)
        create_directories(self.config.bad_dir)

        # cement_strength_08012020_120021
        filepath = self.config.source_dir
        pattern = r'cement_strength_\d{8}_\d{6}.csv'
        for file in os.listdir(filepath):
            match = re.search(pattern, file)
            if match:
                if not os.path.exists(os.path.join(self.config.good_dir, file)):
                    shutil.copy(os.path.join(self.config.source_dir,file), self.config.good_dir)
                else:
                    logger.info("file already exists")
            else:
                if not os.path.exists(os.path.join(self.config.bad_dir, file)):
                    shutil.copy(os.path.join(self.config.source_dir,file), self.config.bad_dir)
                else:
                    logger.info("file already exists") 

    def column_check(self):
        filepath = self.config.good_dir
        for file in os.listdir(filepath):
            print(file)
            df = pd.read_csv(os.path.join(self.config.good_dir, file))
            if df.shape[1]!=9:
                shutil.move(os.path.join(self.config.good_dir,file), self.config.bad_dir)
                logger.info(f"file {file} transferrred to bad folder")
        logger.info("file check completed")
            