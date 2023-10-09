import os
import sys
import logging

logging_str = "[%(asctime)s]:%(levelname)s:%(module)s:%(message)s"
log_dir = "logs"
log_path = os.path.join(log_dir,"current_logs.log")
os.makedirs(log_dir,exist_ok=True)#exist_ok=True ensures that no error is raised if the directory already exists

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_path),
        logging.StreamHandler(sys.stdout)

    ]
)
logger = logging.getLogger("MyProjectLogger")


