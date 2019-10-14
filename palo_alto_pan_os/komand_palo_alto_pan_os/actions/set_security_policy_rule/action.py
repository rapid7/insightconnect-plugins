import komand
from .schema import SetSecurityPolicyRuleInput, SetSecurityPolicyRuleOutput
from komand.exceptions import PluginException
# Custom imports below


class SetSecurityPolicyRule(komand.Action):

    _BOOL_TO_VALUE = {
        True: "yes",
        False: "no"
    }

    def __init__(self):
        super(self.__class__, self).__init__(
                name='set_security_policy_rule',
                description='Create a new Security Policy Rule',
                input=SetSecurityPolicyRuleInput(),
                output=SetSecurityPolicyRuleOutput())

    def run(self, params={}):

        rule_name = params.get('rule_name')
        source = params.get('source')
        destination = params.get('destination')
        service = params.get('service')
        application = params.get('application')
        action = params.get('action')
        source_user = params.get('source_user')
        disable_server_response_inspection = params.get('disable_server_response_inspection')
        negate_source = params.get('negate_source')
        negate_destination = params.get('negate_destination')
        disabled = params.get('disabled')
        log_start = params.get('log_start')
        log_end = params.get('log_end')
        description = params.get('description')
        src_zone = params.get('src_zone')
        dst_zone = params.get('dst_zone')

        # Set boolean values to yes or no
        disable_server_response_inspection = self._BOOL_TO_VALUE[disable_server_response_inspection]
        negate_source = self._BOOL_TO_VALUE[negate_source]
        negate_destination = self._BOOL_TO_VALUE[negate_destination]
        disabled = self._BOOL_TO_VALUE[disabled]
        log_start = self._BOOL_TO_VALUE[log_start]
        log_end = self._BOOL_TO_VALUE[log_end]

        # Build xpath and element
        xpath = "/config/devices/entry/vsys/entry/rulebase/security/rules/entry[@name='{0}']".format(rule_name)
        element = '<source><member>{source}</member></source>' \
                  '<destination><member>{destination}</member></destination>' \
                  '<service><member>{service}</member></service>' \
                  '<application><member>{application}</member></application>' \
                  '<action>{action}</action>' \
                  '<source-user><member>{source_user}</member></source-user>' \
                  '<option><disable-server-response-inspection>{dsri}</disable-server-response-inspection></option>' \
                  '<negate-source>{negate_source}</negate-source>' \
                  '<negate-destination>{negate_destination}</negate-destination>' \
                  '<disabled>{disabled}</disabled>' \
                  '<log-start>{log_start}</log-start>' \
                  '<log-end>{log_end}</log-end>' \
                  '<description>{description}</description>' \
                  '<from><member>{src_zone}</member></from>' \
                  '<to><member>{dst_zone}</member></to>'.format(source=source, destination=destination, service=service,
                                                                application=application, action=action,
                                                                source_user=source_user,
                                                                dsri=disable_server_response_inspection,
                                                                negate_source=negate_source,
                                                                negate_destination=negate_destination,
                                                                disabled=disabled, log_start=log_start, log_end=log_end,
                                                                description=description, src_zone=src_zone,
                                                                dst_zone=dst_zone)

        output = self.connection.request.set_(xpath=xpath, element=element)
        try:
            return {"response": output['response']}
        except KeyError:
            raise PluginException(cause='The output did not contain expected keys.',
                                  assistance='Contact support for help.',
                                  data=output)
