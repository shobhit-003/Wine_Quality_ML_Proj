from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_transformation import DataTransformation # here we need to call components also, as we are going to use them also
from mlProject.logging.logging import logger


STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager() # calling the configuration manager
            data_transformation_config = config.get_data_transformation_config() # fetching the object from config manager
            data_transformation = DataTransformation(config = data_transformation_config) # creating the component related to object, only make 1 component
            data_transformation.train_test_spliting() # fetching that component
        except Exception as e:
            raise e
        

if __name__ == '__main':
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = DataTransformationTrainingPipeline() #creating object
        obj.main() # calling the func to create pipeline
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e
