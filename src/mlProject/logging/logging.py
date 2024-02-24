import os
import sys
import logging

# why we need logging?
# at the production server, we dom't have terminals to see where and what is going on
# we keep the track by creating this "logs" dir
# and for exception handling also, we use logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
# there are many severity levels in logging (info, debug, warning, error, critical)
# module will show the module or file name from where logging is done

log_dir = "logs"

log_filepath = os.path.join(log_dir, "running_log.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format = logging_str,

    handlers = [
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

# create an object to emit log messages from the application
# now whenever and whereever we have to log, we have to call this object
logger = logging.getLogger()

# FileHandler writes log msgs to a file specified by log_filepath
# StreamHandler writes log msgs in terminal