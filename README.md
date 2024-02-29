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

1. update config.yaml -> first we will configure it for data ingestion we are fetching data from somewhere (it's not necessary that data will be always on our local machine) and where we want to store it in our local machine

2. update schema.yaml -> needed for machine learning algorithms, as in ML we work with hand-crafted features, we create a record of features and their type, useful at the time of validation to check whether all the columns(features) are present or not

3. update params.yaml

4. update the constants -> put the path links of config.yaml, schema.yaml and params.yaml are in this folder (as these folders items i.e. data ingestion source, data's feature (in case of ML), and hyperparameter are not going to change, we keep them under constants)

5. update/create the data ingestion entity -> here entity is nothing but data ingestion, the config we have setup in config.yaml, make a dataclass of that type

6. update the configuration manager for data ingestion in src config -> it will return all the root_dir, source_url, local_data_file, unzip_dir in one shot

7. update the data ingestion component -> now download the data and extract it.

8. update the pipeline -> pipeline is nothing but sequence of methods, which you want to call first and so on. To understand the flow for data ingestion that what we are doing and why we are doing, just see the pipeline.

9. update main.py -> launch the data ingestion in main.py