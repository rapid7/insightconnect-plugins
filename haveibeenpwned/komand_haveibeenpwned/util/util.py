import requests
import time
import random
from komand_haveibeenpwned.util.log_helper import LogHelper


class HaveIBeenPwned(object):

    _HEADERS = {'User-Agent': "Rapid7 InsightConnect", 'Accept': "application/vnd.haveibeenpwned.v2+json"}

    def __init__(self, logger=None):
        if logger:
            self.logger = logger
        else:
            self.logger = LogHelper().logger
        self._retries = 0


    def get_request(self, url: str, key: str, params=None, max_attempts=2) -> list:
        """
        :param url: specifies which haveibeenpwned api call is used
        :param params: used to filter searches
        :param max_attempts: how many times the plugin will retry if it receives a 429 error
        :return: A boolean value 'found' for results and the results if found is True
        """
        self._HEADERS["hibp-api-key"] = key
        try:
            response = requests.get(url=url, headers=self._HEADERS, params=params)
        except requests.RequestException as e:
            self.logger.error(e)
            raise
        if response.status_code == 200:  # 200 Results found
            response_json = response.json()
            time.sleep(2)
            return response_json
        elif response.status_code == 404:  # 404 Results were not found
            time.sleep(2)
            return []
        elif response.status_code == 429:  # too many requests from your IP
            if 'Retry-After' in response.headers:
                retry = response.headers['Retry-After']
                # HIBP recommendation on adding an additional 100 millisecond delay between requests
                self.logger.info('Too many requests. The rate limit has been exceeded.'
                                 ' Will retry after back off of: {0} sec'.format(retry))
                time.sleep(retry+.100)
                return self.get_request(url, params, max_attempts=0)  # Retry get_request
            else:
                # Just in case we don't get a Retry-After in the header
                if max_attempts > 0:
                    range_increase = 2**self._retries
                    self._retries = self._retries+1
                    back_off = random.randrange(3, 5+range_increase)  # set random time to wait
                    self.logger.info('Too many requests. The rate limit has been exceeded.'
                                     ' Will retry after back off of: {0} sec'.format(back_off))
                    time.sleep(back_off)  # Wait to slow down request rate
                    return self.get_request(url, params, max_attempts=max_attempts - 1)  # Retry get_request
            raise Exception('Too many requests. The rate limit has been exceeded. Back off has failed.'
                                ' Please run fewer workflows with the Have I been Pwned plugin')
        elif response.status_code == 503:  # DDOS protection has flagged your IP for possible abuse
            raise Exception('Warning: HTTP 503 status code received.'
                            ' Have I Been Pwned has flagged this IP address as possibly abusive,'
                            ' and issued a 24-hour ban. Please discontinue use of the plugin for 24 hours'
                            ' and try again. If the issue persists, contact support.')
        else:
            self.logger.error('An unknown error occurred status code: {0}'.format(response.status_code))
            raise Exception('{0} error'.format(response.status_code))


    def get_password(self, hash_start: str) -> list:
        """
        :param hash_start: The first 5 characters of a SHA1 hash
        :return: A list of hashes that match the hash_start param
        """
        BASE_URl = 'https://api.pwnedpasswords.com/range/'

        url = BASE_URl + hash_start
        try:
            response = requests.get(url)
        except requests.RequestException as e:
            self.logger.error(e)
            raise
        hash_list = response.text.splitlines()
        hash_list = [hash_start + hash_ for hash_ in hash_list]
        hash_list = [hash_[:40] for hash_ in hash_list]
        return hash_list
