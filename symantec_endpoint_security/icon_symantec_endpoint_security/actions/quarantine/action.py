import insightconnect_plugin_runtime
from .schema import QuarantineInput, QuarantineOutput, Input, Output, Component
# Custom imports below
from icon_symantec_endpoint_security.util.api import APIException
import re
from insightconnect_plugin_runtime.exceptions import PluginException


class Quarantine(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='quarantine',
                description=Component.DESCRIPTION,
                input=QuarantineInput(),
                output=QuarantineOutput())

    def run(self, params={}):
        agent_identifier = params.get(Input.AGENT)
        whitelist = params.get(Input.WHITELIST, [])
        quarantine_state = params.get(Input.QUARANTINE_STATE)

        # Normalize the whitelist
        whitelist_normalized = set(map(self._normalize_mac_address, whitelist))

        # Hostnames cannot be used to quarantine, but MAC addresses can. If a hostname is passed
        # then we need to do an additional lookup to get the unique ID to use.
        # If a MAC address is passed then we can go ahead and use that directly after normalizing it
        if not self._is_mac_address(agent_identifier=agent_identifier):
            full_details = self.connection.api_client.get_computer(computer_name=agent_identifier)
            mac_addresses = set(full_details.get("macAddresses", []))

            in_whitelist = len(whitelist_normalized.intersection(mac_addresses)) > 0
            hardware_identifier = mac_addresses.pop()
        else:
            hardware_identifier = self._normalize_mac_address(mac_address=agent_identifier)
            in_whitelist = hardware_identifier in whitelist_normalized

        if in_whitelist:
            self.logger.info(f"The agent specified '{agent_identifier}' was found within the whitelist and "
                             f"will be skipped!")
            return {Output.SUCCESS: False, Output.WHITELISTED: True}

        self.logger.info(f"{'Quarantining' if quarantine_state else 'Unquarantining'} the "
                         f"following agent: {agent_identifier}")

        try:
            self.connection.api_client.update_quarantine_status(hardware_ids=[hardware_identifier],
                                                                quarantine=quarantine_state)
        except APIException as e:
            raise PluginException(cause=f"An error occurred while attempting to "
                                        f"{'quarantine' if quarantine_state else 'unquarantine'} the agent!",
                                  assistance=e.message)

        return {Output.SUCCESS: True}

    @staticmethod
    def _is_mac_address(agent_identifier: str) -> bool:
        """
        Determines whether or not an agent identifier is a MAC address or hostname
        :param agent_identifier: Agent identifier input from the user
        :return: Boolean indicating if the agent identifier given was a MAC address (true)
        """
        r = r"([a-fA-F0-9]{2}[-:]){5}[a-zA-Z0-9]{2}"
        matches = re.match(r, agent_identifier)

        if matches:
            return True

        return False

    @staticmethod
    def _normalize_mac_address(mac_address: str) -> str:
        """
        Normalizes MAC addresses for input into the SEPM API
        :param mac_address: MAC address to normalize
        :return: Normalized MAC address
        """

        return mac_address.upper().replace(":", "-")
