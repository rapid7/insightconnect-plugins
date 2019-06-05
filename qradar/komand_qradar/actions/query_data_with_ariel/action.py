import komand
from .schema import QueryDataWithArielInput, QueryDataWithArielOutput
# Custom imports below
from komand_qradar.util import helpers


class QueryDataWithAriel(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='query_data_with_ariel',
                description='Asynchronously query data using the Ariel Query Language',
                input=QueryDataWithArielInput(),
                output=QueryDataWithArielOutput())

    def run(self, params={}):
        url = self.connection.url
        username = self.connection.username
        password = self.connection.password
        token = self.connection.token
        query = params.get("query")

        if token:
            r = helpers.new_ariel_query(self.logger, url, token=token, query=query)
        else:
            auth = helpers.encode_basic_auth(username, password)
            r = helpers.new_ariel_query(self.logger, url, basic_auth=auth, query=query)

        if not r:
            raise Exception("Run: Error creating new ariel query")
        else:
            return {"search_id": r["search_id"]}

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
