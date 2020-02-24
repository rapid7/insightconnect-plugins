# Custom imports below
from komand_rest.util.util import Common

import komand
from .schema import PutInput, PutOutput, Input, Output, Component


class Put(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='put',
            description=Component.DESCRIPTION,
            input=PutInput(),
            output=PutOutput())

    def run(self, params={}):
        response = Common.send_request(
            'put',
            params.get(Input.ROUTE),
            params.get(Input.HEADERS, {}),
            self.connection.default_headers,
            self.connection.base_url,
            self.connection.ssl_verify,
            params.get(Input.BODY, {})
        )

        return {
            Output.BODY_OBJECT: response['body_object'],
            Output.BODY_STRING: response['response_text'],
            Output.STATUS: response['status_code'],
            Output.HEADERS: response['resp_headers']
        }
