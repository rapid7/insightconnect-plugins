import komand
from .schema import AddApprovalIndicatorInput, AddApprovalIndicatorOutput
# Custom imports below
import base64
from copy import copy
from json.decoder import JSONDecodeError


class AddApprovalIndicator(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_approval_indicator',
                description='Import indicator(s) into Anomali with approval',
                input=AddApprovalIndicatorInput(),
                output=AddApprovalIndicatorOutput())

    def run(self, params={}):
        self.request = copy(self.connection.request)
        self.request.url, self.request.method = self.request.url + "/intelligence/import/", "POST"

        file_ = params.get('file', None)
        try:
            file_bytes = base64.b64decode(file_['content'])
        except:
            raise Exception("Error: Unable to decode base64. Contents of the file must be encoded with base64!")

        data = {}
        indicator_settings = params["indicator_settings"]
        # Format indicator settings
        if indicator_settings.get("expiration_ts").startswith("0001-01-01"):
            del indicator_settings["expiration_ts"]
        for key, value in indicator_settings.items():
            if key == "notes" or key == "trustedcircles":
                value = ",".join(str(val) for val in value)

            data[key] = value
        self.request.files = {"file": (file_["filename"], file_bytes)}
        self.request.data = data
        response = self.connection.session.send(self.request.prepare(),
                                                verify=False)
        if response.status_code not in range(200, 299):
            raise Exception(
                "Error: Received %d HTTP status code from ThreatStream. Please verify your ThreatStream server "
                "status and try again. If the issue persists please contact support. "
                "Server response was: %s" % (
                    response.status_code, response.text))

        try:
            response_data = response.json()
        except JSONDecodeError:
            raise Exception(
                "Error: Received an unexpected response from ThreatStream "
                "(non-JSON or no response was received). Response was: %s" % response.text)

        clean_response = komand.helper.clean(response_data)
        return {"results": clean_response}

    def test(self):
        # TODO: Implement test function
        return {}
