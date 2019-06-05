import komand
from .schema import QuarantineInput, QuarantineOutput
from komand.exceptions import ConnectionTestException
# Custom imports below


class Quarantine(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='quarantine',
                description='Quarantine a host',
                input=QuarantineInput(),
                output=QuarantineOutput())

    def run(self, params={}):
        mac_address = params.get('mac_address')
        policy = params.get('policy')

        self.connection.ers.apply_anc_endpoint_mac(mac_address, policy)
        results = self.connection.ers.get_anc_endpoint()

        try:
            results = results['SearchResult']['resources']
        except KeyError:
            self.logger.error('Raw results from ANC endpoint query: ' + str(results))
            raise
        except Exception as e:
            self.logger.error(e)
            self.logger.error('Raw results from ANC endpoint query: ' + str(results))
            raise

        try:
            for x in results:
                find = self.connection.ers.get_anc_endpoint(x['id'])
                if find['ErsAncEndpoint']['macAddress'] == mac_address:
                    return {'ers_anc_endpoint': find['ErsAncEndpoint']}
        except KeyError:
            self.logger.error('Raw results from ANC endpoint query: ' + str(results))
            self.logger.error('Raw results from ANC endpoint query on IDs: ' + x)
            raise
        except Exception as e:
            self.logger.error(e)
            self.logger.error('Raw results from ANC endpoint query: ' + str(results))
            self.logger.error('Raw results from ANC endpoint query on IDs: ' + x)
            raise

        self.logger.error('MAC address, ' + mac_address)
        self.logger.error('Policy, ' + policy)
        self.logger.error('Raw results from ANC endpoint query,' + str(results))
        raise ConnectionTestException(cause="Cisco ISE did not return a result",
                                      assistance="Check your configuration settings and confirm your policy exists and "
                                                 "MAC address are correct")

    def test(self):
        test = self.connection.ers.get_endpoint()
        return {'endpoint_list': test}
