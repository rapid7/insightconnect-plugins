import komand
from .schema import QueryInput, QueryOutput
# Custom imports below
import requests


class Query(komand.Action):
    
    def __init__(self):
        super(self.__class__, self).__init__(
                name='query',
                description='Query for observables',
                input=QueryInput(),
                output=QueryOutput())

    def run(self, params={}):
        url = '{}/{}'.format(self.connection.url, 'observables')
        headers = {
            "Authorization": "Token token={}".format(self.connection.api_token),
            "Accept": "application/vnd.cif.v2+json",
            "Content-Type": "application/json"
        }
        l = []

        # Normalize input parameters
        nolog = str(1) if params.get('nolog') == True else str(0)
        params['nolog'] = nolog
        if params.get('protocol') == "all": del params['protocol']
        if params.get('otype') == "all": del params['otype']
        for k in list(params.keys()):
            if not params[k]:
                del params[k]

        for i in params.keys():
            l.append(i)

        self.logger.info('Inputs: %s', l)

        if l:
            url = '{}{}'.format(url, '?')
            for opt in l:
                # Debugging
                # self.logger.info(url)
                url = '{}{}={}&'.format(url, opt, params.get(opt))
            url = url.rstrip('&')
        self.logger.info(url)

        try:
            r = requests.get(url, headers=headers, verify=self.connection.verify)
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            self.logger.error("HTTP error occurred. Error: " + str(e))
            raise
        except requests.exceptions.ConnectionError as e:
            self.logger.error("A network problem occurred. Error: " + str(e))
            raise
        except requests.exceptions.Timeout as e:
            self.logger.error("Timeout occurred. Error: " + str(e))
            raise
        except requests.exceptions.TooManyRedirects as e:
            self.logger.error("Too many redirects! Error: " + str(e))
            raise
        except Exception as e:
            self.logger.error("Error: " + str(e))
            raise

        # Debugging
        # self.logger.info(r.request.headers)
        data = r.json()
        mod_data = []
        for item in data:
            if "confidence" in item:
                item["confidence"] = float(item["confidence"])
            if isinstance(item["application"], str):
                format_app = list(); format_app.append(item["application"]); item["application"] = format_app
            mod_data.append(item)
        result = mod_data

        ## Remove None types to avoid schema failure
        # Iterate over list
        for obj in result:
            # Iterate over dict keys
            for k in obj:
                if obj[k] is None:
                    obj[k] = "None"

        return {'query': result}

    def test(self):
        url = '{}/{}'.format(self.connection.url, 'ping')
        headers = {
          "Authorization":"Token token={}".format(self.connection.api_token),
          "Accept": "application/vnd.cif.v2+json",
          "Content-Type": "application/json"
        }

        try:
            r = requests.get(url, headers=headers, verify=self.connection.verify)
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            self.logger.error("HTTP error occurred. Error: " + str(e))
            raise
        except requests.exceptions.ConnectionError as e:
            self.logger.error("A network problem occurred. Error: " + str(e))
            raise
        except requests.exceptions.Timeout as e:
            self.logger.error("Timeout occurred. Error: " + str(e))
            raise
        except requests.exceptions.TooManyRedirects as e:
            self.logger.error("Too many redirects! Error: " + str(e))
            raise
        except Exception as e:
            self.logger.error("Error: " + str(e))
            raise
        return { 'query': [r.json()] }
