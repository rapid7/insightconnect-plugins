import komand
from .schema import CheckIpInput, CheckIpOutput
# Custom imports below
from komand.exceptions import PluginException
import json
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
        except json.decoder.JSONDecodeError:
            raise PluginException(cause='Received an unexpected response from AbuseIPDB.', 
                                  assistance="(non-JSON or no response was received). Response was: %s" % r.text)
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
                            raise PluginException(cause='Received an error response from AbuseIPDB.', assistance=msg)
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
