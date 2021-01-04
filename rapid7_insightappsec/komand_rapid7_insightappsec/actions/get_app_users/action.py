import insightconnect_plugin_runtime
from .schema import GetAppUsersInput, GetAppUsersOutput, Input, Output, Component
# Custom imports below
from komand_rapid7_insightappsec.util.endpoints import Apps
from komand_rapid7_insightappsec.util.resource_helper import ResourceHelper
from insightconnect_plugin_runtime.exceptions import PluginException
import json

class GetAppUsers(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_app_users',
                description=Component.DESCRIPTION,
                input=GetAppUsersInput(),
                output=GetAppUsersOutput())

    def run(self, params={}):
        # TODO: Implement run function
        app_id = params.get(Input.APP_ID)
        request = ResourceHelper(self.connection.session, self.logger)

        url = Apps.get_app_users(self.connection.url,app_id)

        response = request.resource_request(url, 'get')
        try:
            result = json.loads(response['resource'])
        except json.decoder.JSONDecodeError:
            self.logger.error(f'InsightAppSec response: {response}')
            raise PluginException(cause='The response from InsightAppSec was not in JSON format.', assistance='Contact support for help.'
                            ' See log for more details')
        return {Output.USER_ID: result}
