# here we are fetching file location from constants.py
# and using two modules read_yaml to extract the paths and create_directories from utils.common.py

from mlProject.constants import *
from mlProject.utils.common import read_yaml, create_directories
"""
need to import entity i.e. class in this notebook to use it
"""
from mlProject.entity.config_entity import DataIngestionConfig 

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