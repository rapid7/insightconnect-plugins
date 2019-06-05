import komand
from .schema import AddPcapInput, AddPcapOutput
# Custom imports below
from komand_crits.util import utils


class AddPcap(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_pcap',
                description='Creates a new PCAP',
                input=AddPcapInput(),
                output=AddPcapOutput())

    def run(self, params={}):
        filename, file_obj = utils.file_from_params(**params['file'])
        response = self.connection.crits.add_pcap(
            source=params['source'],
            filename=filename,
            file_obj=file_obj
        )
        return {'response': utils.make_response(response)}

    def test(self):
        """TODO: Test action"""
        return {}
