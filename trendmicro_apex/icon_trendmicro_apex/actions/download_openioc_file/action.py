import komand
from .schema import DownloadOpeniocFileInput, DownloadOpeniocFileOutput, Input, Component
# Custom imports below
import urllib.parse
import json


class DownloadOpeniocFile(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='download_openioc_file',
            description=Component.DESCRIPTION,
            input=DownloadOpeniocFileInput(),
            output=DownloadOpeniocFileOutput())

    def run(self, params={}):
        quoted_param = urllib.parse.quote(json.dumps({
            "FileHashID": params.get(Input.FILE_HASH_ID)
        }))
        return self.connection.api.execute(
            "get",
            f"/WebApp/IOCBackend/OpenIOCResource/File?param={quoted_param}",
            ""
        )
