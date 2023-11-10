from CementStrength.config import ConfigurationManager
from CementStrength.components import DataValidation
class Data_validation_pipeline:
    
    def __init__(self):
        pass

    def main(self): 
      
        data_validation_configurations = ConfigurationManager()
        configs = data_validation_configurations.get_data_validation_config()
        data_validation_obj = DataValidation(config = configs)
        data_validation_obj.file_name_check()
        data_validation_obj.column_check()