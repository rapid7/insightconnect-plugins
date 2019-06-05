import komand
from .schema import GetPackageDetailsInput, GetPackageDetailsOutput
# Custom imports below


class GetPackageDetails(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_package_details',
                description='Fetch details for the package with the given ID',
                input=GetPackageDetailsInput(),
                output=GetPackageDetailsOutput())

    def run(self, params={}):
        app_id = params.get('app_id')
        package_id = params.get('package_id')

        package = self.connection.api.get_package_details(app_id, package_id)

        return {'package': package}

    def test(self):
        return {}
