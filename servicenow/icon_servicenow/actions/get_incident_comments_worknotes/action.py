import komand
from komand.exceptions import PluginException
from .schema import GetIncidentCommentsWorknotesInput, GetIncidentCommentsWorknotesOutput, Input, Output, Component
# Custom imports below


class GetIncidentCommentsWorknotes(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_incident_comments_worknotes',
                description=Component.DESCRIPTION,
                input=GetIncidentCommentsWorknotesInput(),
                output=GetIncidentCommentsWorknotesOutput())

    def run(self, params={}):
        table = "sys_journal_field"
        url = f'{self.connection.table_url}{table}'
        system_id = params.get(Input.SYSTEM_ID)
        type_ = "work_notes" if params.get(Input.TYPE) == "work notes" else params.get(Input.TYPE)
        fields = "sys_id,sys_created_on,name,element_id,sys_tags,value,sys_created_by,element"

        if type_ == "all":
            url = f'{url}?sysparm_query=element_id={system_id}&sysparm_fields={fields}'
        elif type_ == "comments":
            url = f'{url}?sysparm_query=element_id={system_id}^element={type_}&sysparm_fields={fields}'
        elif type_ == "work_notes":
            url = f'{url}?sysparm_query=element_id={system_id}^element={type_}&sysparm_fields={fields}'

        method = "get"

        response = self.connection.request.make_request(url, method)

        try:
            result = response["resource"].get("result")
        except KeyError as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN,
                                  data=response.text) from e

        return {
            Output.INCIDENT_COMMENTS_WORKNOTES: result
        }
