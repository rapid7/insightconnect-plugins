import komand
from .schema import LookupAlertInput, LookupAlertOutput, Input, Output, Component
# Custom imports below



class LookupAlert(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='lookup_alert',
                description=Component.DESCRIPTION,
                input=LookupAlertInput(),
                output=LookupAlertOutput())

    def run(self, params={}):
        alert_id = params.get(Input.ALERT_ID)
        alert = self.connection.client.lookup_alert(alert_id)
        return {Output.ALERT: komand.helper.clean(alert.get("data"))}

