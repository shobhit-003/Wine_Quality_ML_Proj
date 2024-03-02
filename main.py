from mlProject.logging.logging import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = DataIngestionTrainingPipeline() #creating object
    obj.main() # calling the func to create pipeline
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx=======x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = DataValidationTrainingPipeline() #creating object
    obj.main() # calling the func to create pipeline
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx=======x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = DataTransformationTrainingPipeline() #creating object
    obj.main() # calling the func to create pipeline
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx=======x")
except Exception as e:
    logger.exception(e)
    raise e