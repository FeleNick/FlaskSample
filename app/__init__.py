from flask import Flask
import logging.config
import os

# set the path to the logging configuration file
logging_config_path = os.path.join(os.path.dirname(__file__), 'logging.cfg')
# configure logging
logging.config.fileConfig(logging_config_path)

# Create a Flask app instance
app = Flask(__name__)

# Import views and tasks
from app import views
from app import tasks
