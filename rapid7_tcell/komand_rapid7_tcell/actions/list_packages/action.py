import komand
from .schema import ListPackagesInput, ListPackagesOutput
# Custom imports below


class ListPackages(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_packages',
                description='Fetch details for all seen packages (matching the provided criteria)',
                input=ListPackagesInput(),
                output=ListPackagesOutput())

    def run(self, params={}):
        app_id = params.get('app_id')
        from_ = params.get('from')
        to = params.get('to')
        per_page = params.get('per_page', 10)
        page = params.get('page', 1)

        packages = self.connection.api.list_packages(
            app_id, from_, to, per_page, page
        )
        if packages is None:
            packages = {'total': 0, 'packages': []}

        return packages

    def test(self):
        return {}
