import komand
from .schema import SearchInput, SearchOutput
# Custom imports below
from komand.exceptions import PluginException
import re
import datetime


class Search(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='search',
                description='The pattern search functionality in Investigate uses regular expressions (RegEx) to search against the Investigate database',
                input=SearchInput(),
                output=SearchOutput())

    def run(self, params={}):
        expression = params.get('expression')
        start = params.get('start')
        limit = params.get('limit', None)
        include_category = params.get('include_category', False)
        
        if not limit or limit == 0:
            limit = 1000
        
        if not include_category or include_category == None:
            include_category = False

        nr = re.search(r'[+-]?\d+', start)
        if not nr:
            raise PluginException(cause='An invalid start time was provided.', assistance='For more information, see: https://docs.umbrella.com/investigate-api/docs/pattern-search-1#section-parameters-for-input')

        if "sec" in start:
            start = datetime.timedelta(seconds=int(nr.group()))
        elif "min" in start:
            start = datetime.timedelta(minutes=int(nr.group()))
        elif "hour" in start:
            start = datetime.timedelta(hours=int(nr.group()))
        elif "day" in start:
            start = datetime.timedelta(days=int(nr.group()))
        else:
            start = datetime.timedelta(weeks=int(nr.group()))

        try:
            search = self.connection.investigate.search(expression, start=start, limit=limit, include_category=include_category)
        except Exception as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=e)
        return search

    def test(self):
        return {"expression": "", "limit": 0, "matches": [], "moreDataAvailable": False, "totalResults": 0}
