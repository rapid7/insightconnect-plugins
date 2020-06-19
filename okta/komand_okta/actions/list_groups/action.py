import komand
from .schema import ListGroupsInput, ListGroupsOutput, Input, Output, Component
# Custom imports below
import requests
import urllib.parse
from komand_okta.util.helpers import raise_based_on_error_code

class ListGroups(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='list_groups',
            description=Component.DESCRIPTION,
            input=ListGroupsInput(),
            output=ListGroupsOutput())

    def run(self, params={}):
        """ Get the user by email """
        query = params.get(Input.QUERY)
        okta_url = self.connection.okta_url

        if query:
            # Query provided
            url = requests.compat.urljoin(okta_url, f'/api/v1/groups?q={urllib.parse.quote(query)}')
        else:
            url = requests.compat.urljoin(okta_url, '/api/v1/groups')

        """ Query for groups """
        response = self.connection.session.get(url)

        try:
            data = response.json()
        except ValueError:
            return {Output.GROUPS: [], Output.SUCCESS: False}

        if response.status_code == 200:
            if len(data) == 0:
                return {Output.GROUPS: data, Output.SUCCESS: False}

            # Normalize data for easier UX
            for group in data:
                keys = group.pop('profile')
                group['name'] = keys.get('name', 'Unknown')
                group['description'] = keys.get('description', 'Unknown')

            return {Output.GROUPS: data, Output.SUCCESS: True}
        else:
            raise_based_on_error_code(response=response)

