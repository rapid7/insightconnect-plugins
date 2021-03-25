import insightconnect_plugin_runtime

from .schema import DeleteSnapshotsInput, DeleteSnapshotsOutput, Input, Component


class DeleteSnapshots(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_snapshots",
            description=Component.DESCRIPTION,
            input=DeleteSnapshotsInput(),
            output=DeleteSnapshotsOutput(),
        )

    def run(self, params={}):
        return self.connection.client.delete_snapshots(params.get(Input.SNAPSHOT))
