import komand
from .schema import ConnectionSchema
# Custom imports below
import logging.config

# Use a custom logger to decrease verbosity for matplotlib
logging.getLogger("matplotlib").setLevel(logging.INFO)


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        pass
