import komand
from .schema import CheckIfAddressInGroupInput, CheckIfAddressInGroupOutput, Input, Output, Component
# Custom imports below


class CheckIfAddressInGroup(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='check_if_address_in_group',
                description=Component.DESCRIPTION,
                input=CheckIfAddressInGroupInput(),
                output=CheckIfAddressInGroupOutput())

    def run(self, params={}):
        address = params.get(Input.ADDRESS)
        enable_search = params.get(Input.ENABLE_SEARCH)
        group = params.get(Input.GROUP)
        discard_other_sessions = params.get(Input.DISCARD_OTHER_SESSIONS)

        headers = self.connection.get_headers()
        url = f"{self.connection.server_and_port}/web_api/add-host"

        group = self.connection.get_group(name=group)
        found = False
        for member in group["members"]:
            if "ipv4-address" in member.keys() and member["ipv4-address"] == address:
                found = True
            elif "ipv6-address" in member.keys() and member["ipv6-address"] == address:
                found = True
            else:
                self.logger.warn(f"Member from group returned without IPv4 or IPv6 address: {member['name']}")

        self.logger.info(f"GROUP IS: {group}")

        # payload = {
        #
        # }
        #
        # self.connection.post_and_publish(headers, discard_other_sessions, payload, url)

        return {}
