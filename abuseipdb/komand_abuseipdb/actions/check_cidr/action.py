import komand
from .schema import CheckCidrInput, CheckCidrOutput
# Custom imports below
import requests
import logging
logging.getLogger('requests').setLevel(logging.WARNING)


class CheckCidr(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='check_cidr',
                description='Look up a CIDR address in the database',
                input=CheckCidrInput(),
                output=CheckCidrOutput())

    def run(self, params={}):
        try:
            url = '{base}/{endpoint}/json?key={key}&network={cidr}&days={days}'.format(
                base=self.connection.base, 
                endpoint='check-block',
                key=self.connection.api_key,
                cidr=params.get('cidr'),
                days=params.get('days', '30')
            )
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
                        self.logger.error(msg)
                        return error
        except KeyError:
            # All good, no error because 'id' key is not present
            self.logger.info('No errors')

        return out

    def test(self):
        try:
            url = '{base}/{endpoint}/json?key={key}&network=207.126.144.0/20&days=30'.format(
                base=self.connection.base, 
                endpoint='check-block',
                key=self.connection.api_key,
            )
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
                        self.logger.error(msg)
                        return error
        except KeyError:
            # All good, no error because 'id' key is not present
            self.logger.info('No errors')

        return out
