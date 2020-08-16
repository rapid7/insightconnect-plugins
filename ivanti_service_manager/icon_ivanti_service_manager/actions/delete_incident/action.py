import insightconnect_plugin_runtime
from .schema import DeleteIncidentInput, DeleteIncidentOutput, Input, Output, Component
# Custom imports below


class DeleteIncident(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_incident',
                description=Component.DESCRIPTION,
                input=DeleteIncidentInput(),
                output=DeleteIncidentOutput())

    def run(self, params={}):
        errors = self.connection.ivanti_service_manager_api.delete_incident(
            self.connection.ivanti_service_manager_api.get_incident_by_number(
                params.get(Input.INCIDENT_NUMBER)
            ).get('RecId')
        )

        if len(errors) != 0:
            raise PluginException(cause='The response from the Ivanti Service Manager was not in the correct format.',
                                  assistance='Contact support for help. See log for more details',
                                  data=errors)

        return {
            Output.SUCCESS: True
        }
