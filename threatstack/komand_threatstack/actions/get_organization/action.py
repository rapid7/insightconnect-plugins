import komand
from .schema import GetOrganizationInput, GetOrganizationOutput
# Custom imports below


class GetOrganization(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_organization',
                description='Get organization',
                input=GetOrganizationInput(),
                output=GetOrganizationOutput())

    def run(self, params={}):
        organizations = self.connection.client.organizations.list()

        organization = None
        while True:
            try:
                org = next(organizations)
                if org.get('id') == params.get('organization_id'):
                    organization = org
                    break
            except TypeError:
                raise Exception('No organizations found')
            except StopIteration:
                break

        if organization is None:
            raise Exception('Organization not found')

        return {'organization': organization}


    def test(self):
        '''Test action'''
        self.logger.info('Unable to test request, proceeding with example output')
        return { 'organization': {} }
