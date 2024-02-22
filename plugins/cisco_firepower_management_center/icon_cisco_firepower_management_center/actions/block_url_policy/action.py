import insightconnect_plugin_runtime
from .schema import BlockUrlPolicyInput, BlockUrlPolicyOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException
from typing import Union, Dict, Any

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
        A method to get the individual policy object if it is found, otherwise
        return None

        :param policy_name: Name of the policy

        :return: Policy object if found, else None
        """

        policies = self.connection.cisco_firepower_api.get_policies()
        # If get AND found, return whole individual policy object
        for policy in policies:
            if policy.get("name", "") == policy_name:
                return self.connection.cisco_firepower_api.get_policies(policy.get("id", ""))
        return None

    def make_policy(self, policy_name: str) -> dict:
        """
        A method to create a new policy object with the given name if not found,
        else return the policy object matching the input name

        :param policy_name: Name of the policy

        :return: Policy object
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

    def check_url_exists(self, name: str) -> Union[str, None]:
        """
        Helper method to check if the name for the URL already exists,
        to prevent the code breaking if name is already found.

        :param name: URL name

        :return: The ID for the associated URL name if found, else None
        """

        response = self.connection.cisco_firepower_api.get_urls()

        for item in response:
            if item.get("name", "") == name:
                self.logger.info(f"{name} found in URL List...")
                return item.get("id", "")

        return None

    def make_url_object(self, name: str, url: str) -> str:
        """
        A method to post the input URLs to add them to the db,
        then get the URLs and return the corresponding, newly created ID for each.

        :param name: URL Name, e.g. google
        :param url: URL, e.g. https://www.google.com

        :return: Unique ID associated with URL
        """

        # Check if URL exists first
        check_url = self.check_url_exists(name)

        # If it does not exist, post
        if not check_url:
            self.logger.info(f"{name} not found, creating...")
            response = self.connection.cisco_firepower_api.post_urls({"name": name, "url": url})
            return response.get("id", "")

        return check_url

    def make_rule(self, policy: Dict[str, Any], rule_name: str, urls: list[dict[str, str | Any]]) -> None:
        """
        Make a new rule based on the input.

        :param policy: Policy object from previous steps
        :param rule_name: Name of the rule
        :param urls: Object containing the URLs

        :return: None
        """
        payload = {
            "name": rule_name,
            "urls": {"objects": urls},
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
        url_objects = params.get(Input.URL_OBJECTS)

        urls = []
        self.logger.info("Posting URLS")
        for url_object in url_objects:
            url = url_object.get("url")
            url_object_name = url_object.get("name")
            if len(url) > 400:
                raise PluginException(
                    cause="URL exceeds max length of 400.",
                    assistance="Please shorten the URL or try another.",
                )

            url_id = self.make_url_object(name=url_object_name, url=url)
            urls.append({"type": "URL", "id": url_id, "name": url_object_name})
        policy = self.make_policy(policy_name=policy_name)
        self.make_rule(policy=policy, rule_name=rule_name, urls=urls)

        return {Output.SUCCESS: True}
