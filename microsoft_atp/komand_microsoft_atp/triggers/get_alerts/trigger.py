import komand
import time
from .schema import GetAlertsInput, GetAlertsOutput
# Custom imports below


class GetAlerts(komand.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_alerts',
                description='Return all new alerts',
                input=GetAlertsInput(),
                output=GetAlertsOutput())

    def run(self, params={}):
        """Run the trigger"""

        frequency = params.get("frequency", 5)

        while True:
            all_results = self.connection.get_all_alerts()

            if(len(all_results) > 0):
                self.send({"results": all_results})

            time.sleep(frequency)
