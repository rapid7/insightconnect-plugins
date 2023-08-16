import insightconnect_plugin_runtime
from .schema import (
    EditAlertStatusInput,
    EditAlertStatusOutput,
    Input,
    Output,
    Component,
)
import json
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import pytmv1


class EditAlertStatus(insightconnect_plugin_runtime.Action):
    STATUS_MAPPING = {
        "New": pytmv1.InvestigationStatus.NEW,
        "In Progress": pytmv1.InvestigationStatus.IN_PROGRESS,
        "True Positive": pytmv1.InvestigationStatus.TRUE_POSITIVE,
        "False Positive": pytmv1.InvestigationStatus.FALSE_POSITIVE,
    }

    def __init__(self):
        super(self.__class__, self).__init__(
            name="edit_alert_status",
            description=Component.DESCRIPTION,
            input=EditAlertStatusInput(),
            output=EditAlertStatusOutput(),
        )

    def run(self, params={}):
        # Get Connection Client
        client = self.connection.client
        # Get Action Parameters
        alert_id = params.get(Input.ID)
        status = params.get(Input.STATUS)
        if_match = params.get(Input.IF_MATCH, None)
        # Choose enum
        status = self.STATUS_MAPPING.get(status)
        # Make Action API Call
        self.logger.info("Making API Call...")
        response = client.edit_alert_status(alert_id=alert_id, status=status, if_match=if_match)
        if "error" in response.result_code.lower():
            raise PluginException(
                cause="An error occurred while trying to edit the alert status.",
                assistance="Please check the provided parameters and try again.",
                data=response,
            )
        result_response = json.dumps(response.result_code).replace('"', "")
        # Return results
        self.logger.info("Returning Results...")
        return {Output.RESULT_CODE: result_response}
