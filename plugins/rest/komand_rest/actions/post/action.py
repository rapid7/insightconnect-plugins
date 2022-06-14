import insightconnect_plugin_runtime
from .schema import PostInput, PostOutput, Component, Input, Output

# Custom imports below
from komand_rest.util.util import Common
from komand_rest.util.util import convert_dict_body_to_string


class Post(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="post", description=Component.DESCRIPTION, input=PostInput(), output=PostOutput()
        )

    def run(self, params={}):
        headers = params.get(Input.HEADERS, {})
        body = params.get(Input.BODY, {})

        # Support encoding for x-www-form-urlencoded
        for key, value in headers.items():
            if "content-type" in key.lower():
                if "x-www-form-urlencoded" in value:
                    body = convert_dict_body_to_string(body)

        response = self.connection.api.call_api(
            method="POST",
            path=params.get(Input.ROUTE),
            json_data=body,
            headers=headers,
        )

        return {
            Output.BODY_OBJECT: Common.body_object(response),
            Output.BODY_STRING: response.text,
            Output.STATUS: response.status_code,
            Output.HEADERS: Common.copy_dict(response.headers),
        }
