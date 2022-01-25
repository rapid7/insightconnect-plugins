import komand
from .schema import QuarantineHostInput, QuarantineHostOutput, Input, Output, Component

# Custom imports below


class QuarantineHost(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="quarantine_host",
            description=Component.DESCRIPTION,
            input=QuarantineHostInput(),
            output=QuarantineHostOutput(),
        )

    def run(self, params={}):
        # TODO: Implement run function
        return {}
