import komand
from .schema import GetOrganizationsInput, GetOrganizationsOutput
# Custom imports below


class GetOrganizations(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_organizations',
                description='Get organizations',
                input=GetOrganizationsInput(),
                output=GetOrganizationsOutput())

    def run(self, params={}):
        organizations = self.connection.client.organizations.list(**params)
        organization_list = []

        while True:
            try:
                org = next(organizations)
                organization_list.append(org)
            except TypeError:
                # Nothing found.
                # Not necessarily an error; could be failed search.
                break
            except StopIteration:
                break

        return {'organizations': organization_list, 'count': len(organization_list)}
