from CementStrength.config import ConfigurationManager
from CementStrength.components import Training
class Training_pipeline:
    
    def __init__(self):
        pass

    def main(self): 
      
        training_configurations = ConfigurationManager()
        configs = training_configurations.get_training_config()
        train = Training(config=configs)
        train.copy_training_file()
        train.preprocessing()
        train.clustering()
        train.regressor()