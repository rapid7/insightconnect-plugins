import insightconnect_plugin_runtime
from .schema import SearchCertstreamInput, SearchCertstreamOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
import certstream
import re
import Levenshtein
from komand_typo_squatter.util import utils


class SearchCertstream(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="search_certstream",
            description=Component.DESCRIPTION,
            input=SearchCertstreamInput(),
            output=SearchCertstreamOutput(),
        )
        self.domain = ""
        self.query = ""
        self.levenshtein = 0

    def callback(self, message, context):  # pylint: disable=unused-argument
        """Callback handler for certstream events."""
        message_type = message.get("message_type")
        if message_type == "heartbeat":
            return

        if message_type == "certificate_update":
            all_domains = message.get("data", {}).get("leaf_cert", {}).get("all_domains", [])

            for domain in all_domains:
                score = utils.score_domain(domain.lower())

                # If issued from a free CA = more suspicious
                issued = message.get("data", {}).get("leaf_cert", {}).get("issuer", {}).get("O")
                if issued:
                    if "Let's Encrypt" in issued:
                        score += 10
                if self.query:
                    if not re.search(self.query, domain):
                        continue
                else:
                    if Levenshtein.distance(str(self.domain), str(domain)) > self.levenshtein:
                        continue
                self.send({Output.DOMAIN: domain, Output.SCORE: score})
        else:
            raise PluginException(
                cause="An unrecognized message type was returned.", assistance="Please contact support."
            )

    def run(self, params={}):
        """Run the trigger"""
        self.query = params.get(Input.QUERY)
        self.levenshtein = params.get(Input.LEVENSHTEIN)
        self.domain = params.get(Input.DOMAIN)
        certstream.listen_for_events(self.callback, "wss://certstream.calidog.io")
