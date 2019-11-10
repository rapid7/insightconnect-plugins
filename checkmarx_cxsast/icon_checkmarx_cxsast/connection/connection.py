import komand
from .schema import ConnectionSchema

# Custom imports below
from icon_checkmarx_cxsast.util.api import CheckmarxCxSAST


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        """
        grant_type: Value must be set as 'password'
        scope: Value must be set as 'access_control_api'
        client_id: Value must be set as 'resource_owner_client'
        client_secret: Value must be set as '014DF517-39D1-4453-B7B3-9930C563627C'
            (from documentation, not really 'secret')
        """

        self.logger.info("Connect: Connecting...")
        self.client = CheckmarxCxSAST(
          params["host"],
          self.logger,
          params["credentials"]["username"],
          params["credentials"]["password"],
        )

    def test(self):
        """
        Returning nothing since connect is called before test
        This means the login attempt will "test" the connection
        """
        return {}
