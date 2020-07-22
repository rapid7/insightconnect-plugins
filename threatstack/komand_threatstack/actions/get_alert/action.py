import komand
from .schema import GetAlertInput, GetAlertOutput
# Custom imports below


class GetAlert(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_alert',
                description='Get alert data by ID',
                input=GetAlertInput(),
                output=GetAlertOutput())

    def run(self, params={}):
        alert = self.connection.client.alerts.get(params.get('alert_id'))
        return {'alert': alert}
