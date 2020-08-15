import insightconnect_plugin_runtime
from .schema import UpdateIncidentInput, UpdateIncidentOutput, Input, Output, Component
# Custom imports below


class UpdateIncident(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='update_incident',
                description=Component.DESCRIPTION,
                input=UpdateIncidentInput(),
                output=UpdateIncidentOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
