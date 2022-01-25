import komand
from .schema import CheckHostQuarantineStatusInput, CheckHostQuarantineStatusOutput, Input, Output, Component

# Custom imports below


class CheckHostQuarantineStatus(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="check_host_quarantine_status",
            description=Component.DESCRIPTION,
            input=CheckHostQuarantineStatusInput(),
            output=CheckHostQuarantineStatusOutput(),
        )

    def run(self, params={}):
        # TODO: Implement run function
        return {}
