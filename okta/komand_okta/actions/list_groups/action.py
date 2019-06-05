import komand
from .schema import ListGroupsInput, ListGroupsOutput
# Custom imports below
import requests
import urllib


class ListGroups(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_groups',
                description='List available groups',
                input=ListGroupsInput(),
                output=ListGroupsOutput())

    def run(self, params={}):
        """ Get the user by email """
        query = params.get("query")
        okta_url = self.connection.okta_url

        if query:
            # Query provided
            url = requests.compat.urljoin(okta_url, '/api/v1/groups?q=' + urllib.quote(query))
        else:
            url = requests.compat.urljoin(okta_url, '/api/v1/groups')

        """ Query for groups """
        response = self.connection.session.get(url)

        try:
            data = response.json()
        except ValueError:
            return {'groups': [], 'success': False}

        if response.status_code == 200:

            if len(data) == 0:
                return {'groups': data, 'success': False}

            # Normalize data for easier UX
            for group in data:
                keys = group.pop('profile')
                group['name'] = keys.get('name', 'Unknown')
                group['description'] = keys.get('description', 'Unknown')

            return {'groups': data, 'success': True}
