import komand
from .schema import SendPushInput, SendPushOutput, Input, Output, Component
# Custom imports below
import requests

class SendPush(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='send_push',
                description=Component.DESCRIPTION,
                input=SendPushInput(),
                output=SendPushOutput())

    def run(self, params={}):
        self.logger.info("Sending a push verify to %s", params)
        user_id = params.get(Input.USER_ID)
        factor_id = params.get(Input.FACTOR_ID)

        if not user_id or factor_id:
            raise ValueError('user_id and factor_id is required')

        okta_url = self.connection.okta_url
        url = requests.compat.urljoin(okta_url, f'/api/v1/users/{user_id}/factors/{factor_id}/verify')
        response = self.connection.session.post(url)
        if response.status_code == 401:
            self.logger.error('Okta: Invalid token or domain')
        data = response.json()

        for link in data['_links']:
            if link == "poll":
                poll_url = link['poll']['href']

        poll_status = "WAITING"

        while poll_status == "WAITING":
            poll_response = self.connection.session.get(poll_url)
            poll_data = poll_response.json()
            poll_status = poll_data['factor_result']

        return {Output.FACTOR_DATA: poll_data}
