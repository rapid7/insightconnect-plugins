import insightconnect_plugin_runtime

from .schema import Component, Input, ListEntitiesInput, ListEntitiesOutput, Output


class ListEntities(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_entities",
            description=Component.DESCRIPTION,
            input=ListEntitiesInput(),
            output=ListEntitiesOutput(),
        )

    def run(self, params={}):
        subscription_id = params.get(Input.SUBSCRIPTIONID)
        incident_id = params.get(Input.INCIDENTID)
        resource_group_name = params.get(Input.RESOURCEGROUPNAME)
        workspace_name = params.get(Input.WORKSPACENAME)
        entities = self.connection.api_client.list_entities(
            incident_id, resource_group_name, workspace_name, subscription_id
        )
        return {Output.ENTITIES: entities}
