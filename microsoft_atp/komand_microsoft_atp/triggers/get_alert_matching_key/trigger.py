import komand
import time
from .schema import GetAlertMatchingKeyInput, GetAlertMatchingKeyOutput
# Custom imports below


class GetAlertMatchingKey(komand.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_alert_matching_key',
                description='Get alerts that match a given key to its value',
                input=GetAlertMatchingKeyInput(),
                output=GetAlertMatchingKeyOutput())

    def run(self, params={}):
        """Run the trigger"""
        while True:
            key = params["key"]
            value = params["value"]

            matching_alerts = self.connection.get_alerts_by_key_value(key, value)

            if(len(matching_alerts) > 0):
                self.send({"results": matching_alerts})

            time.sleep(params.get("interval", 5))

    def test(self):
        # This will raise an exception for failure cases
        self.connection.test()

        # No exception raised, pass back json
        return {"results": self.connection.fake_alert()}
