import komand
from .schema import SearchInput, SearchOutput, Input, Output, Component
# Custom imports below
import json
from datetime import datetime


class Search(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='search',
            description=Component.DESCRIPTION,
            input=SearchInput(),
            output=SearchOutput())

    def run(self, params={}):
        """Run action"""
        search_timeframe = self.parse_search_timeframe(params.get(Input.SEARCH_TIMEFRAME))
        if search_timeframe:
            result = self.connection.client.jobs.oneshot(
                params.get(Input.QUERY),
                count=params.get(Input.COUNT),
                output_mode="json",
                earliest_time=search_timeframe["start_time"],
                latest_time=search_timeframe["end_time"]
            )
        else:
            result = self.connection.client.jobs.oneshot(
                params.get(Input.QUERY),
                count=params.get(Input.COUNT),
                output_mode="json"
            )
        results = json.loads(result.readall())

        count = 0
        if "results" in results:
            count = len(results["results"])

        return {Output.RESULT: results, Output.COUNT: count}

    @staticmethod
    def parse_search_timeframe(search_timeframe: str) -> dict:
        datetime_format = "%Y-%m-%dT%H:%M:%S"
        if search_timeframe:
            split_search_timeframe = search_timeframe.split("-")
            start_time = datetime.fromtimestamp(int(split_search_timeframe[0])).strftime(datetime_format)
            if len(split_search_timeframe) > 1:
                end_time = datetime.fromtimestamp(int(split_search_timeframe[1])).strftime(datetime_format)
            else:
                end_time = datetime.now().strftime(datetime_format)

            return {
                "start_time": start_time,
                "end_time": end_time
            }

        return {}
