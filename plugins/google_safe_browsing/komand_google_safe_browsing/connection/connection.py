import komand
from .schema import ConnectionSchema
from komand.exceptions import PluginException

# Custom imports below


class Connection(komand.Connection):

    API_KEY = None

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        raise PluginException(cause="This plugin is obsolete. Please use the Google Web Risk plugin instead.")
