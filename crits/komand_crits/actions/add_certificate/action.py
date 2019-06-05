import komand
from .schema import AddCertificateInput, AddCertificateOutput
# Custom imports below
from komand_crits.util import utils


class AddCertificate(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_certificate',
                description='Creates a new certificate',
                input=AddCertificateInput(),
                output=AddCertificateOutput())

    def run(self, params={}):
        filename, file_obj = utils.file_from_params(**params['file'])
        response = self.connection.crits.add_certificate(
            source=params['source'],
            filename=filename,
            file_obj=file_obj,
            params=params['params']
        )
        return {'response': utils.make_response(response)}

    def test(self):
        """TODO: Test action"""
        return {}
