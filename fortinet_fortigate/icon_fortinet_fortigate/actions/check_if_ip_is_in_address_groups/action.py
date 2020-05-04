import komand
from .schema import CheckIfIpIsInAddressGroupsInput, CheckIfIpIsInAddressGroupsOutput, Input, Output, Component
# Custom imports below


class CheckIfIpIsInAddressGroups(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='check_if_ip_is_in_address_groups',
                description=Component.DESCRIPTION,
                input=CheckIfIpIsInAddressGroupsInput(),
                output=CheckIfIpIsInAddressGroupsOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
