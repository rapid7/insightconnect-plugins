import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import GetIncidentInput, GetIncidentOutput, Input, Output, Component


# Custom imports below


class GetIncident(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_incident",
            description=Component.DESCRIPTION,
            input=GetIncidentInput(),
            output=GetIncidentOutput()
        )

    def run(self, params={}):
        response = self.connection.ivanti_service_manager_api.get_incident_by_number(
            params.get(Input.INCIDENT_NUMBER))
        return {"incident": response}
