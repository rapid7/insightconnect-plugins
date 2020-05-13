import komand
from .schema import GetPolicyInput, GetPolicyOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException

class GetPolicy(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_policy',
                description=Component.DESCRIPTION,
                input=GetPolicyInput(),
                output=GetPolicyOutput())

    def run(self, params={}):
        name = params.get(Input.POLICY_NAME)
        device_name = params.get(Input.DEVICE_NAME)
        vsys = params.get(Input.VIRTUAL_SYSTEM)

        xpath = f"/config/devices/entry[@name=\"{device_name}\"]/vsys/entry[@name=\"{vsys}\"]/rulebase/security/rules/entry[@name=\"{name}\"]"

        response = self.connection.request.get_(xpath)

        entry = response.get("response", {}).get("result", {}).get("entry", {})
        if not entry:
            raise PluginException(cause="PAN OS returned an unexpected response.",
                                  assistance=f"Could not find policy {name}. Check the name, virutal system name, and device name.\ndevice name: {device_name}\nvirtual system: {vsys}",
                                  data=response)

        to = self.get_entries(entry, "to")
        from_ = self.get_entries(entry, "from")
        source = self.get_entries(entry, "source")
        destination = self.get_entries(entry, "destination")
        source_user = self.get_entries(entry, "source-user")
        category = self.get_entries(entry, "category")
        application = self.get_entries(entry, "application")
        service = self.get_entries(entry, "service")
        hip_profiles = self.get_entries(entry, "hip-profiles")
        action = entry.get("action", {}).get("#text")

        output_object = {
            Output.TO: to,
            Output.FROM: from_,
            Output.SOURCE: source,
            Output.DESTINATION: destination,
            Output.SOURCE_USER: source_user,
            Output.CATEGORY: category,
            Output.APPLICATION: application,
            Output.SERVICE: service,
            Output.HIP_PROFILES: hip_profiles,
            Output.ACTION: action
        }

        return output_object

    def get_entries(self, entry, key):
        out = []

        entries = entry.get(key, {})
        member = entries.get("member")

        if type(member) is list:
            for m in member:
                out.append(m.get("#text",""))
        elif member:
            out.append(member.get("#text",""))

        return out


