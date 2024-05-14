import insightconnect_plugin_runtime
from .schema import GetPolicyInput, GetPolicyOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class GetPolicy(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_policy", description=Component.DESCRIPTION, input=GetPolicyInput(), output=GetPolicyOutput()
        )

    def run(self, params={}):
        name = params.get(Input.POLICY_NAME)
        device_name = params.get(Input.DEVICE_NAME)
        vsys = params.get(Input.VIRTUAL_SYSTEM)

        xpath = f'/config/devices/entry[@name="{device_name}"]/vsys/entry[@name="{vsys}"]/rulebase/security/rules/entry[@name="{name}"]'

        response = self.connection.request.get_(xpath)

        try:
            entry = response.get("response").get("result").get("entry")

        except AttributeError:
            raise PluginException(
                cause="PAN OS returned an unexpected response.",
                assistance=f"Could not find policy '{name}'. Check the name, virtual system name, and device name.\ndevice name: {device_name}\nvirtual system: {vsys}",
                data=response,
            )

        entry_action = entry.get("action")
        if type(entry_action) is dict:
            action = entry_action.get("#text")
        else:
            action = entry_action

        return {
            Output.TO: self.get_entries(entry, "to"),
            Output.FROM: self.get_entries(entry, "from"),
            Output.SOURCE: self.get_entries(entry, "source"),
            Output.DESTINATION: self.get_entries(entry, "destination"),
            Output.SOURCE_USER: self.get_entries(entry, "source-user"),
            Output.CATEGORY: self.get_entries(entry, "category"),
            Output.APPLICATION: self.get_entries(entry, "application"),
            Output.SERVICE: self.get_entries(entry, "service"),
            Output.HIP_PROFILES: self.get_entries(entry, "hip-profiles"),
            Output.ACTION: action,
        }

    def get_entries(self, entry, key):
        out = []

        member = entry.get(key, {}).get("member")

        if type(member) is str:
            out.append(member)
        elif type(member) is list:
            for m in member:
                if type(m) is dict:
                    out.append(m.get("#text", ""))
                if type(m) is str:
                    out.append(m)
        elif type(member) is dict:
            out.append(member.get("#text", ""))

        return out
