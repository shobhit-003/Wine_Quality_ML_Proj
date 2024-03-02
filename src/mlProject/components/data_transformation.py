import os
import pandas as pd
from sklearn.model_selection import train_test_split
from mlProject.logging.logging import logger

# import entity i.e. skeleton (just to tell that we are going to use this type of data type). So what about the value?
# in the pipeline we will call life func i.e. get_data_transformation_config to give life to it
# and then we will call component i.e. this func and we will pass the alive obj in the constructor of this class

from mlProject.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
    
    ## Note: We do all the feature engineering and EDA here
    
    # here we are doing only train tes split as data is already clean
    # make separate func for separate operation
    
    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)

        # Split the data into training and test sets. (0.75, 0.25) split.
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index= False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index= False)

        logger.info("Spliited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)