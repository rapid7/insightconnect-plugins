import komand
from .schema import LookupInput, LookupOutput
# Custom imports below
import requests


class Lookup(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='lookup',
                description='Lookup intelligence information',
                input=LookupInput(),
                output=LookupOutput())

    def run(self, params={}):
        url = 'https://ipintel.io'
        lstRet = []
        ipList = ''
        try:
            for ip in params.get('addresses'):
                ipList = ipList + ip + ' '
            client = requests.session()
            client.get(url)
            csrftoken = client.cookies['csrftoken']
            geolookuponly = params.get('geolookup')
            stealth = params.get('stealth')
            data = {'geolookuponly': str(geolookuponly).lower(), 'iplist': ipList, 'stealth': str(stealth).lower(), 'csrfmiddlewaretoken': csrftoken}
            headers = {
              'User-Agent': 'Komand',
              'Referer': url
            }
            r = client.post(url + "/process", data=data, headers=headers)
            requestId = r.json()['request_id']
            r = client.get(url+'/status/'+requestId)
            if 'lookup_results' not in r.json():
                raise Exception('IPIntel did not return the expected data')
            for var in r.json()['lookup_results']:
                intel={
                    'ip': var['ip'],
                    'info': var['info'],
                    'threats': [] if geolookuponly == True and stealth == False else var['threats'],
                    'warnings': var['warnings'],
                    'cached': var['cached'],
                    'country': var['country'],
                    'hostname': var['hostname'],
                    'geoonly': str(var['geoonly']),
                    'lookup_time': str(var['lookup_time']),
                    'longitude': str(var['longitude']),
                    'stealth': str(var['stealth']),
                    'references': [] if geolookuponly == True and stealth == False else var['references'],
                    'location': var['location'],
                    'country_iso': var['location'],
                    'latitude': str(var['latitude']),
                    'org': var['org'],
                    'first_seen': '' if geolookuponly == True and stealth == False else var['first_seen'],
                    'city': '' if geolookuponly == False and stealth == True else var['city'],
                    'last_seen': '' if geolookuponly == True and stealth == False else var['last_seen'],
                    'permalink': r.json()["permalink"]
                }
                lstRet.append(intel)

            return { 'result': lstRet }

        except requests.exceptions.HTTPError as e:
            self.logger.error("An HTTP error occurred. Error: " + str(e))
        except requests.exceptions.ConnectionError as e:
            self.logger.error("A connection error occurred. Error: " + str(e))
        except requests.exceptions.Timeout as e:
            self.logger.error("A timeout occurred. Error: " + str(e))
        except requests.exceptions.TooManyRedirects as e:
            self.logger.error("Too many redirects. Error: " + str(e))
        except Exception as e:
            self.logger.error('An unknown error occurred. Error: ' + str(e))

    def test(self):
        url = 'https://ipintel.io'
        try:
            r = requests.get(url)
            if r.status_code != 200:
                self.logger.error('Web request to https://ipintel.io returned a %d', r.status_code)
        except:
            self.logger.error('Request to https://ipintel.io failed')
            raise
        return {}
