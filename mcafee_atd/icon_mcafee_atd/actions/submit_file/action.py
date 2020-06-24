import insightconnect_plugin_runtime
from .schema import SubmitFileInput, SubmitFileOutput, Input, Output, Component
# Custom imports below


class SubmitFile(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='submit_file',
                description=Component.DESCRIPTION,
                input=SubmitFileInput(),
                output=SubmitFileOutput())

    def run(self, params={}):
        return {
            Output.SUBMIT_FILE_INFO: self.connection.mcafee_atd_api.submit_file(
                params.get(Input.FILE),
                params.get(Input.URL_FOR_FILE)
            )
        }
