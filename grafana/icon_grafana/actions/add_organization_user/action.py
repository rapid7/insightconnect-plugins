import komand
from .schema import AddOrganizationUserInput, AddOrganizationUserOutput
# Custom imports below


class AddOrganizationUser(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_organization_user',
                description='Add a global user to the organization',
                input=AddOrganizationUserInput(),
                output=AddOrganizationUserOutput())

    def run(self, params={}):
        organization_id = params.get('organization_id', -1)
        if organization_id != -1:
            urlparts = ('orgs', organization_id, 'users')
        else:
            urlparts = ('org', 'users')

        response = self.connection.request(
            'POST', urlparts,
            json={
                'loginOrEmail': params.get('login_or_email'),
                'role': params.get('role')
            }
        )
        message = response.json().get('message', '')
        if response.ok:
            return {
                'success': True,
                'message': message
            }
        else:
            self.logger.error('Grafana API: ' + message)
            response.raise_for_status()

    def test(self):
        return self.connection.test()
