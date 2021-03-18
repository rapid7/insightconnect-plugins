import insightconnect_plugin_runtime

from .schema import ListSnapshotsInput, ListSnapshotsOutput, Input, Component


# Custom imports below


class ListSnapshots(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_snapshots",
            description=Component.DESCRIPTION,
            input=ListSnapshotsInput(),
            output=ListSnapshotsOutput(),
        )

    def run(self, params={}):
        return self.connection.client.list_snapshots(
            params.get(Input.FILTER), params.get(Input.MAXRESULTS), params.get(Input.ORDERBY)
        )
