import os
from ensure import ensure_annotations
from pathlib import Path
from MLOPS_project import logger
from box import ConfigBox
import yaml
import json
from typing import Any
import joblib
from box.exceptions import BoxValueError
@ensure_annotations
def read_yaml(path_yaml:Path)->ConfigBox:
    try:
        with open(path_yaml) as yaml_file:
            content =yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_yaml}, load Success")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
            

@ensure_annotations

def create_directories(path_directory:list,verbose = True):
    for path in path_directory:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")



@ensure_annotations
def save_json(path:Path,data:dict):
    with open(path,"r") as f:
        json.dump(data,f,indent=4)
    
    logger.info(f"json file created at {path}")


@ensure_annotations

def load_json(path:Path)->ConfigBox:
    with open(path) as p:
        content = json.load(p)
    
    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data:Any,path:Path):
    joblib.dump(value=data,filename=path)
    logger.info(f"binary file saved at {path}")


@ensure_annotations
def load_bin(path:Path)->Any:
    data = joblib.load(path)
    logger.info(f"binary file loaded at {path}")
    return data


@ensure_annotations
def get_size(path:Path)->str:
    sizeKb= round(os.path.getsize(path)/1024)
    return f"{sizeKb} kb"