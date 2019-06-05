import komand
import time
from .schema import GetAlertForFileInput, GetAlertForFileOutput
# Custom imports below


class GetAlertForFile(komand.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_alert_for_file',
                description='Get alerts by File Name',
                input=GetAlertForFileInput(),
                output=GetAlertForFileOutput())
        self.FILE_NAME = "FileName"

    def run(self, params={}):
        """Run the trigger"""
        while True:
            filename = params['filename']

            matching_alerts = self.connection.get_alerts_by_key_value(self.FILE_NAME, filename)

            if(len(matching_alerts) > 0):
                self.send({"results": matching_alerts})

            time.sleep(params.get("interval", 5))

    def test(self):
        # This will raise an exception for failure cases
        self.connection.test()

        # No exception raised, pass back json
        return {"results": self.connection.fake_alert()}
