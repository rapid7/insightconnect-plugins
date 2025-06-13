import insightconnect_plugin_runtime
from .schema import SearchAlertsInput, SearchAlertsOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean
from komand_rapid7_insightidr.util.endpoints import Alerts
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper
from komand_rapid7_insightidr.util.util import get_logging_context
from dateutil.relativedelta import relativedelta
import datetime
import json


class SearchAlerts(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="search_alerts",
            description=Component.DESCRIPTION,
            input=SearchAlertsInput(),
            output=SearchAlertsOutput(),
        )

    def run(self, params={}):  # noqa MC0001
        input_start_time = params.get(Input.START_TIME)
        input_end_time = params.get(Input.END_TIME)

        start_time = (
            datetime.datetime.fromisoformat(input_start_time)
            .astimezone(datetime.timezone.utc)
            .strftime("%Y-%m-%dT%H:%M:%SZ")
            if input_start_time
            else None
        )

        end_time = (
            datetime.datetime.fromisoformat(input_end_time)
            .astimezone(datetime.timezone.utc)
            .strftime("%Y-%m-%dT%H:%M:%SZ")
            if input_end_time
            else None
        )

        # if the user adds a start or end time we need to make sure there is both
        if start_time or end_time:
            if not start_time:
                raise PluginException(
                    cause="End time was provided but not start time, both are required for a valid timerange",
                    assistance="Please add in a start time",
                )
            elif not end_time:
                raise PluginException(
                    cause="Start time was provided but not end time, both are required for a valid timerange",
                    assistance="Please add in an end time",
                )
            elif datetime.datetime.fromisoformat(input_start_time) >= datetime.datetime.fromisoformat(input_end_time):
                raise PluginException(
                    cause="End time is greater than Start time",
                    assistance="Please adjust the start and endtime to have the endtime be after the start time",
                )
            elif not (
                (datetime.datetime.fromisoformat(input_end_time) - relativedelta(months=6))
                <= datetime.datetime.fromisoformat(input_start_time)
            ):
                raise PluginException(
                    cause="The maximum delta between start and endtime must be 6 months",
                    assistance="Please adjust the start and endtime to be within 6 months",
                )

        if not start_time and not end_time:
            start_time = (
                (datetime.datetime.now() - relativedelta(months=6))
                .astimezone(datetime.timezone.utc)
                .strftime("%Y-%m-%dT%H:%M:%SZ")
            )
            self.logger.info(
                f"No user supplied time, defaulting to start time of 6 months ago: {start_time}",
                **self.connection.log_values,
            )

        search = clean(
            {
                "start_time": start_time,
                "end_time": end_time,
                "leql": params.get(Input.LEQL),
                "terms": params.get(Input.TERMS),
            }
        )

        data = clean(
            {
                "search": search,
                "sorts": params.get(Input.SORTS),
                "field_ids": params.get(Input.FIELD_IDS),
                "aggregates": params.get(Input.AGGREGATES),
            }
        )

        parameters = clean(
            {"rrns_only": params.get(Input.RRNS_ONLY), "size": params.get(Input.SIZE), "index": params.get(Input.INDEX)}
        )

        self.connection.session.headers["Accept-version"] = "strong-force-preview "
        request = ResourceHelper(self.connection.session, self.logger)

        endpoint = Alerts.get_alert_serach(self.connection.url)
        response = request.resource_request(endpoint, "post", payload=data, params=parameters)

        try:
            result = json.loads(response.get("resource"))
        except json.decoder.JSONDecodeError:
            self.logger.error(f"InsightIDR response: {response}")
            raise PluginException(
                cause="The response from InsightIDR was not in the correct format.",
                assistance="Contact support for help. See log for more details",
            )

        try:
            if params.get(Input.RRNS_ONLY):
                rrns = clean(result.get("rrns", []))
                metadata = result.get("metadata", {})
                return {Output.RRNS: rrns, Output.METADATA: metadata}
            else:
                alerts = clean(result.get("alerts", []))
                metadata = result.get("metadata", {})
                return {Output.ALERTS: alerts, Output.METADATA: metadata}
        except KeyError:
            self.logger.error(result)
            raise PluginException(
                cause="The response from InsightIDR was not in the correct format.",
                assistance="Contact support for help. See log for more details",
            )
