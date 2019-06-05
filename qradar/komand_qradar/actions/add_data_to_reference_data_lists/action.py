import komand
from .schema import AddDataToReferenceDataListsInput, AddDataToReferenceDataListsOutput
# Custom imports below
from komand_qradar.util import helpers


class AddDataToReferenceDataLists(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_data_to_reference_data_lists',
                description='Add data to reference_data lists',
                input=AddDataToReferenceDataListsInput(),
                output=AddDataToReferenceDataListsOutput())

    def run(self, params={}):
        url = self.connection.url
        username = self.connection.username
        password = self.connection.password
        token = self.connection.token

        payload = {
            "element_type": params.get("element_type"),
            "name": params.get("name")
        }
        if params.get("time_to_live"):
            payload["time_to_live"] = params.get("time_to_live")
        if params.get("timeout_type"):
            payload["timeout_type"] = params.get("timeout_type")

        if token:
            r = helpers.add_data_to_reference_data_lists(self.logger, url, token=token, payload=payload)
        else:
            auth = helpers.encode_basic_auth(username, password)
            r = helpers.add_data_to_reference_data_lists(self.logger, url, basic_auth=auth, payload=payload)

        if not r:
            raise Exception("Run: Error adding data to reference list")
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
