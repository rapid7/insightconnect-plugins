import komand
from .schema import RemoveFromQuarantineInput, RemoveFromQuarantineOutput
# Custom imports below
import asyncio


class RemoveFromQuarantine(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='remove_from_quarantine',
                description='Remove a host from quarantine',
                input=RemoveFromQuarantineInput(),
                output=RemoveFromQuarantineOutput())

    def run(self, params={}):
        mac_address = params.get('mac_address')

        self.connection.ers.clean_anc_end_point(mac_address=mac_address)
        results = self.connection.ers.get_anc_endpoint()

        try:
            if results['SearchResult']['total'] == 0:
                return {'success': True}
            results = results['SearchResult']['resources']
        except KeyError:
            self.logger.error('Raw results from ANC endpoint query: ' + str(results))
            raise Exception('Results contained improperly formatted data. See log for more details')
        except Exception as e:
            self.logger.error(e)
            self.logger.error('Raw results from ANC endpoint query: ' + str(results))
            raise Exception('Unexpected error. See log for more details')

        try:
            ids = [result["id"] for result in results]
            found = asyncio.run(self.connection.ers.get_anc_endpoints(endpoint_ids=ids))
            for f in [f for f in found if f is not None]:
                if f['ErsAncEndpoint']['macAddress'] == mac_address:
                    self.logger.error(results)
                    raise Exception('{} was not removed. See log for more details'.format(mac_address))
            return {'success': True}
        except KeyError:
            self.logger.error('Raw results from ANC endpoint query: ' + str(results))
            self.logger.error('Raw results from ANC endpoint query on IDs: ' + x)
            raise
        except Exception as e:
            self.logger.error(e)
            self.logger.error('Raw results from ANC endpoint query: ' + str(results))
            self.logger.error('Raw results from ANC endpoint query on IDs: ' + x)
            raise

    def test(self):
        test = self.connection.ers.get_endpoint()
        return {'endpoint_list': test}
