import komand
from .schema import GetAlertInput, GetAlertOutput, Input, Output
# Custom imports below
from komand.helper import clean
from threatstack.errors import ThreatStackAPIError, ThreatStackClientError, APIRateLimitError
from komand.exceptions import PluginException


class GetAlert(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_alert',
                description='Get alert data by ID',
                input=GetAlertInput(),
                output=GetAlertOutput())

    def run(self, params={}):
        alert_id = params.get(Input.ALERT_ID)
        try:
            alert = clean(self.connection.client.alerts.get(alert_id))
        except (ThreatStackAPIError, ThreatStackClientError, APIRateLimitError) as e:
            raise PluginException(cause="An error occurred!",
                                  assistance=e)

        return {Output.ALERT: alert}
