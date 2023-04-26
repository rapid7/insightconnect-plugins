import insightconnect_plugin_runtime
from .schema import AddAlertNoteInput, AddAlertNoteOutput, Input, Output, Component

# Custom imports below
import pytmv1


class AddAlertNote(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_alert_note",
            description=Component.DESCRIPTION,
            input=AddAlertNoteInput(),
            output=AddAlertNoteOutput(),
        )

    def run(self, params={}):
        # Get Connection Parameters
        url = self.connection.server
        token = self.connection.token_
        app = self.connection.app
        # Get Action Parameters
        alert_id = params.get(Input.ALERT_ID)
        content = params.get(Input.CONTENT)
        # Initialize PYTMV1 Client
        self.logger.info("Initializing PYTMV1 Client...")
        client = pytmv1.client(app, token, url)
        # Make Action API Call
        self.logger.info("Making API Call...")
        response = client.add_alert_note(alert_id=alert_id, note=content)
        if "error" in response.result_code.lower():
            return response.error
        else:
            self.logger.info("Returning Results...")
            location = response.response.location
            note_id = location.split("/")[-1]
            result_code = response.result_code
            return {"result_code": result_code, "location": location, "note_id": note_id}
