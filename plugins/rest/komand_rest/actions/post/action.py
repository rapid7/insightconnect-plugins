import insightconnect_plugin_runtime
from .schema import PostInput, PostOutput, Component, Input, Output

# Custom imports below
from komand_rest.util.util import Common
from komand_rest.util.util import convert_body_for_urlencoded


class Post(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="post", description=Component.DESCRIPTION, input=PostInput(), output=PostOutput()
        )

    def run(self, params={}):
        headers = params.get(Input.HEADERS, {})

        body = params.get(Input.BODY, {})

        if check_headers_for_urlencoded(headers):
            body = convert_body_for_urlencoded(headers, body)
            kwargs = {"method": "POST", "path": params.get(Input.ROUTE), "data": body, "headers": headers}
        else:
            kwargs = {"method": "POST", "path": params.get(Input.ROUTE), "json_data": body, "headers": headers}

        response = self.connection.api.call_api(**kwargs)

        return {
            Output.BODY_OBJECT: Common.body_object(response),
            Output.BODY_STRING: response.text,
            Output.STATUS: response.status_code,
            Output.HEADERS: Common.copy_dict(response.headers),
        }
