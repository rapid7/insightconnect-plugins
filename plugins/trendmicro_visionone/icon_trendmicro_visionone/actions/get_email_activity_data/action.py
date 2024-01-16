import insightconnect_plugin_runtime
from .schema import GetEmailActivityDataInput, GetEmailActivityDataOutput, Input, Output, Component
# Custom imports below


class GetEmailActivityData(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_email_activity_data',
                description=Component.DESCRIPTION,
                input=GetEmailActivityDataInput(),
                output=GetEmailActivityDataOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
