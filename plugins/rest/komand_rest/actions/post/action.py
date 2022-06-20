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
        switch_ONoff = check_headers_for_urlencoded(headers)

        body = params.get(Input.BODY, {})
        body = convert_body_for_urlencoded(headers, body)

        body = convert_body_for_urlencoded(headers, body)

        response = self.connection.api.call_api(
            method="POST",
            path=params.get(Input.ROUTE),
            data=body,
            headers=headers,
        )
        # x = ""
        # for key, value in headers.items():
        #
        #     if key.lower() == "content-type" and value.lower() == "application/x-www-form-urlencoded":
        #         x += value.lower()
        #         print("\n\n\nXXXXX: ", x)
        #
        # args = {'method': 'POST', "path": params.get(Input.ROUTE), 'json_data': body, 'headers': headers}
        # args2 = {'method': 'POST', "path": params.get(Input.ROUTE), 'data': body, 'headers': headers}
        # if x == 'application/x-www-form-urlencoded':
        #     response = self.connection.api.call_api(
        #         *args
        #         # method="POST",
        #         # path=params.get(Input.ROUTE),
        #         # json_data=body,
        #         # headers=headers,
        #     )
        # else:
        #     response = self.connection.api.call_api(
        #         *args2
        #         # method="POST",
        #         # path=params.get(Input.ROUTE),
        #         # json_data=body,
        #         # headers=headers,
        #     )

        return {
            Output.BODY_OBJECT: Common.body_object(response),
            Output.BODY_STRING: response.text,
            Output.STATUS: response.status_code,
            Output.HEADERS: Common.copy_dict(response.headers),
        }
