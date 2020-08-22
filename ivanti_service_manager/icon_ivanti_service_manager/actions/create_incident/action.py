import insightconnect_plugin_runtime
from .schema import CreateIncidentInput, CreateIncidentOutput, Input, Output, Component
# Custom imports below


class CreateIncident(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_incident',
                description=Component.DESCRIPTION,
                input=CreateIncidentInput(),
                output=CreateIncidentOutput())

    def run(self, params={}):
        urgency = params.get(Input.URGENCY)
        assignee = params.get(Input.ASSIGNEE)
        source = params.get(Input.SOURCE)
        impact = params.get(Input.IMPACT)
        category = params.get(Input.CATEGORY)

        payload = {
            'Subject': params.get(Input.SUMMARY),
            'Symptom': params.get(Input.DESCRIPTION),
            'ProfileLink': self.connection.ivanti_service_manager_api.search_employee(
                params.get(Input.CUSTOMER)
            ).get('RecId'),
            'Status': params.get(Input.STATUS),
            'TypeOfIncident': params.get(Input.TYPE)
        }

        if urgency:
            payload['Urgency'] = urgency
        if assignee:
            payload['Owner'] = assignee
        if source:
            payload['Source'] = source
        if impact:
            payload['Impact'] = impact
        if category:
            payload['Category'] = category

        return {
            Output.INCIDENT: self.connection.ivanti_service_manager_api.post_incident(payload)
        }
