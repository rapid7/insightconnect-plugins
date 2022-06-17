import insightconnect_plugin_runtime
from .schema import PostInput, PostOutput, Component, Input, Output

# Custom imports below
from komand_rest.util.util import Common
from komand_rest.util.util import convert_body_for_urlencoded, check_headers_for_urlencoded


class Post(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="post", description=Component.DESCRIPTION, input=PostInput(), output=PostOutput()
        )

    def run(self, params={}):
        headers = params.get(Input.HEADERS, {})
        switch_ONoff = check_headers_for_urlencoded(headers)
        print("\n\n\nSWITCH: ", switch_ONoff)

        body = params.get(Input.BODY, {})
        body = convert_body_for_urlencoded(headers, body)
        print("\n\n\nBODY: ", body, "\nTYPE OF: ", type(body))

        args = {"method": "POST", "path": params.get(Input.ROUTE), "data": body, "headers": headers}
        args2 = {"method": "POST", "path": params.get(Input.ROUTE), "json_data": body, "headers": headers}

        if switch_ONoff:
            response = self.connection.api.call_api(**args)
        else:
            response = self.connection.api.call_api(**args2)

        return {
            Output.BODY_OBJECT: Common.body_object(response),
            Output.BODY_STRING: response.text,
            Output.STATUS: response.status_code,
            Output.HEADERS: Common.copy_dict(response.headers),
        }
