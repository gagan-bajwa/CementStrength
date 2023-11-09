import zipfile
from CementStrength import logger

import urllib.request as request
from CementStrength.entity import DataIngestionConfig





class DataIngestion:
     
    def __init__(self,config: DataIngestionConfig):
        self.config = config
          
    def download_and_unzip_data(self):
        logger.info("Downloading data")
        filename, headers = request.urlretrieve(url=self.config.source_URL    ,
                                              filename=self.config.local_data_file)
        logger.info("Data downloaded and now Unzipping data")
        with zipfile.ZipFile(file=self.config.local_data_file, mode='r') as zip_ref:
            zip_ref.extractall(self.config.unzip_dir)
            logger.info("data unzipped")