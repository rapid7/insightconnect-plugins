import komand
from .schema import ReportIpInput, ReportIpOutput
# Custom imports below
from komand.exceptions import PluginException
import json
import requests
import logging
logging.getLogger('requests').setLevel(logging.WARNING)


class ReportIp(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='report_ip',
                description='Report an abusive IP address',
                input=ReportIpInput(),
                output=ReportIpOutput())

    def run(self, params={}):
        try:
            # https://www.abuseipdb.com/report/json?key=[API_KEY]&category=[CATEGORIES]&comment=[COMMENT]&ip=[IP]
            url = '{base}/{endpoint}/json?key={key}&category={category}&ip={ip}'.format(
                base=self.connection.base, 
                endpoint='report',
                key=self.connection.api_key,
                category=params.get('categories'),
                ip=params.get('address'),
            )

            comment = params.get('comment')
            if comment:
                if len(comment) > 0:
                   # Comment provided
                    url = '{}&comment={}'.format(url, comment)

            r = requests.get(url)
            # Not using r.raise_for_status() since we get useful JSON information on an API 4**
            out = r.json()
        except Exception as e:
            self.logger.error(e)
            raise

        try:
            if isinstance(out, list):
                error = out[0]
                if isinstance(error, dict):
                    if error['id']:
                        msg = '{}: {}: {}'.format(error.get('id'), error.get('title'), error.get('detail'))
                        raise PluginException(cause='Received an error response from AbuseIPDB.', assistance=msg)
        except KeyError:
            # All good, no error because 'id' key is not present
            self.logger.info('No errors')

        return out
