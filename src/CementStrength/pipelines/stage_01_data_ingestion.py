
from CementStrength.config import ConfigurationManager
from CementStrength.components import DataIngestion



class Data_ingestion_pipeline:
    
    def __init__(self):
        pass

    def main(self): 
      
        data_ingestion_configurations = ConfigurationManager()
        configs = data_ingestion_configurations.get_data_ingestion_config()
        data_ingestion_obj = DataIngestion(config = configs)
        data_ingestion_obj.download_and_unzip_data()