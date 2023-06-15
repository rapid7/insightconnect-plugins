import insightconnect_plugin_runtime
from .schema import AddAlertNoteInput, AddAlertNoteOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below


class AddAlertNote(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_alert_note",
            description=Component.DESCRIPTION,
            input=AddAlertNoteInput(),
            output=AddAlertNoteOutput(),
        )

    def run(self, params={}):
        # Get Connection Client
        client = self.connection.client
        # Get Action Parameters
        alert_id = params.get(Input.ALERT_ID)
        content = params.get(Input.CONTENT)
        # Make Action API Call
        self.logger.info("Making API Call...")
        response = client.add_alert_note(alert_id=alert_id, note=content)
        if "error" in response.result_code.lower():
            raise PluginException(
                cause="An error occurred while adding an alert note.",
                assistance="Please check the provided alert ID and content.",
                data=response.error,
            )
        self.logger.info("Returning Results...")
        location = response.response.location
        note_id = location.split("/")[-1]
        result_code = response.result_code
        return {
            Output.RESULT_CODE: result_code,
            Output.LOCATION: location,
            Output.NOTE_ID: note_id,
        }
