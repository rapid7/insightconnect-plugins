import insightconnect_plugin_runtime
from .schema import SetSecurityPolicyRuleInput, SetSecurityPolicyRuleOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below


class SetSecurityPolicyRule(insightconnect_plugin_runtime.Action):

    _BOOL_TO_VALUE = {True: "yes", False: "no"}

    def __init__(self):
        super(self.__class__, self).__init__(
            name="set_security_policy_rule",
            description=Component.DESCRIPTION,
            input=SetSecurityPolicyRuleInput(),
            output=SetSecurityPolicyRuleOutput(),
        )

    def run(self, params={}):

        rule_name = params.get(Input.RULE_NAME)
        source = params.get(Input.SOURCE)
        destination = params.get(Input.DESTINATION)
        service = params.get(Input.SERVICE)
        application = params.get(Input.APPLICATION)
        action = params.get(Input.ACTION)
        source_user = params.get(Input.SOURCE_USER)
        disable_server_response_inspection = params.get(Input.DISABLE_SERVER_RESPONSE_INSPECTION)
        negate_source = params.get(Input.NEGATE_SOURCE)
        negate_destination = params.get(Input.NEGATE_DESTINATION)
        disabled = params.get(Input.DISABLED)
        log_start = params.get(Input.LOG_START)
        log_end = params.get(Input.LOG_END)
        description = params.get(Input.DESCRIPTION)
        src_zone = params.get(Input.SRC_ZONE)
        dst_zone = params.get(Input.DST_ZONE)

        # Set boolean values to yes or no
        disable_server_response_inspection = self._BOOL_TO_VALUE[disable_server_response_inspection]
        negate_source = self._BOOL_TO_VALUE[negate_source]
        negate_destination = self._BOOL_TO_VALUE[negate_destination]
        disabled = self._BOOL_TO_VALUE[disabled]
        log_start = self._BOOL_TO_VALUE[log_start]
        log_end = self._BOOL_TO_VALUE[log_end]

        # Build xpath and element
        xpath = f"/config/devices/entry/vsys/entry/rulebase/security/rules/entry[@name='{rule_name}']"
        element = (
            f"<source><member>{source}</member></source>"
            f"<destination><member>{destination}</member></destination>"
            f"<service><member>{service}</member></service>"
            f"<application><member>{application}</member></application>"
            f"<action>{action}</action>"
            f"<source-user><member>{source_user}</member></source-user>"
            f"<option><disable-server-response-inspection>{disable_server_response_inspection}</disable-server-response-inspection></option>"
            f"<negate-source>{negate_source}</negate-source>"
            f"<negate-destination>{negate_destination}</negate-destination>"
            f"<disabled>{disabled}</disabled>"
            f"<log-start>{log_start}</log-start>"
            f"<log-end>{log_end}</log-end>"
            f"<description>{description}</description>"
            f"<from><member>{src_zone}</member></from>"
            f"<to><member>{dst_zone}</member></to>"
        )

        output = self.connection.request.set_(xpath=xpath, element=element)
        try:
            return {Output.RESPONSE: output["response"]}
        except KeyError:
            raise PluginException(
                cause="The output did not contain expected keys.",
                assistance="Contact support for help.",
                data=output,
            )
