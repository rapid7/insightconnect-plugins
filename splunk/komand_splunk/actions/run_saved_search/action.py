import komand
from .schema import RunSavedSearchInput, RunSavedSearchOutput
# Custom imports below


class RunSavedSearch(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='run_saved_search',
                description='Runs a saved search',
                input=RunSavedSearchInput(),
                output=RunSavedSearchOutput())

    def run(self, params={}):
        saved_search_name = params.get("saved_search_name")

        try:
            saved_search = self.connection.client.saved_searches[saved_search_name]
            search_job = saved_search.dispatch()
            job_id = search_job["sid"]  # Search ID
        except KeyError as error:
            self.logger.error(error)
            raise

        return {"job_id": job_id}

    def test(self):
        return {}
