import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
# Custom imports below
from ..util.api import CortexXdrAPI


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.xdr_api = None

    def connect(self, params):
        """
        Connection config params are supplied as a dict in
        params or also accessible in self.parameters['key']

        The following will setup the var to be accessed
          self.blah = self.parameters['blah']
        in the action and trigger files as:
          blah = self.connection.blah
        """
        # TODO: Implement connection or 'pass' if no connection is necessary
        self.logger.info("Connect: Connecting...")
        api_key_id = params.get(Input.API_KEY_ID).get("secretKey")
        api_key = params.get(Input.API_KEY).get("secretKey")
        fqdn = params.get(Input.FQDN)
        self.xdr_api = CortexXdrAPI(api_key_id, api_key, fqdn, self.logger)

    def test(self):
        # TODO: Implement connection test
        pass
