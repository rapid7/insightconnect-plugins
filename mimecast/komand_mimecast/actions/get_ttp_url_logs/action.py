import komand
from .schema import GetTtpUrlLogsInput, GetTtpUrlLogsOutput, Input, Output, Component
# Custom imports below
from komand_mimecast.util import util
from komand.exceptions import PluginException
import re


class GetTtpUrlLogs(komand.Action):
    _URI = '/api/ttp/url/get-logs'

    def __init__(self):
        super(self.__class__, self).__init__(
            name='get_ttp_url_logs',
            description=Component.DESCRIPTION,
            input=GetTtpUrlLogsInput(),
            output=GetTtpUrlLogsOutput())

    def run(self, params={}):
        # Import variables from connection
        url = self.connection.url
        access_key = self.connection.access_key
        secret_key = self.connection.secret_key
        app_id = self.connection.app_id
        app_key = self.connection.app_key

        from_ = params.get(Input.FROM)
        to_ = params.get(Input.TO)
        route = params.get(Input.ROUTE)
        scan_result = params.get(Input.SCAN_RESULT)
        url_to_filter = params.get(Input.URL_TO_FILTER)
        max_pages = params.get(Input.MAX_PAGES, 100)
        page_size = params.get(Input.PAGE_SIZE, 10)

        data = {'route': route, 'scanResult': scan_result}
        if to_:
            data['to'] = to_
        if from_:
            data['from'] = from_

        meta = {
            "pagination": {
                "pageSize": page_size
            }
        }

        if max_pages < 2:
            max_pages = 1

        # Mimecast request
        mimecast_request = util.MimecastRequests()
        responses = []

        for pages in range(max_pages):
            response = mimecast_request.mimecast_post(url=url, uri=GetTtpUrlLogs._URI,
                                                      access_key=access_key, secret_key=secret_key,
                                                      app_id=app_id, app_key=app_key,
                                                      data=data, meta=meta)
            responses.append(response)

            if 'meta' not in response or \
                    'pagination' not in response['meta'] or \
                    'next' not in response['meta']['pagination']:
                break
            meta['pagination']['pageToken'] = response['meta']['pagination']['next']

        try:
            output = list()
            if url_to_filter:
                for response in responses:
                    for log in response['data'][0]['clickLogs']:
                        if re.search(r'{}'.format(url_to_filter), log['url']):
                            output.append(log)
            else:
                for response in responses:
                    output.extend(response['data'][0]['clickLogs'])
        except (KeyError, IndexError):
            self.logger.error(responses)
            raise PluginException(cause='Unexpected output format.',
                                  assistance='The output from Mimecast was not in the expected format. Please contact support for help.',
                                  data=responses)

        return {Output.CLICK_LOGS: output}
