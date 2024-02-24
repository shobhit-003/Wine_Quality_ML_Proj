import os
from pathlib import Path
import logging

# Insted of creating files manually in folder, we are writing commands to create files
# therefore we are keeping log to check whether file is created or not
# we are keeping this in terminal only, here we are not making any log folder in directory to check this
logging.basicConfig(level = logging.INFO, format = '[%(asctime)s]: %(message)s:')

project_name = "mlProject" # any name we want to give

# __init__.py -> If we want to use/install any folder as local package then we create __ini__.py constructor file in it to make it a package
# another method -> using sys command, then we have to give the path in interpreter which is very hectic and have to do it every time but on server we can't do like this

# we can access python files within a folder just simply write import "file_name"
# Use of local package -> .py file itself a package but if a python file is in another folder then we can't directly access it like
# from src.data_ingestion import main then this data_ingestion should be a manually created package


list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
]


# as we have to create all this files, i have to iterate on this list

for filepath in list_of_files:
    filepath = Path(filepath) # what is the use of Path()
    # it used to create path objects, which represent paths to files in a "platform-independent way"
    # as windows use backward slash (\) while linux use (\) for th path, so there will be error as OS changes
    # hence we use this function

    filedir, filename = os.path.split(filepath) # splitting the dir and file
    # if there is no dir like "app.py" then it will return filedir as empty and filename as app.py
    # only filename i.e. with extension will be considered as filename and before that every thing as filedir
    # ex . for "src/{project_name}/entity/config_entity.py"
    # filedir : src/mlproject/entity
    # filename : config_entity.py


    if filedir != "": # if there is directory
        os.makedirs(filedir, exist_ok=True) # then create this file as dir, if already present then it will no throw error by using exist_ok = True
        logging.info(f"Creating directory: {filedir} for the file : {filename}")

    # dir is created, now we have to create files in it, if any
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # 1st cod : checking whether at this locatio nfile exist or not, if not exist then go inside if i.e. create it
        # 2nd cod : if it is available then its size is 0 or not i.e. empty or not
        # 2nd cod is redundant bcoz if it is already present, doesn't matter empty or not, 1st cod will not allow to enter inside th if cod
        
        with open (filepath, "w") as f:
            # we have to give full file path to create file at particular location thatswhy give filepath instead of filename
            pass # have nothing to do here, just want to create file
            logging.info(f"Creating empty file : {filepath}")

    else:
        logging.info(f"{filename} is already exists in {filedir} folder")


