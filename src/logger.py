import logging # Provides functions for logging messages (INFO, WARNING, ERROR)
import os # Used to interact with the operating system (e.g., create directories).
from datetime import datetime #  Used to generate timestamps dynamically.


# Generate a Log File Name with Timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create a Directory for Logs
logs_path = os.path.join(os.getcwd(), "logs")

os.makedirs(logs_path, exist_ok=True) # creates the "logs" directory if it doesn't exist. exist_ok=True prevents an error if the directory already exists.

# Define Full Path for the Log File
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
# logging.basicConfig() is a method in Python's logging module that configures the basic settings for logging. It is used to define:
# Where logs should be stored (file or console).
# # How log messages should be formatted.
# Which level of logs should be recorded