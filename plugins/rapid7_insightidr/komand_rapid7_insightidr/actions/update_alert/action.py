import insightconnect_plugin_runtime
from .schema import UpdateAlertInput, UpdateAlertOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean
from komand_rapid7_insightidr.util.endpoints import Alerts
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper
import json


class UpdateAlert(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_alert", description=Component.DESCRIPTION, input=UpdateAlertInput(), output=UpdateAlertOutput()
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        alert_rrn = params.get(Input.ALERT_RRN)
        assignee_id = params.get(Input.ASSIGNEE_ID)
        comment = params.get(Input.COMMENT)
        disposition = params.get(Input.DISPOSITION)
        investigation_rrn = params.get(Input.INVESTIGATION_RRN)
        priority = params.get(Input.PRIORITY)
        status = params.get(Input.STATUS)
        # END INPUT BINDING - DO NOT REMOVE

        # Create a dictionary with the parameters
        data = clean(
            {
                "status": {"value": status},
                "disposition": {"value": disposition},
                "priority": {"value": priority},
                "assignee_id": {"value": assignee_id},
                "investigation_rrn": {"value": investigation_rrn},
                "comment": comment,
            }
        )

        # Remove keys with empty values to ensure only populated fields are sent in the request
        data = {k: v for k, v in data.items() if v and (isinstance(v, dict) and v["value"] or not isinstance(v, dict))}

        # Set the API version header and create a request helper instance
        self.connection.headers["Accept-version"] = "strong-force-preview"
        request = ResourceHelper(self.connection.headers, self.logger)

        # Construct the endpoint URL
        endpoint = Alerts.get_alert_information(self.connection.url, alert_rrn)

        # Send the PATCH request to the API endpoint with the cleaned data
        response = request.resource_request(endpoint, "patch", payload=data)

        try:
            # Attempt to parse the response JSON
            result = json.loads(response.get("resource"))
        except json.decoder.JSONDecodeError:
            # Log the error and raise an exception if the response is not valid JSON
            self.logger.error(f"InsightIDR response: {response}")
            raise PluginException(
                cause="The response from InsightIDR was not in the correct format.",
                assistance="Contact support for help. See log for more details",
            )
        try:
            # Return the cleaned result
            return {Output.ALERT: clean(result)}
        except KeyError:
            # Log the error and raise an exception if the expected key is not in the result
            self.logger.error(result)
            raise PluginException(
                cause="The response from InsightIDR was not in the correct format.",
                assistance="Contact support for help. See log for more details",
            )
