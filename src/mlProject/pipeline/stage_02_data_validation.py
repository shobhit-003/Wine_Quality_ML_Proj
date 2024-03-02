from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_validation import DataValidation # here we need to call components also, as we are going to use them also
from mlProject.logging.logging import logger


STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager() # step 1 -> getting the configuration manager
    
        data_validation_config = config.get_data_validation_config() # step 2 -> getting the object of data validation from the config manager like having file path and all
        
        data_validation = DataValidation(config=data_validation_config) # step 3 -> creating the component for this object, make 1 component
        
        data_validation.validate_all_columns() # step 4 -> fetching the component
        


if __name__ == '__main':
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = DataValidationTrainingPipeline() #creating object
        obj.main() # calling the func to create pipeline
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e

