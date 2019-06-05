import komand
from .schema import ListRoutesInput, ListRoutesOutput
# Custom imports below


class ListRoutes(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_routes',
                description='Fetch details for all seen routes (matching the provided criteria)',
                input=ListRoutesInput(),
                output=ListRoutesOutput())

    def run(self, params={}):
        app_id = params.get('app_id')
        from_ = params.get('from')
        to = params.get('to')
        per_page = params.get('per_page', 10)
        page = params.get('page', 1)

        routes = self.connection.api.list_routes(
            app_id, from_, to, per_page, page
        )
        if routes is None:
            routes = {'total': 0, 'routes': []}

        return routes

    def test(self):
        return {}
