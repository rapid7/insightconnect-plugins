import komand
from .schema import RetrieveFileCatalogEntryInput, RetrieveFileCatalogEntryOutput
# Custom imports below


class RetrieveFileCatalogEntry(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='retrieve_file_catalog_entry',
                description='Retrieves a file catalog entry for a file given the file catalog ID',
                input=RetrieveFileCatalogEntryInput(),
                output=RetrieveFileCatalogEntryOutput())

    def run(self, params={}):
        file_catalog_id = params.get("file_catalog_id")

        url = self.connection.host + '/api/bit9platform/v1/fileCatalog/%d' % file_catalog_id

        response = self.connection.session.get(url=url, verify=self.connection.verify)

        try:
            response.raise_for_status()
        except:
            raise Exception('Run: HTTPError: %s' % response.text)
        else:
            file_catalog_entry = response.json()
            file_catalog_entry = komand.helper.clean(file_catalog_entry)

        return {"file_catalog_entry": file_catalog_entry}

    def test(self):
        url = self.connection.host + "/api/bit9platform/v1/approvalRequest?limit=-1"  # -1 returns just the count (lightweight call)

        request = self.connection.session.get(url=url, verify=self.connection.verify)

        try:
            request.raise_for_status()
        except:
            raise Exception('Run: HTTPError: %s' % request.text)

        return {}

