from CementStrength.utils import read_yaml,create_directories
from CementStrength.entity import DataIngestionConfig
from CementStrength.constants import *





class ConfigurationManager:
    
      def __init__(self, 
                config_file= CONFIG_FILE_PATH,
                param_file = PARAMS_FILE_PATH):

            self.config_file = read_yaml(config_file)
            self.param_file = read_yaml(param_file)
            create_directories(self.config_file.data_ingestion.root_dir)  
      def get_data_ingestion_config(self) -> DataIngestionConfig:
            data_ingestion_config = DataIngestionConfig(
            root_dir = self.config_file.data_ingestion.root_dir,
            source_URL = self.config_file.data_ingestion.source_URL,
            local_data_file = self.config_file.data_ingestion.local_data_file,
            unzip_dir = self.config_file.data_ingestion.unzip_dir
                        
                  )
            return data_ingestion_config