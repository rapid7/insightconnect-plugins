import insightconnect_plugin_runtime
from .schema import UpdateAppInput, UpdateAppOutput, Input, Output, Component
# Custom imports below
from komand_rapid7_insightappsec.util.endpoints import Apps
from komand_rapid7_insightappsec.util.resource_helper import ResourceHelper
from insightconnect_plugin_runtime.exceptions import PluginException
import json

class UpdateApp(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='update_app',
                description=Component.DESCRIPTION,
                input=UpdateAppInput(),
                output=UpdateAppOutput())

    def run(self, params={}):
        # TODO: Implement run function
        app_id = params.get(Input.APP_ID)
        app_name = params.get(Input.APP_NAME)
        app_description = params.get(Input.APP_DESCRIPTION)
        request = ResourceHelper(self.connection.session, self.logger)

        url = Apps.update_app(self.connection.url,app_id)
        payload = {'name': app_name, 'description': app_description}

        try:
            response = request.resource_request(url, 'put', payload=payload)

        except json.decoder.JSONDecodeError:
            self.logger.error(f'InsightAppSec response: {response}')
            raise PluginException(cause='The response from InsightAppSec was not in JSON format.', assistance='Contact support for help.'
                                        ' See log for more details')

        return {Output.STATUS: response['status']}
