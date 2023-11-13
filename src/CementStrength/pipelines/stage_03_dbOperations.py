from CementStrength.config import ConfigurationManager
from CementStrength.components import DbOperations
class DbOperation_pipeline:
    
    def __init__(self):
        pass

    def main(self): 
      
        db_operation_configurations = ConfigurationManager()
        configs = db_operation_configurations.get_db_operations_config()
        db_operation_obj = DbOperations(config = configs)
        db_operation_obj.connect_to_db()
        db_operation_obj.get_data_into_db()
        db_operation_obj.fetch_data_from_db()