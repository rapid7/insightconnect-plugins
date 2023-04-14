import insightconnect_plugin_runtime
from .schema import GetIncidentInput, GetIncidentOutput, Input, Output, Component

# Custom imports below
from icon_bmc_helix_itsm.util.helpers import convert_dict_keys_to_camel_case, filter_dict_keys, clean_dict
from icon_bmc_helix_itsm.util.constants import Incident, IncidentResponse


class GetIncident(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="getIncident", description=Component.DESCRIPTION, input=GetIncidentInput(), output=GetIncidentOutput()
        )

    def run(self, params={}):
        incident = self.connection.api_client.get_incident(params.get(Input.INCIDENTNUMBER)).get(
            IncidentResponse.VALUES, {}
        )
        incident = filter_dict_keys(incident, Incident().get_all_parameters())
        incident = convert_dict_keys_to_camel_case(incident)
        return {Output.INCIDENT: clean_dict(incident)}
