import komand
from .schema import ResolveApprovalRequestInput, ResolveApprovalRequestOutput, Input
# Custom imports below
import requests
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

        statuses = {
            "Submitted": 1,
            "Open": 2,
            "Closed": 3
        }

        approval_request_id = params.get(Input.APPROVAL_REQUEST_ID)
        desired_resolution = params.get(Input.RESOLUTION)
        status_ = params.get(Input.STATUS)

        desired_resolution_code = resolutions.get(desired_resolution, 0) # Not resolved
        desired_status_code = statuses.get(status_, 1) # Submitted

        self.logger.info("Updating approval request...")
        self.logger.info(f"Resolution Code: {desired_resolution_code}")
        self.logger.info(f"Status Code: {desired_status_code}")

        data = {
            "resolution": desired_resolution_code,
            "status": desired_status_code
        }

        self.logger.info("Payload: ")
        self.logger.info(data)

        api_endpoint = f'/api/bit9platform/v1/approvalRequest/{approval_request_id}'
        url = self.connection.host + api_endpoint

        self.logger.info(f"Sending to: {url}")

        r = self.connection.session.put(url, data=json.dumps(data), verify=self.connection.verify)

        try:
            r.raise_for_status()
        except requests.HTTPError as e:
            self.logger.error(f"Resolve Approval Request Failed with status code: {r.status_code}")
            self.logger.error(f"Request returned was: {r.text}")
            raise Exception(f'HTTPError: {r}')

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
