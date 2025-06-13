import insightconnect_plugin_runtime
from .schema import CloseInvestigationsInBulkInput, CloseInvestigationsInBulkOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
from komand_rapid7_insightidr.util.endpoints import Investigations
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper
from komand_rapid7_insightidr.util.util import get_logging_context
import json
from datetime import datetime
from datetime import timedelta


class CloseInvestigationsInBulk(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="close_investigations_in_bulk",
            description=Component.DESCRIPTION,
            input=CloseInvestigationsInBulkInput(),
            output=CloseInvestigationsInBulkOutput(),
        )

    def run(self, params={}):
        self.connection.session.headers["Accept-version"] = "investigations-preview"
        request = ResourceHelper(self.connection.session, self.logger)
        endpoint = Investigations.close_investigations_in_bulk(self.connection.url)

        source = self._get_with_default(params, Input.SOURCE, "MANUAL")
        max_investigations_to_close = self._get_with_default(params, Input.MAX_INVESTIGATIONS_TO_CLOSE, None)
        alert_type = self._get_with_default(params, Input.ALERT_TYPE, None)

        timestamp_from = params.get(Input.DATETIME_FROM)
        if not timestamp_from:
            timestamp_from = (datetime.now() - timedelta(days=7)).replace(microsecond=0).isoformat()
            timestamp_from = f"{timestamp_from}Z"

        timestamp_to = params.get(Input.DATETIME_TO)
        if not timestamp_to:
            timestamp_to = datetime.now().replace(microsecond=0).isoformat()
            timestamp_to = f"{timestamp_to}Z"

        response = request.resource_request(
            endpoint,
            "post",
            payload={
                "alert_type": alert_type,
                "from": timestamp_from,
                "max_investigations_to_close": max_investigations_to_close,
                "source": source,
                "to": timestamp_to,
            },
        )

        try:
            result = json.loads(response.get("resource", "{}"))
        except json.decoder.JSONDecodeError:
            self.logger.error(f"InsightIDR response: {response}", **self.connection.cloud_log_values)
            raise PluginException(
                cause="The response from InsightIDR was not in the expected format.",
                assistance="Contact support for help. See log for more details:",
                data=response,
            )

        return {Output.IDS: result.get("ids", []), Output.NUM_CLOSED: result.get("num_closed", 0)}

    @staticmethod
    def _get_with_default(dictionary, key, def_value):
        value = dictionary.get(key, def_value)
        if not value:
            return def_value

        return value
