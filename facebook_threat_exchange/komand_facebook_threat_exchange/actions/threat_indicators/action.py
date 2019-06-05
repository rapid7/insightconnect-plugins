import komand
from .schema import ThreatIndicatorsInput, ThreatIndicatorsOutput
# Custom imports below
import requests
from urllib.parse import urlencode


class ThreatIndicators(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='threat_indicators',
                description='Searching for indicators of compromise stored in ThreatExchange',
                input=ThreatIndicatorsInput(),
                output=ThreatIndicatorsOutput())

    def run(self, params={}):
        query_params = {}
        # filter through key:values to get non-empty strings
        for param in params:
            if params.get(param):
                query_params[param] = params[param]
        self.logger.info(query_params)
        try:
            auth_url = "https://graph.facebook.com/v2.11/threat_indicators?access_token={}|{}&".format(self.connection.appid,
                                                                                                      self.connection.appsecret)
            query_url = auth_url + urlencode(query_params)
            response = requests.get(query_url)
            data = response.json()
            return{"data": data["data"],"paging":data["paging"]}
        except:
            self.logger.error("An error has occurred while retrieving threat indicators")
            raise

    def test(self):
        try:
            app_id = self.connection.appid
            app_secret = self.connection.appsecret
            type_ = 'IP_ADDRESS'
            text = ''
            query_params = urlencode({
                'access_token': app_id + '|' + app_secret,
                'type': type_,
                'text': text
            })
            url = "https://graph.facebook.com/v2.8/threat_indicators?"
            response = requests.get(url + query_params)
            data = response.json()
            return {"data": data["data"], "paging": data["paging"]}
        except:
            self.logger.error("An error has occurred while testing indicators method")
            raise

