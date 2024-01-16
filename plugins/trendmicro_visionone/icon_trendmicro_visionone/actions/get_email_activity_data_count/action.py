import insightconnect_plugin_runtime
from .schema import GetEmailActivityDataCountInput, GetEmailActivityDataCountOutput, Input, Output, Component
# Custom imports below


class GetEmailActivityDataCount(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_email_activity_data_count',
                description=Component.DESCRIPTION,
                input=GetEmailActivityDataCountInput(),
                output=GetEmailActivityDataCountOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
