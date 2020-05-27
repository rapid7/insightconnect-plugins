import komand
from .schema import OpeniocFilesListInput, OpeniocFilesListOutput, Input, Component
# Custom imports below
import urllib.parse
import json


class OpeniocFilesList(komand.Action):
    SORTING_COLUMNS = {
        "FileName": 1,
        "Title": 2,
        "FileAddedDatetime": 3,
        "UploadedFrom": 4,
        "UploadedBy": 5,
        "ExtractingStatus": 6
    }
    SORTING_DIRECTION = {
        "Ascending": 1,
        "Descending": 2
    }

    def __init__(self):
        super(self.__class__, self).__init__(
            name='openioc_files_list',
            description=Component.DESCRIPTION,
            input=OpeniocFilesListInput(),
            output=OpeniocFilesListOutput())

    def run(self, params={}):
        params = {
            "FileHashIDList": params.get(Input.FILE_HASH_ID_LIST, []),
            "PageSize": params.get(Input.PAGE_SIZE, 10),
            "PageNumber": params.get(Input.PAGE_NUMBER, 1),
            "SortingColumn": self.SORTING_COLUMNS.get(params.get(Input.SORTING_COLUMN, "FileAddedDatetime")),
            "SortingDirection": self.SORTING_DIRECTION.get(params.get(Input.SORTING_DIRECTION, "Descending"))
        }

        if params.get(Input.FUZZY_MATCH_STRING):
            params["FuzzyMatchString"] = params.get(Input.FUZZY_MATCH_STRING)

        quoted_param = urllib.parse.quote(json.dumps(params))

        return self.connection.api.execute(
            "get",
            f"/WebApp/IOCBackend/OpenIOCResource/FilingCabinet?param={quoted_param}",
            ""
        )
