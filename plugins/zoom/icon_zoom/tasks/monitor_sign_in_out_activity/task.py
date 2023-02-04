import insightconnect_plugin_runtime
from .schema import MonitorSignInOutActivityInput, MonitorSignInOutActivityOutput, MonitorSignInOutActivityState, Input, Output, Component, State
# Custom imports below


class MonitorSignInOutActivity(insightconnect_plugin_runtime.Task):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='monitor_sign_in_out_activity',
                description=Component.DESCRIPTION,
                input=MonitorSignInOutActivityInput(),
                output=MonitorSignInOutActivityOutput(),
                state=MonitorSignInOutActivityState())

    def run(self, params={}, state={}):
        # TODO: Implement run function
        return {}, {}
