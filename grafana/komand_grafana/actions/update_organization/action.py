import komand
from .schema import UpdateOrganizationInput, UpdateOrganizationOutput
# Custom imports below


class UpdateOrganization(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='update_organization',
                description='Update the name of the organization',
                input=UpdateOrganizationInput(),
                output=UpdateOrganizationOutput())

    def run(self, params={}):
        organization_id = params.get('organization_id', -1)
        if organization_id != -1:
            urlparts = ('orgs', organization_id)
        else:
            urlparts = ('org',)

        response = self.connection.request(
            'PUT', urlparts,
            json={'name': params.get('name')}
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
