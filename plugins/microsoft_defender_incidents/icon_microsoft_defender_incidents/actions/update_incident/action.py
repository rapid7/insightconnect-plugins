import insightconnect_plugin_runtime

# Custom imports below
from ...util.tools import return_non_empty
from .schema import Component, Input, Output, UpdateIncidentInput, UpdateIncidentOutput


class UpdateIncident(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_incident",
            description=Component.DESCRIPTION,
            input=UpdateIncidentInput(),
            output=UpdateIncidentOutput(),
        )

    def run(self, params={}):
        identifier = params.get(Input.IDENTIFIER)
        data = return_non_empty(
            {
                "status": params.get(Input.STATUS),
                "assignedTo": params.get(Input.ASSIGNEDTO),
                "classification": params.get(Input.CLASSIFICATION),
                "determination": params.get(Input.DETERMINATION),
                "tags": params.get(Input.TAGS),
                "comment": params.get(Input.COMMENTS),
            }
        )

        return self.connection.client.update_incident(identifier, data)
