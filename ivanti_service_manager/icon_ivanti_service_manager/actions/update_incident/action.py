import insightconnect_plugin_runtime
from .schema import UpdateIncidentInput, UpdateIncidentOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException
# Custom imports below


class UpdateIncident(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='update_incident',
                description=Component.DESCRIPTION,
                input=UpdateIncidentInput(),
                output=UpdateIncidentOutput())

    def run(self, params={}):
        customer = params.get(Input.CUSTOMER)
        assignee = params.get(Input.ASSIGNEE)
        status = params.get(Input.STATUS)
        category = params.get(Input.CATEGORY)
        cause_code = params.get(Input.CAUSE_CODE)
        resolution = params.get(Input.RESOLUTION)

        if all((v is None or v == "") for v in [customer, assignee, status, category, cause_code, resolution]):
            raise PluginException(
                cause='At least one action input is required.',
                assistance='No parameters provided to update. Please validate and try again.'
            )
        
        payload = {}
        if assignee:
            payload['Owner'] = self.connection.ivanti_service_manager_api.search_employee(
                assignee
            ).get('LoginID')
        if customer:
            payload['ProfileLink'] = self.connection.ivanti_service_manager_api.search_employee(
                customer
            ).get('RecId')
        if status:
            payload['Status'] = status
        if category:
            payload['Category'] = category
        if cause_code:
            payload['CauseCode'] = cause_code
        if resolution:
            payload['Resolution'] = resolution

        return {
            Output.INCIDENT: self.connection.ivanti_service_manager_api.update_incident(
                self.connection.ivanti_service_manager_api.get_incident_by_number(
                    params.get(Input.INCIDENT_NUMBER)
                ).get('RecId'),
                payload
            )
        }
