import komand
from .schema import ConnectionSchema

# Custom imports below
import ssl
from metasploit.msfrpc import MsfRpcClient
from komand_rapid7_metasploit.connection.schema import Input


class Connection(komand.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None

    def connect(self, params):
        try:
            _create_unverified_https_context = ssl._create_unverified_context
        except AttributeError as e:
            self.logger.debug(e)
        else:
            ssl._create_default_https_context = _create_unverified_https_context
        self.logger.info("Connect: Connecting...")
        self.logger.info(params)
        password = unicode(params.get(Input.CREDENTIALS)["password"]).encode("utf-8")
        new_params = {}
        self.recursive_encode_params(params, new_params)
        params = {unicode(k).encode("utf-8"): unicode(v).encode("utf-8") for k, v in params.iteritems()}
        self.logger.info(new_params)
        self.client = MsfRpcClient(password, **new_params)
        self.logger.info("Client connection established")

    def recursive_encode_params(self, template_dict, building_dict):
        for k, v in template_dict.iteritems():
            new_key = unicode(k).encode("utf-8")
            if isinstance(v, dict):
                building_dict[new_key] = self.recursive_encode_params(template_dict[k],{})
            else:
                building_dict[new_key] = unicode(v).encode("utf-8")
        return building_dict
