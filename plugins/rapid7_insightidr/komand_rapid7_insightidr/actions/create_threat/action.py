import insightconnect_plugin_runtime
from .schema import CreateThreatInput, CreateThreatOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import validators
from komand_rapid7_insightidr.util.endpoints import Threats
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper
import json


class CreateThreat(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_threat",
            description=Component.DESCRIPTION,
            input=CreateThreatInput(),
            output=CreateThreatOutput(),
        )

    def run(self, params={}):
        self.connection.headers["Accept-version"] = "investigations-preview"
        request = ResourceHelper(self.connection.headers, self.logger)
        endpoint = Threats.create_threat(self.connection.url)

        indicators = params.get(Input.INDICATORS)
        note_text = params.get(Input.NOTE_TEXT)
        if not note_text:
            note_text = "Threat created via InsightConnect"

        ip_indicator = []
        url_indicator = []
        domain_indicator = []
        hash_indicator = []

        for indicator in indicators:
            if validators.ipv4(indicator):
                ip_indicator.append(indicator)
            elif validators.domain(indicator):
                domain_indicator.append(indicator)
            elif validators.url(indicator):
                url_indicator.append(indicator)
            elif validators.sha1(indicator) or validators.md5(indicator) or validators.sha256(indicator):
                hash_indicator.append(indicator)
            else:
                self.logger.info(
                    f"Given indicator: '{indicator}' is not in correct type and will not be added "
                    "to this new threat."
                )

        response = request.resource_request(
            endpoint,
            "post",
            params={"format": "json"},
            payload={
                "threat": params.get(Input.THREAT_NAME),
                "note": note_text,
                "indicators": {
                    "ips": ip_indicator,
                    "hashes": hash_indicator,
                    "domain_names": domain_indicator,
                    "urls": url_indicator,
                },
            },
        )
        try:
            result = json.loads(response["resource"])
        except (json.decoder.JSONDecodeError, IndexError, KeyError):
            raise PluginException(
                cause="The response from InsightIDR was not in the correct format.",
                assistance="Contact support for help. See log for more details",
                data=response,
            )

        return {
            Output.REJECTED_INDICATORS: result["rejected_indicators"],
            Output.THREAT: result["threat"],
        }
