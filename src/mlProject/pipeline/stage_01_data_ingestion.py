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
        config = ConfigurationManager() # step 1 -> fetching all the yaml files (config, params, schema) and creating folder 'artifacts'
    
        data_ingestion_config = config.get_data_ingestion_config() # step 2 -> now this object has all the info regarding data ingestion that
        # from where it has to take data(url) and dump it(local machine) and unzipping and also create 'data_ingestion' folder inside 'artifacts' folder 
        
        data_ingestion = DataIngestion(config=data_ingestion_config) # step 3 -> creating an obj by passing all the arguments get in step 2.
        
        data_ingestion.download_file() # step 4
        
        data_ingestion.extract_zip_file() # step 5


if __name__ == '__main':
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = DataIngestionTrainingPipeline() #creating object
        obj.main() # calling the func to create pipeline
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e

