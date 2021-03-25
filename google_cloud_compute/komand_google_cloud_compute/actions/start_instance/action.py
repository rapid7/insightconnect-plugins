import insightconnect_plugin_runtime

from .schema import StartInstanceInput, StartInstanceOutput, Input, Component


# Custom imports below


class StartInstance(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="start_instance",
            description=Component.DESCRIPTION,
            input=StartInstanceInput(),
            output=StartInstanceOutput(),
        )

    def run(self, params={}):
        return self.connection.client.start_instance(params.get(Input.ZONE), params.get(Input.INSTANCE))
