import komand
from .schema import ResolveApprovalRequestInput, ResolveApprovalRequestOutput
# Custom imports below
import json


class ResolveApprovalRequest(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='resolve_approval_request',
                description='Resolve approval request with desired status',
                input=ResolveApprovalRequestInput(),
                output=ResolveApprovalRequestOutput())

    def run(self, params={}):
        resolutions = {
            "Not Resolved": 0,
            "Rejected": 1,
            "Resolved - Approved": 2,
            "Resolved - Rule Change": 3,
            "Resolved - Installer": 4,
            "Resolved - Updater": 5,
            "Resolved - Publisher": 6,
            "Resolved - Other": 7
        }

        approval_request_id = params.get("approval_request_id")
        desired_resolution = params.get("resolution")

        desired_resolution_code = resolutions.get(desired_resolution, 999)

        if desired_resolution_code is 999:
            raise Exception("Invalid resolution selected")

        self.logger.info("Updating approval request...")

        data = {
            "value": {
                "resolution": desired_resolution_code
            }
        }

        url = self.connection.host + '/api/bit9platform/v1/approvalRequest/%s' % approval_request_id
        r = self.connection.session.put(url, json.dumps(data), verify=self.connection.verify)

        try:
            r.raise_for_status()
        except Exception as e:
            self.logger.error(e)
            raise Exception('Run: HTTPError: %s' % r.text)

        result = komand.helper.clean(r.json())

        return {"approval_request": result}

    def test(self):
        url = self.connection.host + "/api/bit9platform/v1/approvalRequest?limit=-1"  # -1 returns just the count (lightweight call)

        request = self.connection.session.get(url=url, verify=self.connection.verify)

        try:
            request.raise_for_status()
        except Exception as e:
            self.logger.error(e)
            raise Exception('Run: HTTPError: %s' % request.text)

        return {}
