import komand
from .schema import CheckIfHostInNetworkGroupInput, CheckIfHostInNetworkGroupOutput, Input, Output, Component
# Custom imports below


class CheckIfHostInNetworkGroup(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='check_if_host_in_network_group',
                description=Component.DESCRIPTION,
                input=CheckIfHostInNetworkGroupInput(),
                output=CheckIfHostInNetworkGroupOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
