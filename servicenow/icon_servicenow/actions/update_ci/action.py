import insightconnect_plugin_runtime
from .schema import UpdateCiInput, UpdateCiOutput, Input, Output, Component
# Custom imports below


class UpdateCi(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='update_ci',
                description=Component.DESCRIPTION,
                input=UpdateCiInput(),
                output=UpdateCiOutput())

    def run(self, params={}):
        url = f'{self.connection.table_url}{params.get(Input.TABLE)}/{params.get(Input.SYSTEM_ID)}'
        payload = params.get(Input.UPDATE_DATA)
        method = "put"

        response = self.connection.request.make_request(url, method, payload=payload)

        if response.get("status", 0) in range(200, 299):
            success = True
        else:
            success = False

        return {
            Output.SUCCESS: success
        }
