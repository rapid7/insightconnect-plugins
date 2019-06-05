import komand
from .schema import RemoveUserFromGroupInput, RemoveUserFromGroupOutput
# Custom imports below
import requests
import urllib


class RemoveUserFromGroup(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='remove_user_from_group',
                description='Remove a user from an existing group',
                input=RemoveUserFromGroupInput(),
                output=RemoveUserFromGroupOutput())

    def run(self, params={}):
        """ Get the user by email """
        email = params.get("email")
        group_id = params.get("group_id")
        okta_url = self.connection.okta_url

        url = requests.compat.urljoin(okta_url, '/api/v1/users/' + urllib.quote(email))

        """ Search for the user by email to get the id """
        response = self.connection.session.get(url)
        data = response.json()

        if response.status_code != 200:
            self.logger.error('Okta: Lookup User by Email failed: ' + data['errorSummary'])
            return {'success': False}

        userid = data['id']

        """ Remove user from group by id"""
        url = requests.compat.urljoin(okta_url, '/api/v1/groups/' + group_id + '/users/' + userid)
        response = self.connection.session.delete(url)

        try:
            data = response.json()
        except ValueError:
            if response.status_code == 204:
                return {'user_id': userid, 'success': True}
            return {'success': False}

        if 'errorSummary' in data:
            # 405: {u'errorCode': u'E0000022', u'errorSummary': u'The endpoint does not support the provided HTTP method', u'errorLink': u'E0000022', u'errorCauses': [], u'errorId': u'oaexVslu0CIQCWH63QtUs4kSw'}
            self.logger.error(data['errorSummary'])
            raise Exception(data['errorSummary'])

        return {'success': False}
