import komand
from .schema import GetFileIdFromAlertIdInput, GetFileIdFromAlertIdOutput
# Custom imports below


class GetFileIdFromAlertId(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_file_id_from_alert_id',
                description='Retrieves the File ID related to an alert',
                input=GetFileIdFromAlertIdInput(),
                output=GetFileIdFromAlertIdOutput())

    def run(self, params={}):
        self.logger.info("Running...")
        alert_id = params.get("alert_id")
        self.logger.info("Looking for alerts matching ID: " + alert_id)
        files = self.connection.get_files_from_alert_id(alert_id)
        try:
            files["file_list"] = files.pop("value")
        except KeyError as k:
            self.logger.error("Could not find 'value' key in file information response: " + str(k))
            raise k

        return {"file_information": komand.helper.clean(files)}

    def test(self):
        self.connection.test()
        file_info = self.connection.fake_file_info()
        file_info['file_list'] = file_info.pop('value')
        return {"file_information": file_info}
