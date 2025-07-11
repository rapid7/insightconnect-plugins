import insightconnect_plugin_runtime
from .schema import ImportObservableInput, ImportObservableOutput, Component, Input, Output

# Custom imports below
import base64
from copy import copy
from insightconnect_plugin_runtime.exceptions import PluginException


class ImportObservable(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="import_observable",
            description=Component.DESCRIPTION,
            input=ImportObservableInput(),
            output=ImportObservableOutput(),
        )

    def run(self, params={}):
        self.request = copy(self.connection.api.request)
        self.request.url, self.request.method = self.request.url + "/v2/intelligence/import/", "POST"

        file_ = params.get(Input.FILE, None)
        try:
            file_bytes = base64.b64decode(file_.get("content"))
        except:
            raise PluginException(
                cause="Unable to decode base64.",
                assistance="Contents of the file must be encoded with base64!",
            )

        data = {}
        observable_settings = params.get(Input.OBSERVABLE_SETTINGS, {})
        # Format observable settings

        # If no timestamp is sent, Anomali will default it to 90 days
        if (
            observable_settings.get("expiration_ts", "").startswith("0001-01-01")
            or observable_settings.get("expiration_ts") == ""
        ):
            del observable_settings["expiration_ts"]

        if observable_settings.get("confidence"):
            if not 0 <= observable_settings.get("confidence") <= 100:
                raise PluginException(
                    cause="Confidence score is either above the maximum limit or below the minimum limit.",
                    assistance="Please ensure the confidence score is between 0 and 100.",
                    data=f"Confidence score: {observable_settings.get('confidence')} is either above or below the limit.",
                )

        for key, value in observable_settings.items():
            if key in ("notes", "trustedcircles"):
                value = ",".join(str(val) for val in value)

            data[key] = value

        classification = params.get("classification")
        data["tlp"] = params.get("tlp", None)
        if classification:
            data["classification"] = classification

        self.request.files = {"file": (file_["filename"], file_bytes)}
        self.request.data = data
        response_data = self.connection.api.send(self.request)

        clean_response = insightconnect_plugin_runtime.helper.clean(response_data)
        return {Output.RESULTS: clean_response}
