import dicttoxml
from insightconnect_plugin_runtime.exceptions import PluginException

from komand_palo_alto_pan_os.util.log_helper import LogHelper


class SecurityPolicy:
    def __init__(self, logger=None) -> None:
        if logger:
            self.logger = logger
        else:
            self.logger = LogHelper().logger

    def extract_from_security_policy(self, policy: dict) -> dict:  # noqa: MC0001
        """
        Removes extraneous xml data from a current security policy so that it can be edited.
        :param policy: A PAN-OS security policy
        :return A new cleaner dictionary containing the polices current config.
        """
        self.logger.debug(f" Base policy {policy}")

        key_list = [
            "source",
            "destination",
            "service",
            "application",
            "source-user",
            "to",
            "from",
            "category",
            "hip-profiles",
        ]
        output = {}
        for key in key_list:
            try:
                output[key] = policy["response"]["result"]["entry"][key]["member"]
            except KeyError:
                self.logger.info(f"Current policy {policy}")
                self.logger.info(f"The current policy has no {key} policy: Setting to any.")
                output[key] = "any"
            except TypeError:
                self.logger.info(f"Current policy {policy}")
                self.logger.info(f"The current policy has no policy config for {key}: Setting to any.")
                output[key] = "any"
            except BaseException:
                raise PluginException(
                    cause="An unknown formatting error occurred when formatting a security policy.",
                    assistance="Contact support for help.",
                    data=f"Policy config: {policy}",
                )
        try:
            output["action"] = policy["response"]["result"]["entry"]["action"]
        except KeyError:
            raise PluginException(
                cause="Current policy config missing an action key.",
                assistance="Contact support for help",
                data=f"Policy config: {policy}",
            )

        for _, object_value in output.items():
            if isinstance(object_value, list):
                if isinstance(object_value[0], dict):
                    for _, object_value_value in object_value.items():
                        try:
                            object_value[key] = object_value_value["#text"]
                        except KeyError:
                            raise PluginException(
                                cause="An unknown formatting error occurred when formatting a security subpolicy.",
                                assistance="Contact support for help.",
                                data=f"Subpolicy {object_value[0]}",
                            )
            if isinstance(object_value, dict):
                if isinstance(object_value, dict) and "#text" in object_value:
                    object_value = object_value["#text"]

        return output

    def add_to_key(self, key, add: str):
        # Key can be a str or list
        """
        Adds new items to a current security policy key
        :param key: The key to add to. it may be a string list or a special string 'any'
        :param add: The string to add to the key, or in the case of the key being 'any' replace with
        :return The updated policy key
        """

        self.logger.debug(f"Starting key {key}")
        self.logger.debug(f"String to add {add}")

        if add not in key:
            if isinstance(key, list):
                key.append(add)
            elif key and key != "any":
                key = [key, add]
            else:
                key = add

        self.logger.debug(f"Ending key {key}")
        return key

    def remove_from_key(self, key, remove: str):
        # Key can be a str or list
        """
        Removes existing items to a current security policy key
        :param key: The key to remove from. it may be a string of a list or a special string 'any'
        :param remove: The string to remove from the key, or in the case of the key being 'any' to replace with
        :return The updated policy key
        """

        self.logger.debug(f"Starting key {key}")
        self.logger.debug(f"String to remove {remove}")

        if remove in key:
            # If a list is reduced to len 1 it must be cast as a str. for 2 or more leave as list
            if isinstance(key, list) and len(key) > 3:
                key.remove(remove)
            elif isinstance(key, list):
                key.remove(remove)
                key = key[0]
            else:
                key = "any"
            self.logger.debug(f"Ending key {key}")
            return key
        self.logger.error(
            "{remove} was not found in {key}."
            " {remove} will not be removed from policy.".format(remove=remove, key=key)
        )
        return key

    def element_for_policy_update(
        self,
        rule_name,
        to,
        from_,
        source,
        destination,
        service,
        application,
        category,
        hip_profiles,
        source_user,
        fire_wall_action,
    ) -> str:
        """
        Builds the updated policy dictionary into a XML string
        :param rule_name: Used to pass the name of the policy to be updated
        :param to: The new to list/str
        :param from_: The new from list/str
        :param source: The new source list/str
        :param destination: The new destination list/str
        :param service: The new service list/str
        :param application: The new application list/str
        :param category: The new category list/str
        :param hip_profiles: The new hip-profiles list/str
        :param source_user: The new source-user list/str
        :param fire_wall_action: The new fire_wall_action list/str
        :return A properly formatted XML file for the security policy
        """
        # Build dic for xml
        element = {
            "to": to,
            "from": from_,
            "source": source,
            "destination": destination,
            "service": service,
            "application": application,
            "category": category,
            "hip-profiles": hip_profiles,
            "source-user": source_user,
            "action": fire_wall_action,
        }

        self.logger.debug(f"Dictionary to convert to XML {element}")

        for key, value in element.items():
            if not value == "action" and isinstance(key, str):
                temp = key
                key = {"member": temp}

        element = dicttoxml.dicttoxml(element, attr_type=False, root=False)
        element = element.decode()
        element = element.replace("<item>", "<member>")
        element = element.replace("</item>", "</member>")
        element = f'<entry name="{rule_name}">{element}</entry>'
        self.logger.info(f"XML :{element}")
        return element


class ExternalList:
    def __init__(self, logger=None) -> None:
        if logger:
            self.logger = logger
        else:
            self.logger = LogHelper().logger

    def element_for_create_external_list(
        self, list_type: str, description: str, source: str, repeat: str, time: str, day: str
    ) -> str:
        """
        Builds the update policy dictionary into a xml string
        :param list_type:
        :param description:
        :param source:
        :param certificate_profile:
        :param repeat:
        :param time:
        :param day:
        :return: A properly formatted xml file for the security policy
        """

        if repeat == "daily":
            if not time:
                raise PluginException(cause="Time of day not defined", assistance="Contact support for help.")
            element = (
                "<type><{list_type}>"
                "<recurring><daily><at>{time}</at></daily></recurring>"
                "<description>{description}</description>"
                "<url>{source}</url>"
                "</{list_type}></type>".format(list_type=list_type, time=time, description=description, source=source)
            )
        elif repeat == "weekly":
            if not time:
                raise PluginException(cause="Time of day not defined", assistance="Contact support for help.")
            if not day:
                raise PluginException(cause="Day of week not defined", assistance="Contact support for help.")
            element = (
                "<type><{list_type}>"
                "<recurring><weekly><day-of-week>{day}</day-of-week>"
                "<at>{time}</at></weekly></recurring>"
                "<description>{description}</description>"
                "<url>{source}</url>"
                "</{list_type}></type>".format(
                    list_type=list_type, day=day, time=time, description=description, source=source
                )
            )
        else:
            element = (
                f"<type><{list_type}>"
                f"<recurring><{repeat}/></recurring>"
                f"<description>{description}</description>"
                f"<url>{source}</url>"
                f"</{list_type}></type>"
            )
        self.logger.info(f"XML :{element}")
        return element
