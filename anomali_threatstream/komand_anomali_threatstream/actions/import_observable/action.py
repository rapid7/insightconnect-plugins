import komand
from .schema import ImportObservableInput, ImportObservableOutput, Component

# Custom imports below
import base64
from copy import copy
from json import JSONDecodeError
from komand.exceptions import PluginException


class ImportObservable(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='import_observable',
                description=Component.DESCRIPTION,
                input=ImportObservableInput(),
                output=ImportObservableOutput())

    def run(self, params={}):
        self.request = copy(self.connection.request)
        self.request.url, self.request.method = self.request.url + "/intelligence/import/", "POST"

        file_ = params.get('file', None)
        try:
            file_bytes = base64.b64decode(file_['content'])
        except:
            raise PluginException(cause="Unable to decode base64.",
                                  assistance="Contents of the file must be encoded with base64!")

        data = {}
        observable_settings = params["observable_settings"]
        # Format observable settings
        if observable_settings.get("expiration_ts").startswith("0001-01-01"):
            del observable_settings["expiration_ts"]
        for key, value in observable_settings.items():
            if key == "notes" or key == "trustedcircles":
                value = ",".join(str(val) for val in value)

            data[key] = value
        self.request.files = {"file": (file_["filename"], file_bytes)}
        self.request.data = data
        response = self.connection.session.send(self.request.prepare(),
                                                verify=self.request.verify)
        if response.status_code not in range(200, 299):
            raise PluginException(cause="Received %d HTTP status code from ThreatStream." % response.status_code,
                                  assistance="Please verify your ThreatStream server status and try again. "
                                             "If the issue persists please contact support. "
                                             "Server response was: %s" % response.text)

        try:
            response_data = response.json()
        except JSONDecodeError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)

        clean_response = komand.helper.clean(response_data)
        return {"results": clean_response}

    def test(self):
        # TODO: Implement test function
        return {}
