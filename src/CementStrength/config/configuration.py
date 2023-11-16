from CementStrength.utils import read_yaml,create_directories
from CementStrength.entity import DataIngestionConfig,DataValidationConfig,DbOperationsConfig,TrainingConfig
from CementStrength.constants import *





class ConfigurationManager:
    
      def __init__(self, 
                config_file= CONFIG_FILE_PATH,
                param_file = PARAMS_FILE_PATH):

            self.config_file = read_yaml(config_file)
            self.param_file = read_yaml(param_file)
            
            
      
      def get_data_ingestion_config(self) -> DataIngestionConfig:
            create_directories(self.config_file.data_ingestion.root_dir)  
            create_directories(self.config_file.data_validation.good_dir)
            create_directories(self.config_file.data_validation.bad_dir)
            data_ingestion_config = DataIngestionConfig(
            root_dir = self.config_file.data_ingestion.root_dir,
            source_URL = self.config_file.data_ingestion.source_URL,
            local_data_file = self.config_file.data_ingestion.local_data_file,
            unzip_dir = self.config_file.data_ingestion.unzip_dir
                        
                  )
            return data_ingestion_config
      
      def get_data_validation_config(self) -> DataValidationConfig:
            data_validation_config = DataValidationConfig(
                source_dir = self.config_file.data_validation.source_dir,   
                good_dir =  self.config_file.data_validation.good_dir,
                bad_dir = self.config_file.data_validation.bad_dir
                        
                  )
            return data_validation_config
      
      def get_db_operations_config(self) -> DbOperationsConfig:
            db_operations_config = DbOperationsConfig(
                  source_dir = self.config_file.db_operations.source_dir,
                  db_dir= self.config_file.db_operations.db_dir,
                  db_name= self.config_file.db_operations.db_name,
                  training_dir = self.config_file.db_operations.training_dir,
                  training_file= self.config_file.db_operations.training_file             
                  )
            return db_operations_config

      def get_training_config(self) -> TrainingConfig:
                       
            training_config = TrainingConfig(
                  source_dir = self.config_file.training.source_dir,
                  training_dir = self.config_file.training.training_dir,
                  local_training_file = self.config_file.training.local_training_file,
                  preprocessed_data_dir = self.config_file.training.preprocessed_data_dir,
                  preprocessed_data= self.config_file.training.preprocessed_data,
                  Models_dir= self.config_file.training.Models_dir,
                  images= self.config_file.training.images
                           
                  )
            return training_config