import komand
import time
from .schema import GetAlertForIdInput, GetAlertForIdOutput
# Custom imports below


class GetAlertForId(komand.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_alert_for_id',
                description='Get alerts by ID',
                input=GetAlertForIdInput(),
                output=GetAlertForIdOutput())
        self.ALERT_ID = "AlertId"

    def run(self, params={}):
        """Run the trigger"""
        while True:
            alert_id = params["id"]

            matching_alerts = self.connection.get_alerts_by_key_value(self.ALERT_ID, alert_id)
            if(len(matching_alerts) > 0):
                self.send({"results": matching_alerts})  # Return here

            time.sleep(params.get("interval", 5))

    def test(self):
        # This will raise an exception for failure cases
        self.connection.test()

        # No exception raised, pass back json
        return {"results": self.connection.fake_alert()}
