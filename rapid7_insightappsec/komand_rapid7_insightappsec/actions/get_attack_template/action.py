import insightconnect_plugin_runtime
from .schema import GetAttackTemplateInput, GetAttackTemplateOutput, Input, Output, Component
# Custom imports below
from komand_rapid7_insightappsec.util.endpoints import AttackTemplates
from komand_rapid7_insightappsec.util.resource_helper import ResourceHelper
import json
from insightconnect_plugin_runtime.exceptions import PluginException

class GetAttackTemplate(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_attack_template',
                description=Component.DESCRIPTION,
                input=GetAttackTemplateInput(),
                output=GetAttackTemplateOutput())

    def run(self, params={}):
        id = params.get(Input.ID)
        request = ResourceHelper(self.connection.session, self.logger)

        url = AttackTemplates.get_attack_template(self.connection.url,id)

        response = request.resource_request(url, 'get')
        try:
            result = json.loads(response['resource'])
        except (json.decoder.JSONDecodeError, TypeError, KeyError):
            self.logger.error(f'InsightAppSec response: {response}')
            raise PluginException(cause=PluginException.Preset.INVALID_JSON, assistance=PluginException.Preset.INVALID_JSON)

        return result
