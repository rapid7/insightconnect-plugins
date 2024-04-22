import re

import insightconnect_plugin_runtime
import validators
from insightconnect_plugin_runtime.exceptions import PluginException

from komand_dig.util import util
from komand_dig.util.constants import Message

from .schema import Component, Input, Output, ReverseInput, ReverseOutput


class Reverse(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="reverse",
            description=Component.DESCRIPTION,
            input=ReverseInput(),
            output=ReverseOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        resolver = params.get(Input.RESOLVER, "")
        ip_address = params.get(Input.ADDRESS, "")
        # END INPUT BINDING - DO NOT REMOVE

        # Validate user inputs
        if not validators.ipv4(ip_address):
            raise PluginException(
                cause=Message.INVALID_IP_ADDRESS_CAUSE.format("Address"),
                assistance=Message.INVALID_IP_ADDRESS_ASSISTANCE,
            )
        elif resolver and not validators.ipv4(resolver):
            raise PluginException(
                cause=Message.INVALID_IP_ADDRESS_CAUSE.format("Resolver"),
                assistance=Message.INVALID_IP_ADDRESS_ASSISTANCE,
            )

        command = f"-x {ip_address}"
        if resolver:
            command = f"@{resolver} " + command

        command_output = util.execute_command(self.logger, command, "ANSWER SECTION:\n(.*\n)")
        answer_section = command_output.get("answer_section")

        # Get the answer section
        if answer_section is None:
            address = "Not found"
        else:
            # Grab address
            address = util.safe_parse(re.search(r"\s(\S+)\n", answer_section))
            if util.not_empty(address):
                address = address.rstrip(".")

        return {
            Output.FULLOUTPUT: command_output.get("full_output", ""),
            Output.NAMESERVER: command_output.get("nameserver", ""),
            Output.STATUS: command_output.get("status", ""),
            Output.QUESTION: ip_address,
            Output.ANSWER: address,
        }
