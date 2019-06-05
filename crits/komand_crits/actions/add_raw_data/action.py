import komand
from .schema import AddRawDataInput, AddRawDataOutput
# Custom imports below
from komand_crits.util import utils


class AddRawData(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_raw_data',
                description='Creates new raw data',
                input=AddRawDataInput(),
                output=AddRawDataOutput())

    def run(self, params={}):
        filename, file_obj = utils.file_from_params(**params['file'])
        response = self.connection.crits.add_raw_data(
            type_=params['type'],
            title=params['title'],
            data_type=params['data_type'],
            source=params['source'],
            data=params.get('data'),
            filename=filename,
            file_obj=file_obj
        )
        return {'response': utils.make_response(response)}

    def test(self):
        """TODO: Test action"""
        return {}
