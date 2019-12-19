import komand
from .schema import DeleteOrganizationUserInput, DeleteOrganizationUserOutput
# Custom imports below


class DeleteOrganizationUser(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_organization_user',
                description='Delete user in actual organization',
                input=DeleteOrganizationUserInput(),
                output=DeleteOrganizationUserOutput())

    def run(self, params={}):
        user_id = params.get('user_id')
        organization_id = params.get('organization_id', -1)
        if organization_id != -1:
            urlparts = ('orgs', organization_id, 'users', user_id)
        else:
            urlparts = ('org', 'users', user_id)

        response = self.connection.request(
            'DELETE', urlparts,
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
