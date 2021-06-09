import insightconnect_plugin_runtime

from .schema import StopInstanceInput, StopInstanceOutput, Input, Component


# Custom imports below


class StopInstance(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="stop_instance",
            description=Component.DESCRIPTION,
            input=StopInstanceInput(),
            output=StopInstanceOutput(),
        )

    def run(self, params={}):
        return self.connection.client.stop_instance(params.get(Input.ZONE), params.get(Input.INSTANCE))
