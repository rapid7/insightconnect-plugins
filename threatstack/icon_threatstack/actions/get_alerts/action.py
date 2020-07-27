import insightconnect_plugin_runtime
from .schema import GetAlertsInput, GetAlertsOutput, Input, Output, Component
# Custom imports below
from insightconnect_plugin_runtime.helper import clean
from threatstack.errors import ThreatStackAPIError, ThreatStackClientError, APIRateLimitError
from insightconnect_plugin_runtime.exceptions import PluginException


class GetAlerts(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_alerts',
                description=Component.DESCRIPTION,
                input=GetAlertsInput(),
                output=GetAlertsOutput())

    def run(self, params={}):
        start = params.get(Input.START)
        end = params.get(Input.END)

        try:
            alerts = clean([alert for alert in self.connection.client.alerts.list(start=start, end=end)])
        except (ThreatStackAPIError, ThreatStackClientError, APIRateLimitError) as e:
            raise PluginException(cause="An error occurred!",
                                  assistance=e)

        return {Output.ALERTS: alerts, Output.COUNT: len(alerts)}
