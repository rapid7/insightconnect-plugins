import komand
from .schema import GetApprovalRequestInput, GetApprovalRequestOutput, Input, Output, Component
# Custom imports below


class GetApprovalRequest(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_approval_request',
                description=Component.DESCRIPTION,
                input=GetApprovalRequestInput(),
                output=GetApprovalRequestOutput())

    def run(self, params={}):
        approval_request_id = params.get(Input.APPROVAL_REQUEST_ID)

        self.logger.info("Getting approval request...")
        self.logger.info(f"Approval Request ID: {approval_request_id}")

        url = self.connection.host + '/api/bit9platform/v1/approvalRequest/%s' % approval_request_id
        r = self.connection.session.get(url, verify=self.connection.verify)

        try:
            r.raise_for_status()
        except requests.HTTPError as e:
            self.logger.error(f"Resolve Approval Request Failed with status code: {r.status_code}")
            self.logger.error(f"Request returned was: {r.text}")
            raise Exception(f'HTTPError: {r}')

        result = komand.helper.clean(r.json())

        return {Output.APPROVAL_REQUEST: result}

