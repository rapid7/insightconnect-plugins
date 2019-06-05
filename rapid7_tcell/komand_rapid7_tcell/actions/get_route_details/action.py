import komand
from .schema import GetRouteDetailsInput, GetRouteDetailsOutput
# Custom imports below


class GetRouteDetails(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_route_details',
                description='Fetch details for the route with the given ID',
                input=GetRouteDetailsInput(),
                output=GetRouteDetailsOutput())

    def run(self, params={}):
        app_id = params.get('app_id')
        route_id = params.get('route_id')

        route = self.connection.api.get_route_details(app_id, route_id)

        return {'route': route}

    def test(self):
        return {}
