import komand
from .schema import GetAlertsInput, GetAlertsOutput, Input, Output, Component
# Custom imports below
from komand.helper import clean


class GetAlerts(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_alerts',
                description=Component.DESCRIPTION,
                input=GetAlertsInput(),
                output=GetAlertsOutput())

    def run(self, params={}):
        start = params.get(Input.START)
        end = params.get(Input.END)

        alerts = clean([alert for alert in self.connection.client.alerts.list(start=start, end=end)])

        return {Output.ALERTS: alerts, Output.COUNT: len(alerts)}
