import insightconnect_plugin_runtime
from .schema import SubmitUrlInput, SubmitUrlOutput, Input, Output, Component
# Custom imports below


class SubmitUrl(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='submit_url',
            description=Component.DESCRIPTION,
            input=SubmitUrlInput(),
            output=SubmitUrlOutput())

    def run(self, params={}):
        return {
            Output.SUBMIT_URL_INFO: self.connection.mcafee_atd_api.submit_url(
                params.get(Input.URL),
                params.get(Input.SUBMIT_TYPE)
            )
        }
