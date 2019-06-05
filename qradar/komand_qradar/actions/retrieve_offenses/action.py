import komand
from .schema import RetrieveOffensesInput, RetrieveOffensesOutput
# Custom imports below
from komand_qradar.util import helpers


class RetrieveOffenses(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='retrieve_offenses',
                description='Retrieve a list of offenses currently in the system',
                input=RetrieveOffensesInput(),
                output=RetrieveOffensesOutput())

    def run(self, params={}):
        url = self.connection.url
        username = self.connection.username
        password = self.connection.password
        token = self.connection.token
        fields = params.get('fields')
        filter = params.get('filter')
        range = params.get('range')

        if token:
            r = helpers.get_offenses(self.logger, url, token=token, fields=fields, filter=filter, range=range)
        else:
            auth = helpers.encode_basic_auth(username, password)
            r = helpers.get_offenses(self.logger, url, basic_auth=auth, fields=fields, filter=filter, range=range)

        return {'offenses': r}

    def test(self):
        url = self.connection.url
        username = self.connection.username
        password = self.connection.password
        token = self.connection.token

        if token:
            success = helpers.test_auth(self.logger, url, token=token)
        else:
            auth = helpers.encode_basic_auth(username, password)
            success = helpers.test_auth(self.logger, url, basic_auth=auth)

        if not success:
            raise Exception('Test: Failed authentication')

        return {"offenses": []}
