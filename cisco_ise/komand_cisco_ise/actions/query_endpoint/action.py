import komand
from .schema import QueryEndpointInput, QueryEndpointOutput
# Custom imports below


class QueryEndpoint(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='query_endpoint',
                description='Query an endpoint for more information',
                input=QueryEndpointInput(),
                output=QueryEndpointOutput())

    def run(self, params={}):
        hostname = params.get('hostname')

        result = self.connection.ers.get_endpoint_by_name(hostname)
        try:
            if result == "Not Found":
                self.logger.error("Endpoint was not found")
                return {'ers_endpoint': {}}
            results = result['ERSEndPoint']
        except KeyError:
            self.logger.error('No endpoint key in results, ' + result)
            raise
        except Exception as e:
            self.logger.error(e)
            self.logger.error('Query results, ' + result)
            self.logger.error('Hostname, ' + hostname)
            raise

        return {'ers_endpoint': results}

    def test(self):
        test = self.connection.ers.get_endpoint()
        return {'endpoint_list': test}
