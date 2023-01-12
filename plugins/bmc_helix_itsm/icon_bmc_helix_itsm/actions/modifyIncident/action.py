import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import ModifyIncidentInput, ModifyIncidentOutput, Input, Output, Component

# Custom imports below
from icon_bmc_helix_itsm.util.constants import IncidentRequest, IncidentStatus


class ModifyIncident(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="modifyIncident",
            description=Component.DESCRIPTION,
            input=ModifyIncidentInput(),
            output=ModifyIncidentOutput(),
        )

    def run(self, params={}):
        if params.get(Input.STATUS) in IncidentStatus().get_all_parameters() and not params.get(Input.STATUSREASON):
            raise PluginException(
                cause="Status reason not provided.",
                assistance=f"Please provide a Status Reason parameter for {IncidentStatus().get_all_parameters()} incident status and try again. If the issue persists, please contact support",
            )

        incident_parameters = {
            IncidentRequest.DESCRIPTION: params.get(Input.DESCRIPTION),
            IncidentRequest.STATUS: params.get(Input.STATUS),
            IncidentRequest.STATUS_REASON: params.get(Input.STATUSREASON),
            IncidentRequest.RESOLUTION: params.get(Input.RESOLUTIONNOTE),
        }
        return {
            Output.SUCCESS: self.connection.api_client.modify_incident(
                params.get(Input.INCIDENTNUMBER), incident_parameters
            )
        }
