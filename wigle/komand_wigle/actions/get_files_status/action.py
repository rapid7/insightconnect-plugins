import komand
from .schema import GetFilesStatusInput, GetFilesStatusOutput
# Custom imports below


class GetFilesStatus(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_files_status',
                description='Get the status of files uploaded by the current user',
                input=GetFilesStatusInput(),
                output=GetFilesStatusOutput())

    def run(self, params={}):
        self.logger.info(
            'GetFileStatus: Fetching status of uploaded files from server ...'
        )
        response = self.connection.call_api(
            'get', 'file/transactions', params={
                'pagestart': params.get('pagestart', 0),
                'pageend': params.get('pageend', 100)
            }
        )
        return response

    def test(self):
        return {
          "results": [
            {
              "transid": "string",
              "username": "string",
              "firstTime": "2018-08-28T17:24:07.478Z",
              "lastupdt": "2018-08-28T17:24:07.478Z",
              "fileName": "string",
              "fileSize": 0,
              "fileLines": 0,
              "status": "string",
              "discoveredGps": 0,
              "discovered": 0,
              "total": 0,
              "totalGps": 0,
              "totalLocations": 0,
              "percentDone": 0,
              "timeParsing": 0,
              "genDiscovered": 0,
              "genDiscoveredGps": 0,
              "genTotal": 0,
              "genTotalGps": 0,
              "genTotalLocations": 0,
              "wait": 0
            }
          ],
          "processingQueueDepth": 0
        }
