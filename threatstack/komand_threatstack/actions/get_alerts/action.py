import komand
from .schema import GetAlertsInput, GetAlertsOutput
# Custom imports below


class GetAlerts(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_alerts',
                description='Get alerts by filter',
                input=GetAlertsInput(),
                output=GetAlertsOutput())

    def run(self, params={}):
        alerts = self.connection.client.alerts.list(**params)
        alert_list = []

        while True:
            try:
                alert = next(alerts)
                alert_list.append(alert)
            except TypeError:
                # Nothing found.
                # Not necessarily an error; could be failed search.
                break
            except StopIteration:
                break

        return {'alerts': alert_list, 'count': len(alert_list)}
