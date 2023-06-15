from unittest.mock import MagicMock
import logging
from icon_trendmicro_visionone.connection.connection import Connection
import os
import json
import importlib
import inspect
import pytmv1


def import_all_classes_from_subdirs(path):
    classes = {}
    # Iterate over all files and subdirectories in the provided path
    for root, dirs, files in os.walk(path):
        for file in files:
            # If the file is not 'action.py' or 'trigger.py', skip it
            if file not in ["action.py", "trigger.py"]:
                continue
            # Create a full module name considering it as a package. Exclude current working directory.
            full_module_name = os.path.join(
                root, file[:-3]
            )  # Remove '.py' from the end
            # Replace / with . for correct module name
            full_module_name = full_module_name.replace("/", ".")
            module = importlib.import_module(full_module_name)
            # Get the class from the module and add it to the dictionary
            for name, cls in inspect.getmembers(module, inspect.isclass):
                if name != "Action" and name != "Trigger":
                    classes[name] = cls
    return classes


ACTION_CLASSES = import_all_classes_from_subdirs("icon_trendmicro_visionone")


def mock_params(action=None):
    with open("/python/src/unit_test/action_io.json") as file_:
        params = json.load(file_)
        if action:
            return params[action]
    return params


def mock_connection():
    connection = Connection()
    connection.logger = logging.getLogger()
    connection.url = "https://tmv1-mock.trendmicro.com"
    connection.key = "Dummy-Secret-Token"
    connection.app = "TM-R7"
    connection.client = pytmv1.client(connection.app, connection.key, connection.url)
    return connection


def mock_action(connection, action_name=None):
    if action_name:
        action = ACTION_CLASSES[action_name]()
    else:
        action = MagicMock()
    action.connection = connection
    return action
