import insightconnect_plugin_runtime
from .schema import GetFileIdFromAlertIdInput, GetFileIdFromAlertIdOutput, Input, Output
# Custom imports below


class GetFileIdFromAlertId(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_file_id_from_alert_id',
                description='Retrieves the File ID related to an alert',
                input=GetFileIdFromAlertIdInput(),
                output=GetFileIdFromAlertIdOutput())

    def run(self, params={}):
        self.logger.info("Running...")
        alert_id = params.get(Input.ALERT_ID)
        self.logger.info("Looking for alerts matching ID: " + alert_id)

        file_payload = self.connection.client.get_files_from_id(alert_id)
        files = file_payload.get("value")

        return {Output.FILE_LIST: insightconnect_plugin_runtime.helper.clean(files)}
