import os
import urllib.request as request # with the help of it, we download the data from the given url
import zipfile # to unzip the file
from pathlib import Path
from mlProject.logging.logging import logger
from mlProject.utils.common import get_size
""""
Don't be confused as we have used 'DataIngestionConfig' name at two places
so which should be placed here? this thing will occur will all, like with DataValidationConfig too


from mlProject.config.configuration import DataIngestionConfig
or
from mlProject.entity.config_entity import DataIngestionConfig

As we are making component i.e. entity so import entity
in the entity, we just define data types i.e. entity is just skeleton
configuration manager is basically setting up the entity like folder creation and fetching the links
i.e. in config manager we are giving the values to variables defined in the entity i.e. giving life
even config.configuration doesn't have DataIngestionConfig, it is also importing it from entity
"""

# import entity i.e. skeleton bcoz we will call config. in the constructor and give life to it
from mlProject.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config # fetching all the details from configuration manager

    # downloading data file
    def download_file(self):
        # if data is not present on local device then get it from souce
        # like when we download MNIST from torch.dataset, same thing happens
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_url,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

        
    def extract_zip_file(self):
        """"
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

        