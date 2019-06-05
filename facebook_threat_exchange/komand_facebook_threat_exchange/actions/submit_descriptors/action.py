import komand
from .schema import SubmitDescriptorsInput, SubmitDescriptorsOutput
# Custom imports below
import requests
from urllib.parse import urlencode


class SubmitDescriptors(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='submit_descriptors',
                description='Submit data to Facebook\'s graph API.',
                input=SubmitDescriptorsInput(),
                output=SubmitDescriptorsOutput())

    def run(self, params={}):
        query_params = {}
        # filter through key:values to get non-empty pairs
        for param in params:
            if params.get(param):
                query_params[param] = params[param]
        self.logger.info(query_params)
        payload = urlencode(query_params)
        try:
            auth_url = "https://graph.facebook.com/v2.8/threat_descriptors?access_token={}|{}".format(self.connection.appid,
                                                                                                       self.connection.appsecret)
            response = requests.post(url=auth_url, data=payload)
            data = response.json()
            return {"success": data["success"], "id": str(data["id"])}
        except:
            self.logger.error("An error has occurred while retrieving submit descriptor")
            raise

    def test(self):
        try:
            app_id = self.connection.appid
            app_secret = self.connection.appsecret
            type_ = 'CMD_LINE'
            text = "''"
            query_params = urlencode({
                'access_token': app_id + '|' + app_secret,
                'type': type_,
                'text': text
            })
            url = "https://graph.facebook.com/v2.8/threat_descriptors?"
            response = requests.get(url + query_params)
            self.logger.info("Status Code: " + str(response.status_code))
            self.logger.info("Response: " + response.content.decode())
            return {"status": str(response.status_code)}
        except:
            self.logger.error("An error has occurred while retrieving submit descriptor")
            raise
