import komand
from .schema import GetMachineIdFromAlertIdInput, GetMachineIdFromAlertIdOutput
# Custom imports below


class GetMachineIdFromAlertId(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name="get_machine_id_from_alert_id",
                description="Retrieve the machine ID related to an alert",
                input=GetMachineIdFromAlertIdInput(),
                output=GetMachineIdFromAlertIdOutput())

    def run(self, params={}):
        self.logger.info("Running...")
        alert_id = params.get("alert_id")
        self.logger.info("Looking for alerts matching ID: " + alert_id)
        machines = self.connection.get_machines_from_alert_id(alert_id)
        return {"machine_information": komand.helper.clean(machines)}

    def test(self):
        self.connection.test()
        return {"machine_information": self.connection.fake_machine_info()}
