import komand
from .schema import AddSampleInput, AddSampleOutput
# Custom imports below
from komand_crits.util import utils


class AddSample(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_sample',
                description='Creates a new sample',
                input=AddSampleInput(),
                output=AddSampleOutput())

    def run(self, params={}):
        filename, file_obj = utils.file_from_params(**params['file'])
        response = self.connection.crits.add_sample(
            type_=params['type'],
            source=params['source'],
            filename=filename,
            file_obj=file_obj,
            params=params['params']
        )
        return {'response': utils.make_response(response)}

    def test(self):
        """TODO: Test action"""
        return {}
