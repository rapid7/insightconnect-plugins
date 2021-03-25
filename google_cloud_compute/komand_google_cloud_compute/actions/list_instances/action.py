from .schema import ListInstancesInput, ListInstancesOutput, Input, Component


# Custom imports below


class ListInstances(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_instances",
            description=Component.DESCRIPTION,
            input=ListInstancesInput(),
            output=ListInstancesOutput(),
        )

    def run(self, params={}):
        return self.connection.client.list_instances(
            params.get(Input.ZONE), params.get(Input.FILTER), params.get(Input.MAXRESULTS), params.get(Input.ORDERBY)
        )
