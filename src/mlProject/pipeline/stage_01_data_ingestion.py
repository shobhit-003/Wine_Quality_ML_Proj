from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_ingestion import DataIngestion
from mlProject.logging.logging import logger

""""
we have to make a func or class to call pipeline, so we are making a class
in the main func we are creating pipeline
here we do try except block by creating obj of class
"""
STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager() # step 1 -> getting the configuration manager
        
        data_ingestion_config = config.get_data_ingestion_config() # step 2 -> getting the object of data ingestion which is having all info like source file path and all
        
        data_ingestion = DataIngestion(config=data_ingestion_config) # step 3 -> create the component related to this object, make 2 components
        
        data_ingestion.download_file() # step 4 -> fetching the component
        
        data_ingestion.extract_zip_file() # step 5 -> fetching the component


if __name__ == '__main':
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = DataIngestionTrainingPipeline() #creating object
        obj.main() # calling the func to create pipeline
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e

