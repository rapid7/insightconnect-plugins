import komand
from .schema import SearchInput, SearchOutput
# Custom imports below
import time

TWENTY_FOUR_HOURS_AGO = 86400000

class states:
    DONE = 'DONE GATHERING RESULTS'
    CANCELLED = 'CANCELLED'

class Search(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='search',
                description='Run a search',
                input=SearchInput(),
                output=SearchOutput())

    def run(self, params={}):
        params['timeout'] = params.get('timeout') or 60
        params['from_time'] = params.get('from_time') \
           or str(int(time.time() * 1000) - TWENTY_FOUR_HOURS_AGO)

        params['to_time'] = params.get('to_time') \
           or str(int(time.time() * 1000))

        params['timezone'] = params.get('timezone') or 'UTC'

        sj = self.connection.client.search_job(
                params['query'], 
                params['from_time'], 
                params['to_time'], 
                params['timezone'])

        self.logger.info("Running query: %s", params)

        delay = 2 
        status = self.connection.client.search_job_status(sj)

        while status['state'] != states.DONE:
            self.logger.debug("Running query status: %s", status['state'])

            if status['state'] == states.CANCELLED or delay > params['timeout']:
                break

            time.sleep(delay)
            delay *= 2
            status = self.connection.client.search_job_status(sj)

        page_limit = params.get('page_limit') or 5 
        page_offset = params.get('page_offset') or 0

        offset = page_limit * page_offset

        messages = []
        fields = []
        count = 0
        page_count = 0

        if status['state'] == states.DONE:
            count = status['messageCount']
            limit = count if count < page_limit else page_limit 

            if page_limit > 0:
                page_count = count / page_limit
                if count % page_limit:
                    page_count += 1

            self.logger.debug('Returned results: %s %d', status, count)


            if limit:
                results = self.connection.client.search_job_messages(
                    sj, limit=page_limit, offset=offset)

                if results:
                    fields = results.get('fields')
                    messages = results.get('messages')
   
        return { 
                'messages': messages, 
                'fields': fields,
                'page_count': page_count,
                'total_count': count
                }

    def test(self):
        return {
                'messages': [], 
                'fields': [],
                'page_count': 0,
                'total_count': 0 
               
                } 
