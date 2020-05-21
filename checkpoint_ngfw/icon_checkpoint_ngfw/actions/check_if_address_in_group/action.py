import komand
from .schema import CheckIfAddressInGroupInput, CheckIfAddressInGroupOutput, Input, Output, Component
# Custom imports below
from icon_checkpoint_ngfw.util.utils import DetailsLevel
from typing import Optional


class CheckIfAddressInGroup(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='check_if_address_in_group',
                description=Component.DESCRIPTION,
                input=CheckIfAddressInGroupInput(),
                output=CheckIfAddressInGroupOutput())

    def run(self, params={}):
        address = params.get(Input.ADDRESS)
        group_input = params.get(Input.GROUP)

        host_names: {str} = self._aggregate_hosts(address=address, group_input=group_input)

        if len(host_names):
            return {Output.FOUND: True, Output.ADDRESS_OBJECTS: list(host_names)}
        else:
            return {Output.FOUND: False, Output.ADDRESS_OBJECTS: []}

    def _aggregate_hosts(self, address: str, group_input: Optional[str]) -> {str}:
        """
        Aggregate a list of hosts from network groups within a Check Point firewall instance
        :param address: Address to search for
        :param group_input: Group name, specified by the user. If not provided then all groups will be searched
        :return: Set of hosts found
        """

        # Holds groups with "full" information - the get_groups call below returns groups with minimal information
        full_groups: [dict] = []

        if group_input:
            full_groups.append(self.connection.get_group(name=group_input))
        else:
            groups = self._get_all_groups()

            for group in groups:
                full_groups.append(group)

        # Utilize a set to prevent duplicates
        host_names: {str} = set()
        for full_group in full_groups:
            host_name = self._check_group_for_address(group=full_group, address=address)
            if host_name:
                host_names.add(host_name)

        return host_names

    @staticmethod
    def _check_group_for_address(group: dict, address: str) -> Optional[str]:
        """
        Check a specified group for address membership
        :param group: Network group to check, as a dictionary
        :param address: Address to check for
        :return: Optional string indicating the name of the host
        """

        for member in group["members"]:
            if "ipv4-address" in member.keys() and member["ipv4-address"] == address:
                return member["name"]
            elif "ipv6-address" in member.keys() and member["ipv6-address"] == address:
                return member["name"]

        return None

    def _get_all_groups(self) -> [dict]:
        """
        Returns all network groups found within the Check Point instance
        :return: Network groups as a list of dictionaries
        """
        full_groups: [dict] = []

        limit = 500
        current_offset = 0

        while True:
            response = self.connection.get_groups(details_level=DetailsLevel.full, limit=limit, offset=current_offset)

            objects = response["objects"]
            if not objects:
                break

            for group in objects:
                self.logger.info(f"Getting hosts for group: {group['name']}")
                full_groups.append(self.connection.get_group(name=group["name"]))
            current_offset += limit

        return full_groups
