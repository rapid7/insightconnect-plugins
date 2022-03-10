import insightconnect_plugin_runtime
from .schema import ConnectionSchema

# Custom imports below


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    # pylint: disable=unused-argument
    def connect(self, params={}):
        pass

    def test(self, params={}):
        url = "https://www.google.com"
        insightconnect_plugin_runtime.helper.check_url(url)
        return {}
