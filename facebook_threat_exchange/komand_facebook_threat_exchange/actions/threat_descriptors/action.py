import komand
from .schema import ThreatDescriptorsInput, ThreatDescriptorsOutput
# Custom imports below
import requests
from urllib.parse import urlencode


class ThreatDescriptors(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='threat_descriptors',
                description='Enables searching for subjective opinions on indicators of compromise stored in ThreatExchange',
                input=ThreatDescriptorsInput(),
                output=ThreatDescriptorsOutput())

    def run(self, params={}):
        query_params = {}
        # filter through key:values to get non-empty strings
        for param in params:
            if params.get(param):
                query_params[param] = params[param]
        self.logger.info(query_params)
        try:
            auth_url = "https://graph.facebook.com/v2.8/threat_descriptors?access_token={}|{}&".format(
                self.connection.appid,
                self.connection.appsecret)
            query_url = auth_url + urlencode(query_params)
            self.logger.info(query_url)
            response = requests.get(query_url)
            data = response.json()
            return {"data": data["data"], "paging": data["paging"]}
        except:
            self.logger.error("An error has occurred while testing indicators method")
            raise

    def test(self):
        try:
            app_id = self.connection.appid
            app_secret = self.connection.appsecret
            text = 'proxy'
            query_params = urlencode({
                'access_token': app_id + '|' + app_secret,
                'text': text
            })
            auth_url = "https://graph.facebook.com/v2.8/threat_descriptors?"
            query_url = auth_url + query_params
            self.logger.info(query_url)
            response = requests.get(query_url)
            data = response.json()
            return {"data": data["data"], "paging": data["paging"]}
        except:
            self.logger.error("An error has occurred while testing indicators method")
            raise
