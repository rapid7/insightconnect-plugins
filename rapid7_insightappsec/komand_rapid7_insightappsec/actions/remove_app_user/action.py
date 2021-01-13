import insightconnect_plugin_runtime
from .schema import RemoveAppUserInput, RemoveAppUserOutput, Input, Output, Component
# Custom imports below
from komand_rapid7_insightappsec.util.endpoints import Apps
from komand_rapid7_insightappsec.util.resource_helper import ResourceHelper
from insightconnect_plugin_runtime.exceptions import PluginException
import json

class RemoveAppUser(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='remove_app_user',
                description=Component.DESCRIPTION,
                input=RemoveAppUserInput(),
                output=RemoveAppUserOutput())

    def run(self, params={}):
        # TODO: Implement run function
        app_id = params.get(Input.APP_ID)
        user_id = params.get(Input.USER_ID)
        request = ResourceHelper(self.connection.session, self.logger)

        url = Apps.remove_app_user(self.connection.url,app_id,user_id)

        response = request.resource_request(url, 'delete')
        if response['status'] in range(200, 299):
            return {Output.STATUS: response['status']}
        else:
            try:
                result = json.loads(response['resource'])
            except json.decoder.JSONDecodeError:
                self.logger.error(f'InsightAppSec response: {response}')
                raise PluginException(cause='The response from InsightAppSec was not in JSON format.', assistance='Contact support for help.'
                                ' See log for more details')

                return {Output.STATUS: response['status']}
