import komand
from .schema import DeleteOpeniocFileInput, DeleteOpeniocFileOutput, Input, Component
# Custom imports below
import urllib.parse
import json


class DeleteOpeniocFile(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='delete_openioc_file',
            description=Component.DESCRIPTION,
            input=DeleteOpeniocFileInput(),
            output=DeleteOpeniocFileOutput())

    def run(self, params={}):
        quoted_param = urllib.parse.quote(json.dumps({
            "FileHashIDList": params.get(Input.FILE_HASH_ID_LIST)
        }))
        return self.connection.api.execute(
            "delete",
            f"/WebApp/IOCBackend/OpenIOCResource/File?param={quoted_param}",
            ""
        )
