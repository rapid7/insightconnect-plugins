import insightconnect_plugin_runtime
from .schema import ArchiveSensorInput, ArchiveSensorOutput, Input, Output, Component
# Custom imports below


class ArchiveSensor(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='archive_sensor',
                description=Component.DESCRIPTION,
                input=ArchiveSensorInput(),
                output=ArchiveSensorOutput())

    def run(self, params={}):
        return{
            Output.ARCHIVE_SENSOR_RESPONSE: self.connection.api.archive_sensor(
                params.get(Input.SENSOR_IDS),
                params.get(Input.ARGUMENT)
            )
        }
