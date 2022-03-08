import insightconnect_plugin_runtime
from .schema import CreateExceptionInput, CreateExceptionOutput, Component, Input, Output

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests
from komand_rapid7_insightvm.util.util import convert_date_to_iso8601


class CreateException(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_exception",
            description=Component.DESCRIPTION,
            input=CreateExceptionInput(),
            output=CreateExceptionOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        payload = {}
        scope = {}
        submit = {}
        scope["id"] = params.get(Input.SCOPE)
        scope["type"] = params.get(Input.TYPE)
        if scope["type"] == "Instance":
            if params.get(Input.KEY, "") != "":
                scope["key"] = params.get(Input.KEY)
            if params.get(Input.PORT, 0) != 0:
                scope["port"] = params.get(Input.PORT)
        scope["vulnerability"] = params.get(Input.VULNERABILITY)
        submit["reason"] = params.get(Input.REASON, "Other")
        submit["comment"] = params.get(Input.COMMENT, "Created with InsightConnect")

        payload["scope"] = scope
        payload["submit"] = submit
        expires = params.get(Input.EXPIRATION, "")
        if expires:
            payload["expires"] = convert_date_to_iso8601(expires)

        payload["state"] = "Under Review"

        endpoint = endpoints.VulnerabilityException.vulnerability_exceptions(self.connection.console_url)
        response = resource_helper.resource_request(endpoint=endpoint, method="post", payload=payload)
        return {Output.LINKS: response.get("links", []), Output.ID: response.get("id")}
