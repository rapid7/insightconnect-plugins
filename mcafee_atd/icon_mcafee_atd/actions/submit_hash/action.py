import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import SubmitHashInput, SubmitHashOutput, Input, Output, Component
# Custom imports below
import validators


class SubmitHash(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='submit_hash',
            description=Component.DESCRIPTION,
            input=SubmitHashInput(),
            output=SubmitHashOutput())

    def run(self, params={}):
        if validators.md5(params.get(Input.HASH)):
            return {
                Output.SUCCESS: True,
                Output.RESULTS: self.connection.mcafee_atd_api.submit_hash(params.get(Input.HASH))
            }

        raise PluginException(
            cause="The McAfee ATD API only supports MD5 Hash. ",
            assistance="Please enter MD5 Hash and try again."
        )
