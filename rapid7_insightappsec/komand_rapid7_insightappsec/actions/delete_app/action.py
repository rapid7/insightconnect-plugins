import insightconnect_plugin_runtime
from .schema import DeleteAppInput, DeleteAppOutput, Input, Output, Component
# Custom imports below
from komand_rapid7_insightappsec.util.endpoints import Apps
from komand_rapid7_insightappsec.util.resource_helper import ResourceHelper
from insightconnect_plugin_runtime.exceptions import PluginException

class DeleteApp(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_app',
                description=Component.DESCRIPTION,
                input=DeleteAppInput(),
                output=DeleteAppOutput())

    def run(self, params={}):
        # TODO: Implement run function
        app_id = params.get(Input.APP_ID)
        request = ResourceHelper(self.connection.session, self.logger)

        url = Apps.delete_app(self.connection.url,app_id)
        # url = f'{url}{app_id}'

        response = request.resource_request(url, 'delete')

        return {Output.STATUS: response['status']}
