import insightconnect_plugin_runtime
from .schema import CheckForSquattersInput, CheckForSquattersOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_typo_squatter.util import utils
import subprocess  # nosec B404
import validators
import json
from typing import List, Dict, Any


class CheckForSquatters(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="check_for_squatters",
            description=Component.DESCRIPTION,
            input=CheckForSquattersInput(),
            output=CheckForSquattersOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        domain = params.get(Input.DOMAIN)
        flag = params.get(Input.FLAG, "")
        # END INPUT BINDING - DO NOT REMOVE

        return {Output.POTENTIAL_SQUATTERS: self.check_for_squatters(domain, flag)}

    def check_for_squatters(self, domain: str, flag: str) -> List[Dict[str, Any]]:
        if not validators.domain(domain):
            raise PluginException(
                cause="Invalid domain provided.", assistance="Please provide a valid domain and try again."
            )
        cmd = f"dnstwist {flag} -f json {domain}" if flag else f"dnstwist -f json {domain}"
        self.logger.info(f"Running command: {cmd}")
        results = subprocess.run(  # nosec B603
            cmd.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True
        )
        error = results.stderr.decode()
        if error:
            if "unrecognized arguments" in error:
                raise PluginException(
                    cause="Invalid flag provided.", assistance="Please provide a valid flag and try again.", data=error
                )
            raise PluginException(
                cause=f"An error occurred while executing the command: {cmd}.",
                assistance="Please try again and contact support if the problem persists.",
                data=error,
            )
        json_output = json.loads(results.stdout.decode().replace("\\n", ""))
        for index, item in enumerate(json_output):
            json_output[index]["phishing_score"] = utils.score_domain(item.get("domain"))
        return json_output
