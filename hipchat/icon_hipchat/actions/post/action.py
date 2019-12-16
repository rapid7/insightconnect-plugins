import komand
from .schema import PostInput, PostOutput
# Custom imports below
import json
import urllib2
import requests


class Post(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='post',
            description='Send a message to a room',
            input=PostInput(),
            output=PostOutput())

    def run(self, params={}):
        try:
            server = self.connection.server
            token = self.connection.token
            data = {}

            room_id_or_name = params.get("room_id_or_name", "")
            # add request property
            message = params.get("message", "")
            data["message"] = message

            url = server + '/room/%s/message' % room_id_or_name

            # new Request Request
            request = urllib2.Request(url, data=json.dumps(data), headers={'Content-Type': 'application/json',
                                                                           'Authorization': 'Bearer %s' % token})

            # Call api and response data
            resp = urllib2.urlopen(request)

            # handle decoding json
            try:
                result_dic = json.loads(resp.read())
            except ValueError as e:
                self.logger.error('Decoding JSON Errors:  %s', e)
                raise ('Decoding JSON Errors')

            return result_dic
        # handle exception
        except urllib2.HTTPError as e:
            self.logger.error('HTTPError: %s for %s', str(e.code), url)
            message = json.loads(e.read())["error"]["message"]
            self.logger.error('HTTPError Reason: %s' % message)
            raise Exception(message)
        except urllib2.URLError as e:
            self.logger.error('URLError: %s for %s', str(e.reason), url)
        except Exception:
            import traceback
            self.logger.error('Generic Exception: %s', traceback.format_exc())
        raise Exception('URL Request Failed')

    def test(self):
        http_method = "GET"
        server = self.connection.server
        token = self.connection.token

        #  url test authentication
        url = server + '/room'

        # call request test authentication
        response = requests.request(http_method, url,
                                    headers={'Content-Type': 'application/json', 'Authorization': 'Bearer %s' % token})

        if response.status_code == 401:
            raise Exception('Unauthorized: %s (HTTP status: %s)' % (response.text, response.status_code))
        if response.status_code != 200:
            raise Exception('%s (HTTP status: %s)' % (response.text, response.status_code))

        return {'status_code': response.status_code}
