import insightconnect_plugin_runtime
from .schema import BlockUrlPolicyInput, BlockUrlPolicyOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import fmcapi
from urllib.parse import urlsplit


class BlockUrlPolicy(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="block_url_policy",
            description=Component.DESCRIPTION,
            input=BlockUrlPolicyInput(),
            output=BlockUrlPolicyOutput(),
        )

    def make_policy(self, fmc: fmcapi.FMC, policy_name: str):
        acp = fmcapi.AccessPolicies(fmc=fmc)
        acp.name = policy_name
        policy = acp.get()
        if "paging" in policy:
            if policy.get("paging", {}).get("count") == 0:
                policy = acp.post()
        self.logger.info(policy)
        return policy

    @staticmethod
    def _make_url_object(fmc: fmcapi.FMC, name: str, fqdn: str) -> str:
        url = fmcapi.URLs(fmc=fmc)
        url.name = name
        url.url = fqdn
        url.post()
        url.get()
        return url.id

    @staticmethod
    def _make_rule(fmc: fmcapi.FMC, policy: dict, rule_name: str, urls: dict) -> str:
        acr = fmcapi.AccessRules(fmc=fmc)
        acr.name = rule_name
        acr.urls = urls
        acr.acp_id = policy.get("id")
        acr.URL = policy.get("rules", {}).get("links", {}).get("self")
        acr.action = "BLOCK"
        acr.enabled = True
        acr.post()
        return acr.id

    def run(self, params={}):
        policy_name = params.get(Input.ACCESS_POLICY)
        rule_name = params.get(Input.RULE_NAME)

        with fmcapi.FMC(
            host=urlsplit(self.connection.host.strip()).netloc,
            username=self.connection.username,
            password=self.connection.password,
            autodeploy=True,
            limit=10,
            timeout=60,
        ) as fmc_from_api:
            urls = {"objects": []}
            for url_object in params.get(Input.URL_OBJECTS):
                url = url_object.get("url")
                url_object_name = url_object.get("name")
                if len(url) > 400:
                    raise PluginException(
                        cause="URL exceeds max length of 400.",
                        assistance="Please shorten the URL or try another.",
                    )

                url_id = self._make_url_object(fmc=fmc_from_api, name=url_object_name, fqdn=url)
                urls["objects"].append({"type": "URL", "id": url_id, "name": url_object_name})
            policy = self.make_policy(fmc=fmc_from_api, policy_name=policy_name)
            self._make_rule(fmc=fmc_from_api, policy=policy, rule_name=rule_name, urls=urls)

        return {Output.SUCCESS: True}
