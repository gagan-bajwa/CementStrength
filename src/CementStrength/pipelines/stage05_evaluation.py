from CementStrength.config import ConfigurationManager
from CementStrength.components import Evaluation
class Evaluation_pipeline:
    
    def __init__(self):
        pass

    def main(self): 
      
        evaluation_configurations = ConfigurationManager()
        configs = evaluation_configurations.get_evaluation_config()
        evaluate = Evaluation(config=configs)
        evaluate.evaluate()
        