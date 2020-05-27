import komand
from .schema import UploadOpeniocFileInput, UploadOpeniocFileOutput, Input, Output, Component
# Custom imports below


class UploadOpeniocFile(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='upload_openioc_file',
            description=Component.DESCRIPTION,
            input=UploadOpeniocFileInput(),
            output=UploadOpeniocFileOutput())

    def run(self, params={}):
        files = params.get(Input.FILES)
        payload = {
            "param": [{"FileName": e.get("filename"), "FileContentBase64": e.get("content")} for e in files]
        }
        uploaded = self.connection.api.execute(
            "post",
            "/WebApp/IOCBackend/OpenIOCResource/File",
            payload
        )
        return {
            Output.UPLOADED_INFO_LIST: uploaded.get("Data", {}).get("UploadedResultInfoList", []),
            Output.UPLOADED_MESSAGE_LIST: uploaded.get("Data", {}).get("UploadedResultMessageList", []),
            Output.FEATURECTRL: uploaded.get("FeatureCtrl", {}),
            Output.META: uploaded.get("Meta", {}),
            Output.PERMISSIONCTRL: uploaded.get("PermissionCtrl", {}),
            Output.SYSTEMCTRL: uploaded.get("SystemCtrl", {})
        }
