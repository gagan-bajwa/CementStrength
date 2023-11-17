from src.CementStrength.pipelines.stage_01_data_ingestion import Data_ingestion_pipeline
from src.CementStrength.pipelines.stage_02_data_validation import Data_validation_pipeline
from src.CementStrength.pipelines.stage_03_dbOperations import DbOperation_pipeline
from src.CementStrength.pipelines.stage_04_training import Training_pipeline
from src.CementStrength.pipelines.stage05_evaluation import Evaluation_pipeline
from src.CementStrength import logger


STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = Data_ingestion_pipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_validation = Data_validation_pipeline()
   data_validation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "DB Operation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   db_operation = DbOperation_pipeline()
   db_operation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Training stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   training_operation = Training_pipeline()
   training_operation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Evaluation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   evaluation_operation = Evaluation_pipeline()
   evaluation_operation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e