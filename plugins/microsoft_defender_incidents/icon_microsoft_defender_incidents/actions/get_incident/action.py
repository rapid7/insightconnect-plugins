import insightconnect_plugin_runtime

from .schema import Component, GetIncidentInput, GetIncidentOutput, Input, Output

# Custom imports below


class GetIncident(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_incident", description=Component.DESCRIPTION, input=GetIncidentInput(), output=GetIncidentOutput()
        )

    def run(self, params={}):
        identifier = params.get(Input.IDENTIFIER)
        return self.connection.client.get_incident(identifier)
