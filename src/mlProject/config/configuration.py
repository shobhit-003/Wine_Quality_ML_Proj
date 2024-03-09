# here we are fetching file location from constants.py
# and using two modules read_yaml to extract the paths and create_directories from utils.common.py

from mlProject.constants import *
from mlProject.utils.common import read_yaml, create_directories
"""
need to import entity i.e. skeleton in this notebook to use it i.e. to give it to life
"""
from mlProject.entity.config_entity import DataIngestionConfig 
from mlProject.entity.config_entity import DataValidationConfig
from mlProject.entity.config_entity import DataTransformationConfig
from mlProject.entity.config_entity import ModelTrainerConfig
from mlProject.entity.config_entity import ModelEvaluationConfig

class ConfigurationManager:
    # as soon as obj created, it should read the yaml files and create artifact folder related to data ingestion
    def __init__(
            self,
            config_filepath = CONFIG_FILE_PATH,
            params_file_path = PARAMS_FILE_PATH,
            schema_file_path = SCHEMA_FILE_PATH):
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_file_path)
        self.schema = read_yaml(schema_file_path)

        create_directories([self.config.artifacts_root]) # in the config.yaml, artifacts_root is key, fetch it's value (which is folder name)
        # which we are going to create in the main dir and this create_directories and read_yaml are common funcs defined in utils 


    def get_data_ingestion_config(self) -> DataIngestionConfig: # in python class can also be return type
        config = self.config.data_ingestion # in config 'data_ingestion' is nested dictionary
                                            # we are just copying  its inner key value pairs to another variable namely 'config'
        
        create_directories([config.root_dir]) # root_dir is holding the path artifacts\data_ingestion

        data_ingestion_config = DataIngestionConfig( # creating the object of class
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config # returning the object
    


    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation # get the configuration for data validation from whole configuration
        schema = self.schema.COLUMNS # get the schema used in training

        create_directories([config.root_dir]) # create the root_dir i.e. 'data validation' folder inside artifacts folder

        data_validation_config = DataValidationConfig(
            root_dir = config.root_dir,
            status_file = config.status_file,
            unzip_data_dir = config.unzip_data_dir,
            all_schema = schema
        )

        return data_validation_config # return the object
    



    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path
        )

        return data_transformation_config
    


    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.ElasticNet
        schema =  self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path = config.train_data_path,
            test_data_path = config.test_data_path,
            model_name = config.model_name,
            alpha = params.alpha,
            l1_ratio = params.l1_ratio,
            target_column = schema.name
            
        )

        return model_trainer_config
    


    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        params = self.params.ElasticNet
        schema =  self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            test_data_path=config.test_data_path,
            model_path = config.model_path,
            all_params=params,
            metric_file_name = config.metric_file_name,
            target_column = schema.name
           
        )

        return model_evaluation_config
