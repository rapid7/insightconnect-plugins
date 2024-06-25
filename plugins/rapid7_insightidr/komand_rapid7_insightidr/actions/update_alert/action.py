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
        tags = params.get(Input.TAGS)
        # END INPUT BINDING - DO NOT REMOVE

        data = clean(
            {
                "status": {"value": status},
                "disposition": {"value": disposition},
                "priority": {"value": priority},
                "assignee_id": {"value": assignee_id},
                "investigation_rrn": {"value": investigation_rrn},
                "tags": tags,
                "comment": comment,
            }
        )

        self.connection.session.headers["Accept-version"] = "strong-force-preview"
        request = ResourceHelper(self.connection.session, self.logger)

        endpoint = Alerts.get_alert_information(self.connection.url, alert_rrn)
        response = request.resource_request(endpoint, "patch", payload=data)

        try:
            result = json.loads(response.get("resource"))
        except json.decoder.JSONDecodeError:
            self.logger.error(f"InsightIDR response: {response}")
            raise PluginException(
                cause="The response from InsightIDR was not in the correct format.",
                assistance="Contact support for help. See log for more details",
            )
        try:
            return {Output.ALERT: clean(result)}
        except KeyError:
            self.logger.error(result)
            raise PluginException(
                cause="The response from InsightIDR was not in the correct format.",
                assistance="Contact support for help. See log for more details",
            )
