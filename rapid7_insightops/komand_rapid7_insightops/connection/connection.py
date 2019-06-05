import komand
from .schema import ConnectionSchema
# Custom imports below


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api_key = None
        self.insighturl = None
        self.postopsdataurl = None

    def connect(self, params):
        self.api_key = params["api_key"].get("secretKey")
        self.insighturl = "https://{}.rest.logs.insight.rapid7.com".format(params["region"])
        self.postdataurl = "https://{}.js.logs.insight.rapid7.com/v1/noformat/".format(params["region"])

        self.logger.info("Connect: Connecting..")
