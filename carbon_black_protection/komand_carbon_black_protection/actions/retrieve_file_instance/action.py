import komand
from komand.exceptions import PluginException
from .schema import RetrieveFileInstanceInput, RetrieveFileInstanceOutput, Component
# Custom imports below


class RetrieveFileInstance(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='retrieve_file_instance',
                description=Component.DESCRIPTION,
                input=RetrieveFileInstanceInput(),
                output=RetrieveFileInstanceOutput())

    def run(self, params={}):
        file_catalog_id = params.get("file_catalog_id")
        computer_id = params.get("computer_id")

        url = self.connection.host + '/api/bit9platform/v1/fileInstance'
        query = f"q=computerId:{computer_id}&q=fileCatalogId:{file_catalog_id}"

        self.logger.info(f"URL: {url}")
        self.logger.info(f"Query: {query}")

        full_url = url + "?" + query

        self.logger.info(f"Full URL: {full_url}")

        response = self.connection.session.get(url=full_url, verify=self.connection.verify)

        try:
            response.raise_for_status()
        except Exception as e:
            self.logger.error(f"Call to Carbon Black caused the following error: {e}")
            raise PluginException(cause="Call to Carbon Black failed",
                                  assistance="The connection may not be configured properly, please"
                                             "check your connection settings.")
        else:
            file_catalog_entry = response.json()
            file_catalog_entry = komand.helper.clean(file_catalog_entry)

        return {"file_catalog_entry": file_catalog_entry}
