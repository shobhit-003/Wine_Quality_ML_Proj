# End to End Machine Learning Project

# Task -1
1. Create git hub repo
2. Create the template.py i.e. basic files needed
3. Create requirements.txt
4. Create setup.py -> when we want to distribute our python project i.e. we want that other people can also download it and use it.
It contains metadata about the project, such as its name, version, dependencies, and other details necessary for packaging and installing the project.

As we have created our 'mlProject' as package which can be distributed, we can directly access it withotut src, like from mlProject.whatever instead of from src.mlProject.whatever

# Task -2
1. Notebook experiment -> according to problem statement, try different models and come with the best (under research folder)
first try to build whole model like from getting data to predicting in one go and then try to split this notebook in modular coding.
2. Utilities -> logging,
                exception (depends whether you want in-built or custom),
                utils -> the most frequent code we write here like read yaml, write yaml, json read code, to avoid repeatedness in entire project

# Task -3

# Project Workflow

NOTE :- We put the entities and configuration manager for all the items in single file i.e. entity.config_entity.py and config.configuration.py but we make separate files for the components and pipeline, components can be different for different entities

Here we will first create notebooks for data ingestion (fetch data from database and load on local device and extract it), data validation (now verify whether correct data is downloaded or not i.e. it is the same data (i.e. same features) which we used at the time of training) and data transformation (now apply the necessary transformation) and then will convert them into modular coding by using these steps ->


1. update config.yaml -> here we write that what all things we are going to create and then define attributes of particular thing with their source(in case if fetching) or destination(in case creating) directories, so that in future if we are going to change any directory or any path or data then we just need to change in it

2. update schema.yaml -> needed for machine learning algorithms, as in ML we work with hand-crafted features, we create a record of features and their type, useful at the time of validation to check whether all the columns(features) are present or not

3. update params.yaml -> put the model hyperparameters in it, so we can tune hyperparameter here only.

4. update the constants -> put the path links of config.yaml, schema.yaml and params.yaml are in this folder (as these folders items i.e. data ingestion source, data's feature (in case of ML), and hyperparameter are not going to change, we keep them under constants)

5. update/create the entity (class skeleton)-> create data class and assign variables which you are going to use along with their data type, and in the class we are going to use the same variables which we have already defined in config.yaml, params.yaml and schema.yaml.

Example : data_validation requires variable from config.yaml and schema.yaml(all cols)

model_trainer requires variables from config.yaml, params.yaml and schmea.yaml(target col)


6. update the configuration manager in src config -> here you are giving life to your skeleton i.e. creating an object and assigning values to variables and it's obvious then it should return this object

like in case of data ingestion, it  will create an object which is having the root_dir, source_url, local_data_file, unzip_dir in it.

similarly for data validation it will have root_dir, status_file, unzip_data_dir and schema in it

7. update the component -> now create the component related to entity like

for data ingestion - first download the file and then extract the zip file

for data  validation - validate all the columns

8. update the pipeline (training pipeline) -> pipeline is nothing but sequence of methods, which you want to call first and so on. To understand the flow for data ingestion that what we are doing and why we are doing, just see the pipeline.

9. update main.py -> launch the pipeline in main.py

# Task - 4

1. Create model trainer, model eval components by using the steps shown in task - 3.

2. Create prediction pipeline -> We have to create data pipeline using pickle because when user is giving data to model and if it is not clean then we need transformations to perform on this data, here data was clean so we are doing only train_test_split, if there is more transformation steps then it's good to make pipeline using pickle.

*Note : We have to make prediction pipeline only in the pipeline folder i.e. no entity, configuration and all.