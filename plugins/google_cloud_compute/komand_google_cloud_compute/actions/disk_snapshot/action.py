import insightconnect_plugin_runtime

from .schema import DiskSnapshotInput, DiskSnapshotOutput, Input, Component


class DiskSnapshot(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="disk_snapshot",
            description=Component.DESCRIPTION,
            input=DiskSnapshotInput(),
            output=DiskSnapshotOutput(),
        )

    def run(self, params={}):
        data = {"name": params.get(Input.NAME)}

        if params.get(Input.DESCRIPTION):
            data["description"] = params.get(Input.DESCRIPTION)

        snapshot_encryption_key = params.get(Input.SNAPSHOTENCRYPTIONKEY)
        if any(snapshot_encryption_key.values()):
            data["snapshotEncryptionKey"] = snapshot_encryption_key

        source_disk_encryption_key = params.get(Input.SOURCEDISKENCRYPTIONKEY)
        if any(source_disk_encryption_key.values()):
            data["sourceDiskEncryptionKey"] = source_disk_encryption_key

        return self.connection.client.disk_snapshot(params.get(Input.ZONE), params.get(Input.DISK), data)
