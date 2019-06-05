import komand
import time
from .schema import GetAlertForDomainInput, GetAlertForDomainOutput
# Custom imports below


class GetAlertForDomain(komand.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_alert_for_domain',
                description='Get alerts by Domain',
                input=GetAlertForDomainInput(),
                output=GetAlertForDomainOutput())
        self.MACHINE_DOMAIN = "MachineDomain"

    def run(self, params={}):
        """Run the trigger"""
        while True:
            domain = params['domain']

            matching_alerts = self.connection.get_alerts_by_key_value(self.MACHINE_DOMAIN, domain)

            if(len(matching_alerts) > 0):
                self.send({"results": matching_alerts})

            time.sleep(params.get("interval", 5))

    def test(self):
        # This will raise an exception for failure cases
        self.connection.test()

        # No exception raised, pass back json
        return {"results": self.connection.fake_alert()}
