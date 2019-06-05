import komand
from .schema import GetArielQueryResultsInput, GetArielQueryResultsOutput
# Custom imports below
from komand_qradar.util import helpers


class GetArielQueryResults(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_ariel_query_results',
                description='Gets the results of an Ariel query by search ID',
                input=GetArielQueryResultsInput(),
                output=GetArielQueryResultsOutput())

    def run(self, params={}):
        url = self.connection.url
        username = self.connection.username
        password = self.connection.password
        token = self.connection.token

        search_id = params.get("search_id")

        if token:
            r = helpers.get_ariel_query_results(self.logger, url, token=token, search_id=search_id)
        else:
            auth = helpers.encode_basic_auth(username, password)
            r = helpers.get_ariel_query_results(self.logger, url, basic_auth=auth, search_id=search_id)

        if not r:
            raise Exception("Run: Error getting ariel query results")
        else:
            return r

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

        return {}
