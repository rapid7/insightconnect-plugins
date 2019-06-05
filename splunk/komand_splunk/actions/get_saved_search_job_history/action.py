import komand
from .schema import GetSavedSearchJobHistoryInput, GetSavedSearchJobHistoryOutput
# Custom imports below
import json


class GetSavedSearchJobHistory(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_saved_search_job_history',
                description='Returns the job history of a specified saved search',
                input=GetSavedSearchJobHistoryInput(),
                output=GetSavedSearchJobHistoryOutput())

    def run(self, params={}):
        saved_search_name = params.get("saved_search_name")

        try:
            saved_search = self.connection.client.saved_searches[saved_search_name]
            history = saved_search.history()  # Returns a list of Job objects
        except KeyError as error:
            self.logger.error(error)
            raise

        history_json = json.loads(
            json.dumps(history, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        )

        return {"job_history": history_json}

    def test(self):
        return {}
