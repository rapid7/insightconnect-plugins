import komand
from .schema import AlertInput, AlertOutput
# Custom imports below
import time
from functools import reduce


class Alert(komand.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='alert',
                description='Hook a configured alert to send data to Komand',
                input=AlertInput(),
                output=AlertOutput())

    def run(self, params={}):
        interval = params.get('interval', 15)
        alerts = params.get("names")  # List of saved search names

        saved_searches = map(lambda alert: self.connection.client.saved_searches[alert], alerts)

        for saved_search in saved_searches:
            self.logger.info("Registering webhook: %s" % self.webhook_url)

            actions = saved_search['actions']

            if actions is None:
                self.logger.info("No actions found, skipping")
            else:  # Actions exist
                self.logger.info("Actions are: %s" % actions)

                if "webhook" not in actions:
                    if not actions:
                        actions = "webhook"
                    else:
                        actions += ",webhook"

                result = saved_search.update(**{
                    "actions": actions,
                    "action.webhook": 1,
                    "action.webhook.param.url": self.webhook_url
                })

                self.logger.info("Results: %s" % result)

        while True:  # Sleep indefinitely since the webhooks have been registered
            time.sleep(interval)

    def test(self, params={}):
        try:
            alerts = map(lambda name: self.connection.client.saved_searches[name], params['names'])
            self.logger.info("Got alerts: %s",
                             reduce(lambda a1, a2: str(a1)
                                    + (", " if a2 is not None else "") + str(a2), alerts))
        except Exception:
            self.logger.error("The Splunk connection or alert name was not valid")
            raise

        return {}
