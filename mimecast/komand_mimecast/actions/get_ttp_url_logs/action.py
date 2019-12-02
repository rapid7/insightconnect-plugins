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

        data = {'route': route, 'scanResult': scan_result}
        if to_:
            data['to'] = to_
        if from_:
            data['from'] = from_

        # Mimecast request
        mimecast_request = util.MimecastRequests()
        response = mimecast_request.mimecast_post(url=url, uri=GetTtpUrlLogs._URI,
                                                  access_key=access_key, secret_key=secret_key,
                                                  app_id=app_id, app_key=app_key, data=data)

        try:
            if url_to_filter:
                output = list()
                for log in response['data'][0]['clickLogs']:
                    if re.search(r'{}'.format(url_to_filter), log['url']):
                        output.append(log)
            else:
                output = response['data'][0]['clickLogs']
        except (KeyError, IndexError):
            self.logger.error(response)
            raise PluginException(cause='Unexpected output format.',
                                  assistance='The output from Mimecast was not in the expected format. Please contact support for help.',
                                  data=response)

        return {Output.CLICK_LOGS: output}
