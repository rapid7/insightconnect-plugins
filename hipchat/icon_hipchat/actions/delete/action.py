import komand
from .schema import DeleteInput, DeleteOutput
# Custom imports below
import json
import urllib2
import requests


class Delete(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='delete',
            description='Delete a user',
            input=DeleteInput(),
            output=DeleteOutput())

    def run(self, params={}):
        try:
            server = self.connection.server
            token = self.connection.token

            # add request property
            id_or_email = params.get("id_or_email", "")

            url = server + '/user/' + id_or_email

            # new Request Request
            request = urllib2.Request(url, headers={'Content-Type': 'application/json',
                                                    'Authorization': 'Bearer %s' % token})
            request.get_method = lambda: "DELETE"

            # Call api and response data
            resp = urllib2.urlopen(request)
            status_code = resp.getcode()

            return {'status_code': status_code}

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
