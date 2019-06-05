import komand
from .schema import CheckIpInput, CheckIpOutput
# Custom imports below
import requests
import logging
logging.getLogger('requests').setLevel(logging.WARNING)


class CheckIp(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='check_ip',
                description='Look up an IP address in the database',
                input=CheckIpInput(),
                output=CheckIpOutput())

    def run(self, params={}):
        try:
            # https://www.abuseipdb.com/check/[IP]/json?key=[API_KEY]&days=[DAYS][&verbose]
            url = '{base}/{endpoint}/{ip}/json?key={key}&days={days}'.format(
                base=self.connection.base, 
                endpoint='check',
                ip=params.get('address'),
                key=self.connection.api_key,
                days=params.get('days', '30')
            )

            if params.get('verbose') == True: 
                # Verbose mode selected
                url = '{}&verbose'.format(url)

            r = requests.get(url)
            # Not using r.raise_for_status() since we get useful JSON information on an API 4**
            out = r.json()
        except Exception as e:
            self.logger.error(e)
            raise

        try:
            if isinstance(out, list):

                try:
                    error = out[0]
                except IndexError:
                    self.logger.info('No items in list')

                try:
                    if isinstance(error, dict):
                        # If the id key is present, an error has occurred
                        if error['id']:
                            msg = '{}: {}: {}'.format(error.get('id'), error.get('title'), error.get('detail'))
                            self.logger.error(msg)
                            return error
                # UnboundLocalError is raised if variable error is not set
                # Error will not be set if out[0] doesn't exist per the catching of the IndexError exception above
                except UnboundLocalError:
                    self.logger.info('No error')
                      
        except KeyError:
            # All good, no error because 'id' key is not present
            self.logger.info('No errors')

        if len(out) > 0:
            found = True
        else:
            found = False

        return { 'list': out, 'found': found }

    def test(self):
        try:
            # https://www.abuseipdb.com/check/[IP]/json?key=[API_KEY]&days=[DAYS][&verbose]
            url = '{base}/{endpoint}/{ip}/json?key={key}&days={days}'.format(
                base=self.connection.base, 
                endpoint='check',
                ip='8.8.8.8',
                key=self.connection.api_key,
                days='30'
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

        return { 'list': out, 'found': True }
