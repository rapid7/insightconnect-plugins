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
        customer = params.get(Input.CUSTOMER, None)
        assignee = params.get(Input.ASSIGNEE, None)
        status = params.get(Input.STATUS, None)
        category = params.get(Input.CATEGORY, None)
        cause_code = params.get(Input.CAUSE_CODE, None)
        resolution = params.get(Input.RESOLUTION, None)

        if not self._check_parameters_exist([customer, assignee, status, category, cause_code, resolution]):
            raise PluginException(
                cause='No parameters provided.',
                assistance='No parameters provided to update. Please validate and try again.'
            )

        # Nie mam pojecia czemu to nie dziala, jak testuje osobno to wszystko jest ok, ale w akcji nie dziala.
        # A bylo by troche czysciej
        # if all(v is None for v in [customer, assignee, status, category, cause_code, resolution]):
        #     raise PluginException(
        #         cause='No parameters provided.',
        #         assistance='No parameters provided to update. Please validate and try again.'
        #     )
        
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

    @staticmethod
    def _check_parameters_exist(variables: list) -> bool:
        i = 0
        for variable in variables:
            if variable:
                i += 1
        if i == 0:
            return False
        return True
