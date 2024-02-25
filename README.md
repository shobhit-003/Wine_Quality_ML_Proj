# End to End Machine Learning Project

# Task -1
1. Create git hub repo
2. Create the template.py i.e. basic files needed
3. Create requirements.txt
4. Create setup.py -> when we wnat to distribute our python project i.e. we want that other people can also download it and use it.
It contains metadata about the project, such as its name, version, dependencies, and other details necessary for packaging and installing the project.

# Task -2
1. Notebook experiment -> according to problem statement, try different models and come with the best (under research folder)
first try to build whole model like from getting data to predicting in one go and then try to split this notebook in modular coding.
2. Utilities -> logging
                exception (depends whether you want in-built or custom)
                utils -> the most frequent code we write here like read yaml, write yaml, json read code, to avoid repeatedness in entire project

# Task -3

# Project Workflow

1. update config.yaml -> first we will configure it for data ingestion we are fetching data from somewhere (it's not necessary that data will be always on our local machine) and where we want to store it in our local machine
2. update schema.yaml -> needed for machine learning algorithms, as in ML we work with hand-crafted features, we create a record of features and their type, useful at the time of validation to check whether all the columns(features) are present or not