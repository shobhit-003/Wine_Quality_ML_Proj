import pandas as pd


# import entity i.e. skeleton (just to tell that we are going to use this type of data type). So what about the value?
# in the pipeline we will call life func i.e. get_data_validation_config to give life to it
# and then we will call component i.e. this func and we will pass the alive obj in the constructor of this class

from mlProject.entity.config_entity import DataValidationConfig



class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config


    def validate_all_columns(self)-> bool:
        try:
            overall_validation_status = True

            data = pd.read_csv(self.config.unzip_data_dir) # data we are fetching now
            data_cols = data.dtypes.to_dict() # data type of cols along with cols

            all_schema = self.config.all_schema # data used at the time of training

            for column_name, data_type in data_cols.items():

                if ((column_name in all_schema) and (all_schema[column_name] == data_type)): # if col is present and it's type is also matching
                    val_status = True
                    
                    with open(self.config.status_file, 'a') as f:
                        f.write(f"Col Name: {column_name}, Col type: {data_type} \nValidation Status: {val_status} \n")

                elif ((column_name in all_schema) and (all_schema[column_name] != data_type)): # col is present but type is not matching
                    val_status = False
                    overall_validation_status = False
                    
                    with open(self.config.status_file, 'a') as f:
                        f.write(f"Col Name: {column_name}, Col type: {data_type}, Existing_Col_type: {all_schema[column_name]} \nValidation Status: {val_status} \n")
                    raise Exception('Data type is not matching, terminating the further data fetching process')

                else: # col is not present
                    val_status = False
                    overall_validation_status = False
                    
                    with open(self.config.status_file, 'a') as f:
                        f.write(f"Col Name: {column_name}, Col type: {data_type} \nValidation Status: {val_status} \n")
                    raise Exception("Column does not exist, terminating the further data fetching process")

            return overall_validation_status
        
        except Exception as e:
            print(e)