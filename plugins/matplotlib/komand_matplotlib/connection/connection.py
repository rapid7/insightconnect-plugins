import insightconnect_plugin_runtime
from .schema import ConnectionSchema

# Custom imports below
import logging.config

# Use a custom logger to decrease verbosity for matplotlib
logging.getLogger("matplotlib").setLevel(logging.INFO)


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        pass
