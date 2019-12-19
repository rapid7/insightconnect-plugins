import komand
from .schema import GetOrganizationUsersInput, GetOrganizationUsersOutput
# Custom imports below


class GetOrganizationUsers(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_organization_users',
                description='Get all users within the organization',
                input=GetOrganizationUsersInput(),
                output=GetOrganizationUsersOutput())

    def run(self, params={}):
        organization_id = params.get('organization_id', -1)
        if organization_id != -1:
            urlparts = ('orgs', organization_id, 'users')
        else:
            urlparts = ('org', 'users')

        response = self.connection.request(
            'GET', urlparts,
        )
        if response.ok:
            return {'users': response.json()}
        else:
            self.logger.error('Grafana API: ' + response.json().get('message', ''))
            response.raise_for_status()

    def test(self):
        return self.connection.test()
