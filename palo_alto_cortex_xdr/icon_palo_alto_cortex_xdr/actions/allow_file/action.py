import insightconnect_plugin_runtime
from .schema import AllowFileInput, AllowFileOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class AllowFile(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="allow_file", description=Component.DESCRIPTION, input=AllowFileInput(), output=AllowFileOutput()
        )

    def run(self, params={}):
        file_hash = params.get(Input.FILE_HASH)
        comment = params.get(Input.COMMENT)
        incident_id_string = params.get(Input.INCIDENT_ID)

        try:
            incident_id = int(incident_id_string)
        except Exception:
            raise PluginException(
                cause="Failed converting Incident ID to an integer.",
                assistance=f"Please check that Incident ID: {incident_id} is a valid integer.",
            )

        if incident_id and incident_id < 1:  # Not sure if I need this, but just in case.
            incident_id = None

        return {Output.SUCCESS: self.connection.xdr_api.allow_or_block_file(file_hash, comment, incident_id, False)}
