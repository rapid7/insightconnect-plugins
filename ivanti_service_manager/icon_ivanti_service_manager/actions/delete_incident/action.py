import insightconnect_plugin_runtime
from .schema import DeleteIncidentInput, DeleteIncidentOutput, Input, Output, Component
# Custom imports below


class DeleteIncident(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_incident',
                description=Component.DESCRIPTION,
                input=DeleteIncidentInput(),
                output=DeleteIncidentOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
