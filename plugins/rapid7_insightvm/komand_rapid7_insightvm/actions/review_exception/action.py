import insightconnect_plugin_runtime
from .schema import ReviewExceptionInput, ReviewExceptionOutput, Component

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class ReviewException(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="review_exception",
            description=Component.DESCRIPTION,
            input=ReviewExceptionInput(),
            output=ReviewExceptionOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)

        translate = {"Approved": "approve", "Rejected": "reject"}

        id_ = params.get("exception")
        review = translate.get(params.get("review"))
        comment = params.get("comment")

        payload = {"rawbody": comment}

        endpoint = endpoints.VulnerabilityException.vulnerability_exception_status(
            self.connection.console_url, id_, review
        )
        response = resource_helper.resource_request(endpoint=endpoint, method="post", payload=payload)
        return response
