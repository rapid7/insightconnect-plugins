import re

import insightconnect_plugin_runtime
import validators
from insightconnect_plugin_runtime.exceptions import PluginException

from komand_dig.util import util
from komand_dig.util.constants import Message

from .schema import Component, ForwardInput, ForwardOutput, Input, Output


class Forward(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="forward",
            description=Component.DESCRIPTION,
            input=ForwardInput(),
            output=ForwardOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        resolver = params.get(Input.RESOLVER, "")
        domain = params.get(Input.DOMAIN, "")
        query = params.get(Input.QUERY, "")
        # END INPUT BINDING - DO NOT REMOVE

        # Validate user inputs
        if resolver and not validators.ipv4(resolver):
            raise PluginException(
                cause=Message.INVALID_IP_ADDRESS_CAUSE.format("Resolver"),
                assistance=Message.INVALID_IP_ADDRESS_ASSISTANCE,
            )
        elif not validators.domain(domain):
            raise PluginException(cause=Message.INVALID_DOMAIN_CAUSE, assistance=Message.INVALID_DOMAIN_ASSISTANCE)

        arguments = [domain, query]
        if resolver:
            arguments.insert(0, f"@{resolver}")
        command = " ".join(arguments)

        command_output = util.execute_command(self.logger, command, r"ANSWER SECTION:\n(.*)\n\n;;", re.DOTALL)
        answer_section = command_output.get("answer_section")

        if answer_section is None:
            answers = ["Not found"]
        else:
            # Grab address
            if query == "SOA":
                domain = util.safe_parse(re.search(r"SOA\t(\S+)", answer_section))
                if util.not_empty(domain):
                    domain = domain.rstrip(".")
                answers = [domain]
            else:
                answers = answer_section.split("\n")
                if len(answers) == 0:
                    answers.append("NO MATCHES FOUND")
                answers = [util.safe_parse(re.search(r"\s(\S+)$", answer)) for answer in answers]
                answers = [answer.rstrip(".") for answer in answers]

        return {
            Output.FULLOUTPUT: command_output.get("full_output", ""),
            Output.NAMESERVER: command_output.get("nameserver", ""),
            Output.STATUS: command_output.get("status", ""),
            Output.QUESTION: domain,
            Output.ANSWER: answers[0],
            Output.LAST_ANSWER: answers[-1],
            Output.ALL_ANSWERS: answers,
        }
