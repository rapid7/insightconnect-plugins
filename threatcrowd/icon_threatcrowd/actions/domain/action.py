import insightconnect_plugin_runtime
from .schema import DomainInput, DomainOutput, Input, Output, Component

# Custom imports below


class Domain(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="domain", description=Component.DESCRIPTION, input=DomainInput(), output=DomainOutput()
        )

    def run(self, params={}):
        data = self.connection.client.search_domain(self._url_check(params.get(Input.DOMAIN)))

        if not data or int(data["response_code"]) == 0:
            self.logger.info("Run: ThreatCrowd API did not return any matches.")
            return {Output.FOUND: False}

        return {
            Output.DOMAINS: insightconnect_plugin_runtime.helper.clean_list(data["resolutions"]),
            Output.EMAILS: insightconnect_plugin_runtime.helper.clean_list(data["emails"]),
            Output.HASHES: insightconnect_plugin_runtime.helper.clean_list(data["hashes"]),
            Output.MALICIOUS: self.connection.client.verdict(data["votes"]),
            Output.PERMALINK: data["permalink"],
            Output.REFERENCES: insightconnect_plugin_runtime.helper.clean_list(data["references"]),
            Output.SUBDOMAINS: insightconnect_plugin_runtime.helper.clean_list(data["subdomains"]),
            Output.FOUND: True,
        }

    @staticmethod
    def _url_check(url):
        if url.startswith("http://"):
            url = url.replace("http://", "").split("/")[0]
            return url
        if url.startswith("https://"):
            url = url.replace("https://", "").split("/")[0]
            return url
        url = url.split("/")[0]
        return url
