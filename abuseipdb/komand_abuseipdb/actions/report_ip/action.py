import komand
from .schema import ReportIpInput, ReportIpOutput
# Custom imports below
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
                    self.logger.info('Adding comment')
                    url = '{}&comment={}'.format(url, comment)

            r = requests.get(url)
            # Not using r.raise_for_status() since we get useful JSON information on an API 4**
            out = r.json()
        except Exception as e:
            self.logger.error(e)
            raise

        try:
            self.logger.info(out)
            if isinstance(out, list):
                error = out[0]
                if isinstance(error, dict):
                    if error['id']:
                        msg = '{}: {}: {}'.format(error.get('id'), error.get('title'), error.get('detail'))
                        self.logger.error(msg)
                        return error
        except KeyError:
            # All good, no error because 'id' key is not present
            self.logger.info('No errors')

        return out

    def test(self):
        try:
            url = '{base}/{endpoint}/json?key={key}&category={category}&ip={ip}'.format(
                base=self.connection.base, 
                endpoint='report',
                key=self.connection.api_key,
                category=10,
                # Should return an API error without raising an exception as we don't want to taint the database with false reporting
                ip='1.2.3.4',
            )
            r = requests.get(url)
            # Not using r.raise_for_status() since we get useful JSON information on an API 4**
            out = r.json()
        except Exception as e:
            self.logger.error(e)
            raise

        try:
            self.logger.info(out)
            if isinstance(out, list):
                error = out[0]
                if isinstance(error, dict):
                    if error['id']:
                        msg = '{}: {}: {}'.format(error.get('id'), error.get('title'), error.get('detail'))
                        self.logger.error(msg)
                        return error
        except KeyError:
            # All good, no error because 'id' key is not present
            self.logger.info('No errors')

        return out
