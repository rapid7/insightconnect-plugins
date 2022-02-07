import insightconnect_plugin_runtime
from .schema import GetCompleteAlertByIdInput, GetCompleteAlertByIdOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.helper import clean


class GetCompleteAlertById(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_complete_alert_by_id",
            description=Component.DESCRIPTION,
            input=GetCompleteAlertByIdInput(),
            output=GetCompleteAlertByIdOutput(),
        )

    def run(self, params={}):
        response = self.connection.client.get_complete_alert_by_id(params.get(Input.ALERT_ID))
        return clean(
            {
                Output.ID: response.get("_id"),
                Output.ASSETS: response.get("Assets", []),
                Output.ASSIGNEES: response.get("Assignees", []),
                Output.DETAILS: response.get("Details", {}),
                Output.FOUND_DATE: response.get("FoundDate"),
                Output.UPDATE_DATE: response.get("UpdateDate"),
                Output.TAKEDOWN_STATUS: response.get("TakedownStatus"),
                Output.IS_CLOSED: response.get("IsClosed", False),
                Output.IS_FLAGGED: response.get("IsFlagged", False),
                Output.LEAK_NAME: response.get("LeakName"),
            }
        )
