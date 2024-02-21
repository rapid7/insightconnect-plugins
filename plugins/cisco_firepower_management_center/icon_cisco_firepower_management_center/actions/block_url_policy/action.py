import insightconnect_plugin_runtime
from .schema import BlockUrlPolicyInput, BlockUrlPolicyOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException
from typing import Union

# Custom imports below


class BlockUrlPolicy(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="block_url_policy",
            description=Component.DESCRIPTION,
            input=BlockUrlPolicyInput(),
            output=BlockUrlPolicyOutput(),
        )

    def get_policy_object(self, policy_name: str) -> Union[dict, None]:
        """

        :param policy_name:
        :return:
        """

        policies = self.connection.cisco_firepower_api.get_policies()
        # If get AND found, return whole individual policy object
        for policy in policies.get("items", []):
            if policy.get("name") == policy_name:
                return self.connection.cisco_firepower_api.get_policies(policy.get("id", ""))
        return None

    def make_policy(self, policy_name: str) -> dict:
        """

        :param policy_name:
        :return:
        """

        policy_obj = self.get_policy_object(policy_name)

        if policy_obj is None:
            self.logger.info(f"No policy found, creating new policy: {policy_name}")
            return self.connection.cisco_firepower_api.post_policy(
                {"name": policy_name, "type": "AccessPolicy", "defaultAction": {"action": "BLOCK"}}
            )
        else:
            self.logger.info(f"Found policy returned for: {policy_name}")
            return policy_obj

    def make_url_object(self, name: str, url: str) -> str:
        """

        :param name:
        :param url:
        :return:
        """
        payload = {"name": name, "url": url}
        self.connection.cisco_firepower_api.post_urls(payload)

        response = self.connection.cisco_firepower_api.get_urls()
        url_list = response.get("items")

        for item in url_list:
            if item.get("name") == name:
                return item.get("id")

    def make_rule(self, policy: dict, rule_name: str, urls: dict) -> None:
        """

        :param policy:
        :param rule_name:
        :param urls:
        :return:
        """
        payload = {
            "name": rule_name,
            "urls": urls,
            "action": "BLOCK",
            "enabled": True,
        }
        url = policy.get("rules", {}).get("links", {}).get("self")
        url_split = url.split("/")
        url_join = "/".join(url_split[4:])

        self.connection.cisco_firepower_api.post_rule(path=url_join, payload=payload)

    def run(self, params={}):
        policy_name = params.get(Input.ACCESS_POLICY)
        rule_name = params.get(Input.RULE_NAME)

        urls = {"objects": []}
        self.logger.info("Posting URLS")
        for url_object in params.get(Input.URL_OBJECTS):
            url = url_object.get("url")
            url_object_name = url_object.get("name")
            if len(url) > 400:
                raise PluginException(
                    cause="URL exceeds max length of 400.",
                    assistance="Please shorten the URL or try another.",
                )

            url_id = self.make_url_object(name=url_object_name, url=url)
            urls["objects"].append({"type": "URL", "id": url_id, "name": url_object_name})
        policy = self.make_policy(policy_name=policy_name)
        print(f"Policy:\n{policy}\nRule Name:\n{rule_name}\nURLS:\n{urls}")
        self.make_rule(policy=policy, rule_name=rule_name, urls=urls)

        return {Output.SUCCESS: True}
