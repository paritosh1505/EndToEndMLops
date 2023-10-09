import os
from pathlib import Path
import logging

#it sets up the default logging behavior for your script.
#It sets the logging level to INFO.The INFO level is typically used for general information messages. Other common logging levels include DEBUG, WARNING, ERROR, and CRITICAL, each representing a different level of severity for log messages.
# log messages will be formatted as [timestamp]:message. Actual log messages will replace message, and the timestamp will be in the specified format.

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s')

project_name = "MLOPS_project"

list_file =[
".github/workflows/.gitkeep",
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
"Dockerfile",
"requirements.txt",
"setup.py",
"research/trials.ipynb",
"templates/index.html"

]

for filepath in list_file:
    filePath = Path(filepath)
    filedir,filename = os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")
    if(not os.path.exists(filePath) )or (os.path.getsize(filePath)==0):
        with open(filePath,"w") as f:
            pass
            logging.info(f"Create Empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exist")
