import komand
from .schema import RemoveFromPolicyInput, RemoveFromPolicyOutput
from komand.exceptions import PluginException
# Custom imports below
from komand_palo_alto_pan_os.util import util


class RemoveFromPolicy(komand.Action):
    # used to convert from keys used by plugin input to keys expected by PAN-OS
    _CONVERSION_KEY = {'source': 'source',
                       'destination': 'destination',
                       'service': 'service',
                       'application': 'application',
                       'source-user': 'source_user',
                       'to': 'src_zone',
                       'from': 'dst_zone',
                       'category': 'url_category',
                       'hip-profiles': 'hip_profiles',
                       'action': 'action'}

    def __init__(self):
        super(self.__class__, self).__init__(
                name='remove_from_policy',
                description='Remove a rule to a PAN-OS security policy',
                input=RemoveFromPolicyInput(),
                output=RemoveFromPolicyOutput())

    def run(self, params={}):
        update = util.SecurityPolicy()
        rule_name = params.get('rule_name')
        policy_type = False
        if params.get('update_active_or_candidate_configuration') == 'active':
            policy_type = True

        # Set xpath to security polices
        xpath = "/config/devices/entry/vsys/entry/rulebase/security/rules/entry[@name='{0}']".format(rule_name)

        # Get current policy config
        if policy_type:
            config_output = self.connection.request.show_(xpath=xpath)
        else:
            config_output = self.connection.request.get_(xpath=xpath)

        # Verify and extract needed keys
        current_config = update.extract_from_security_policy(policy=config_output)

        # Update keys
        key_list = ['source', 'destination', 'service',
                    'application', 'source-user', 'to',
                    'from', 'category', 'hip-profiles', 'action']
        new_policy = {}
        for i in key_list:
            value = self._CONVERSION_KEY[i]
            if params.get(value):
                new_policy[i] = update.remove_from_key(current_config[i], params.get(value))
            else:
                new_policy[i] = current_config[i]

        # Build new element
        element = update.element_for_policy_update(rule_name=rule_name,
                                                   to=new_policy['to'],
                                                   from_=new_policy['from'],
                                                   source=new_policy['source'],
                                                   destination=new_policy['destination'],
                                                   service=new_policy['service'],
                                                   application=new_policy['application'],
                                                   category=new_policy['category'],
                                                   hip_profiles=new_policy['hip-profiles'],
                                                   source_user=new_policy['source-user'],
                                                   fire_wall_action=new_policy['action'])

        # Update policy

        output = self.connection.request.edit_(xpath=xpath, element=element)
        try:
            status = output['response']['response']['@status']
            code = output['response']['response']['@code']
            message = output['response']['response']['msg']
            return {"status": status, 'code': code, 'message': message}
        except KeyError:
            raise PluginException(cause='The output did not contain expected keys.',
                                  assistance='Contact support for help.',
                                  data=output)
