import dicttoxml
from insightconnect_plugin_runtime.exceptions import PluginException

from komand_palo_alto_pan_os.util.log_helper import LogHelper


def extract_member_names(member) -> list:
    """
    Flattens the value of a <member> node into a list of names.

    PAN-OS returns a different shape for every member count and configuration state: a list for two
    or more members, a bare value for exactly one, and a dictionary carrying the candidate config
    attributes (admin, dirtyId, time) for any member edited since the last commit.
    :param member: The value of a <member> node, as parsed from the PAN-OS response
    :return The names held in that node, empty when the node holds none
    """

    if isinstance(member, str):
        return [member]
    if isinstance(member, dict):
        name = member.get("#text")
        return [name] if name else []
    if isinstance(member, list):
        names = []
        for item in member:
            names.extend(extract_member_names(item))
        return names
    return []


def extract_static_members(entry: dict, group_name: str) -> list:
    """
    Returns the names of the address objects in a static address group.
    :param entry: The <entry> node of an address group, as parsed from the PAN-OS response
    :param group_name: The name of the address group, used for error reporting
    :return The names of the group's members, empty when the group has none
    """

    if "static" not in entry:
        raise PluginException(
            cause=f"The address group '{group_name}' is not a static address group.",
            assistance="This action can only read and change the members of a static address group. The members of a "
            "dynamic address group are selected by its tag filter and cannot be changed directly.",
            data=entry,
        )

    return extract_member_names((entry.get("static") or {}).get("member"))


def get_response_entry(response: dict) -> dict:
    """
    Returns the <entry> node of a PAN-OS config response.
    :param response: A parsed PAN-OS response
    :return The <entry> node, or None when the response does not hold exactly one
    """

    entry = ((response.get("response") or {}).get("result") or {}).get("entry")
    return entry if isinstance(entry, dict) else None


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
            # PAN-OS 10.0 removed <hip-profiles> from the security rule, so a rule that does not carry
            # the node must not have one written back to it. Every other key falls back to the 'any'
            # keyword, which is the value PAN-OS itself reports for a key a rule does not narrow.
            default = None if key == "hip-profiles" else "any"
            try:
                output[key] = policy["response"]["result"]["entry"][key]["member"]
            except KeyError:
                self.logger.info(f"Current policy {policy}")
                self.logger.info(f"The current policy has no {key} policy: Setting to {default}.")
                output[key] = default
            except TypeError:
                self.logger.info(f"Current policy {policy}")
                self.logger.info(f"The current policy has no policy config for {key}: Setting to {default}.")
                output[key] = default
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

        for object_key, object_value in list(output.items()):
            output[object_key] = self._strip_attributes(object_value)

        return output

    def _strip_attributes(self, value):
        """
        Reduces a policy value to the names it holds, dropping the candidate config attributes
        (admin, dirtyId, time) that PAN-OS adds to anything edited since the last commit. Those
        attributes are read-only, so a value carrying them cannot be written back out as XML.
        :param value: A single policy value, or a list of them
        :return The value with any attribute dictionary replaced by its name
        """

        if isinstance(value, list):
            return [self._strip_attributes(item) for item in value]
        if isinstance(value, dict):
            if "#text" not in value:
                raise PluginException(
                    cause="An unknown formatting error occurred when formatting a security subpolicy.",
                    assistance="Contact support for help.",
                    data=f"Subpolicy {value}",
                )
            return value["#text"]
        return value

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

        if add not in (key if isinstance(key, list) else [key]):
            if isinstance(key, list):
                key.append(add)
            elif key and key != "any":
                key = [key, add]
            else:
                key = add

        self.logger.debug(f"Ending key {key}")
        return key

    def remove_from_key(self, key, remove: str, key_name: str):
        # Key can be a str or list
        """
        Removes existing items to a current security policy key
        :param key: The key to remove from. it may be a string of a list or a special string 'any'
        :param remove: The string to remove from the key, or in the case of the key being 'any' to replace with
        :param key_name: The name of the key, used for error reporting
        :return The updated policy key
        """

        self.logger.debug(f"Starting key {key}")
        self.logger.debug(f"String to remove {remove}")

        members = key if isinstance(key, list) else [key]
        if remove in members:
            members = [member for member in members if member != remove]
            if not members and remove == "any":
                # The key already matches everything, so there is nothing to narrow and PAN-OS has no
                # narrower value to put in its place. The rule is left as it is.
                self.logger.info(
                    f"The '{key_name}' key of this security rule is already set to 'any', so there is no value to"
                    " remove from it and the rule is left as it is."
                )
                return "any"
            if not members:
                # A security policy key cannot be empty. The only value PAN-OS accepts in place of the
                # last one is the 'any' keyword, which widens the rule to match everything instead of
                # narrowing it, so the removal is refused rather than silently inverted.
                raise PluginException(
                    cause=f"'{remove}' is the only value of the '{key_name}' key of this security rule.",
                    assistance=f"A security rule has to match at least one value for '{key_name}', so this value "
                    "cannot be removed. Removing it would leave the key empty, and the only value PAN-OS accepts in "
                    "its place is the 'any' keyword, which would widen the rule to match every value instead. Use the "
                    "Set Security Policy Rule action to set the key to the values the rule should match.",
                    data=key,
                )
            key = members
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

        # A key the rule does not carry is left out rather than written back as an empty node, which is
        # what keeps <hip-profiles> out of a rule on PAN-OS 10.0 and later, where it was removed.
        # Every other key holds a member list, so a lone value still has to be wrapped in a <member>
        # node. The action is a single keyword (allow, deny, drop, reset-*) and never is.
        for key, value in list(element.items()):
            if value is None:
                del element[key]
            elif key != "action" and isinstance(value, str):
                element[key] = [value]

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
