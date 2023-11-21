import insightconnect_plugin_runtime
from .schema import ListSystemsInput, ListSystemsOutput, Input, Output, Component
# Custom imports below


class ListSystems(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name="list_systems",
                description=Component.DESCRIPTION,
                input=ListSystemsInput(),
                output=ListSystemsOutput())

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        # END INPUT BINDING - DO NOT REMOVE
        # TODO - If input bindings for connection can be done check to same if it you can do the same here

        systems = self.connection.api.server_systems()
        return {"systems": systems}

