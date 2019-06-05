import komand
from .schema import PostInput, PostOutput
# Custom imports below
from komand_rest.util.util import Common
import requests


class Post(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='post',
                description='Make a POST request',
                input=PostInput(),
                output=PostOutput())

    def run(self, params={}):
        route = params.get("route")
        headers = params.get("headers", {})
        body = params.get("body", {})

        req_headers = Common.merge_dicts(self.connection.default_headers, headers)
        url = requests.compat.urljoin(self.connection.base_url, route)
        response = requests.post(url, headers=req_headers, json=body, verify=self.connection.ssl_verify)
        body_object = {}
        try:
            body_object = response.json()
        except ValueError:
            """ Nothing? We don't care if it fails, that could be normal """

        resp_headers = Common.copy_dict(response.headers)
        return {
            'body_object': body_object,
            'body_string': response.text,
            'status': response.status_code,
            'headers': resp_headers,
        }

    def test(self):
        # TODO: Implement test function
        return {}
