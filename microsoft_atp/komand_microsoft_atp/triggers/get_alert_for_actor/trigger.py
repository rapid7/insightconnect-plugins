import komand
import time
from .schema import GetAlertForActorInput, GetAlertForActorOutput
# Custom imports below


class GetAlertForActor(komand.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_alert_for_actor',
                description='Get alerts by an actor',
                input=GetAlertForActorInput(),
                output=GetAlertForActorOutput())
        self.ACTOR = "Actor"

    def run(self, params={}):
        """Run the trigger"""
        while True:
            actor = params['actor']

            matching_alerts = self.connection.get_alerts_by_key_value(self.ACTOR, actor)
            if(len(matching_alerts) > 0):
                self.send({"results": matching_alerts})

            time.sleep(params.get("interval", 5))

    def test(self):
        # This will raise an exception for failure cases
        self.connection.test()

        # No exception raised, pass back json
        return {"results": self.connection.fake_alert()}
