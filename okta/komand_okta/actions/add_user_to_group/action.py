import komand
from .schema import AddUserToGroupInput, AddUserToGroupOutput, Input, Output, Component
# Custom imports below
import requests
import urllib.parse
from komand_okta.util import helpers


class AddUserToGroup(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='add_user_to_group',
            description=Component.DESCRIPTION,
            input=AddUserToGroupInput(),
            output=AddUserToGroupOutput())

    def run(self, params={}):
        # Get the user by email
        email = params.get(Input.EMAIL)
        group_id = params.get(Input.GROUP_ID)
        okta_url = self.connection.okta_url
        url = requests.compat.urljoin(okta_url, '/api/v1/users/' + urllib.parse.quote(email))

        # Search for the user by email to get the id
        response = self.connection.session.get(url)
        data = response.json()

        if response.status_code != 200:
            self.logger.error('Okta: Lookup User by Email failed: ' + data['errorSummary'])
            return {Output.SUCCESS: False}

        user_id = data['id']

        # Add user to group by id
        url = requests.compat.urljoin(okta_url, f'/api/v1/groups/{group_id}/users/{user_id}')
        response = self.connection.session.put(url)

        return helpers.group_response(response, user_id)
