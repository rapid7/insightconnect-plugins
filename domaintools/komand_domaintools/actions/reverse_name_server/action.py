import komand
from .schema import ReverseNameServerInput, ReverseNameServerOutput
# Custom imports below
from komand_domaintools.util import util


class ReverseNameServer(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='reverse_name_server',
                description='Provides a list of domain names that share the same primary or secondary name server',
                input=ReverseNameServerInput(),
                output=ReverseNameServerOutput())

    def run(self, params={}):
        params = komand.helper.clean_dict(params)
        params['query'] = params.pop('domain')
        response = utils.make_request(self.connection.api.reverse_name_server, **params)
        return response

    def test(self):
        """TODO: Test action"""
        return {}
