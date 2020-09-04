import komand
from .schema import SearchInput, SearchOutput, Input, Output, Component
# Custom imports below
import json
from datetime import datetime
from komand.exceptions import PluginException
from typing import Optional


class Search(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='search',
            description=Component.DESCRIPTION,
            input=SearchInput(),
            output=SearchOutput())

    def run(self, params={}):
        search_timeframe = params.get(Input.SEARCH_TIMEFRAME)
        if search_timeframe:
            parse_search = self.parse_search_timeframe(search_timeframe)
            result = self.connection.client.jobs.oneshot(
                params.get(Input.QUERY),
                count=params.get(Input.COUNT),
                output_mode="json",
                earliest_time=parse_search["start_time"],
                latest_time=parse_search["end_time"]
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
    def parse_search_timeframe(search_timeframe: Optional[str]) -> dict:
        datetime_format = "%Y-%m-%dT%H:%M:%S"
        split_search_timeframe = search_timeframe.split("-")
        if not split_search_timeframe[0].isdigit():
            raise PluginException(
                cause="Invalid search start timestamp.",
                assistance="Start time should only be a number."
            )
        start_time = datetime.fromtimestamp(int(split_search_timeframe[0])).strftime(datetime_format)
        if len(split_search_timeframe) > 1:
            if not split_search_timeframe[1].isdigit():
                raise PluginException(
                    cause="Invalid search end timestamp.",
                    assistance="End time should only be a number."
                )
            end_time = datetime.fromtimestamp(int(split_search_timeframe[1])).strftime(datetime_format)
        else:
            end_time = datetime.now().strftime(datetime_format)

        return {
            "start_time": start_time,
            "end_time": end_time
        }
