import insightconnect_plugin_runtime
from .schema import AddAppUserInput, AddAppUserOutput, Input, Output, Component
# Custom imports below
from komand_rapid7_insightappsec.util.endpoints import Apps
from komand_rapid7_insightappsec.util.resource_helper import ResourceHelper
from insightconnect_plugin_runtime.exceptions import PluginException
import json

class AddAppUser(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_app_user',
                description=Component.DESCRIPTION,
                input=AddAppUserInput(),
                output=AddAppUserOutput())

    def run(self, params={}):
        # TODO: Implement run function
        app_id = params.get(Input.APP_ID)
        app_id = app_id['id']
        user_id = params.get(Input.USER_ID)
        user_id = user_id['id']
        request = ResourceHelper(self.connection.session, self.logger)

        url = Apps.add_app_user(self.connection.url,app_id)
        payload = {'id':user_id}

        response = request.resource_request(url, 'post', payload=payload)
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
