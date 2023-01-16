import insightconnect_plugin_runtime
from .schema import GetIncidentWorkInformationInput, GetIncidentWorkInformationOutput, Input, Output, Component

# Custom imports below
from icon_bmc_helix_itsm.util.constants import Worklog
from icon_bmc_helix_itsm.util.helpers import filter_dict_keys, convert_dict_keys_to_camel_case, clean_dict


class GetIncidentWorkInformation(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="getIncidentWorkInformation",
            description=Component.DESCRIPTION,
            input=GetIncidentWorkInformationInput(),
            output=GetIncidentWorkInformationOutput(),
        )

    def run(self, params={}):
        worklogs = self.connection.api_client.get_incident_work_information(params.get(Input.INCIDENTNUMBER))
        clean_worklogs = []
        for worklog in worklogs:
            clean_worklog = filter_dict_keys(worklog, Worklog().get_all_parameters())
            clean_worklog = convert_dict_keys_to_camel_case(clean_worklog)
            clean_worklogs.append(clean_dict(clean_worklog))
        return {Output.WORKLOGS: clean_worklogs}
