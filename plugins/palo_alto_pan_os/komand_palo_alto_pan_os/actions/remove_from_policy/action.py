import insightconnect_plugin_runtime
from .schema import RemoveFromPolicyInput, RemoveFromPolicyOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
from komand_palo_alto_pan_os.util import util


class RemoveFromPolicy(insightconnect_plugin_runtime.Action):
    # used to convert from keys used by plugin input to keys expected by PAN-OS
    _CONVERSION_KEY = {
        "source": "source",
        "destination": "destination",
        "service": "service",
        "application": "application",
        "source-user": "source_user",
        "to": "src_zone",
        "from": "dst_zone",
        "category": "url_category",
        "hip-profiles": "hip_profiles",
        "action": "action",
    }

    def __init__(self):
        super(self.__class__, self).__init__(
            name="remove_from_policy",
            description=Component.DESCRIPTION,
            input=RemoveFromPolicyInput(),
            output=RemoveFromPolicyOutput(),
        )

    def run(self, params={}):
        update = util.SecurityPolicy()
        rule_name = params.get(Input.RULE_NAME)
        policy_type = False
        if params.get("update_active_or_candidate_configuration") == "active":
            policy_type = True

        # Set xpath to security polices
        xpath = f"/config/devices/entry/vsys/entry/rulebase/security/rules/entry[@name='{rule_name}']"

        # Get current policy config
        if policy_type:
            config_output = self.connection.request.show_(xpath=xpath)
        else:
            config_output = self.connection.request.get_(xpath=xpath)

        # Verify and extract needed keys
        current_config = update.extract_from_security_policy(policy=config_output)

        # Update keys
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
            "action",
        ]
        new_policy = {}
        for key in key_list:
            value = self._CONVERSION_KEY.get("key")
            if params.get(value):
                new_policy[key] = update.remove_from_key(current_config[key], params.get(value))
            else:
                new_policy[key] = current_config[key]

        # Build new element
        element = update.element_for_policy_update(
            rule_name=rule_name,
            to=new_policy.get("to"),
            from_=new_policy.get("from"),
            source=new_policy.get("source"),
            destination=new_policy.get("destination"),
            service=new_policy.get("service"),
            application=new_policy.get("application"),
            category=new_policy.get("category"),
            hip_profiles=new_policy.get("hip-profiles"),
            source_user=new_policy.get("source-user"),
            fire_wall_action=new_policy.get("action"),
        )

        # Update policy

        output = self.connection.request.edit_(xpath=xpath, element=element)
        try:
            status = output["response"]["response"]["@status"]
            code = output["response"]["response"]["@code"]
            message = output["response"]["response"]["msg"]
            return {"status": status, "code": code, "message": message}
        except KeyError:
            raise PluginException(
                cause="The output did not contain expected keys.",
                assistance="Contact support for help.",
                data=output,
            )
