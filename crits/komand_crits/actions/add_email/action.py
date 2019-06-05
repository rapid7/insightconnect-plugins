import komand
from .schema import AddEmailInput, AddEmailOutput
# Custom imports below
from komand_crits.util import utils


class AddEmail(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_email',
                description='Creates a new email',
                input=AddEmailInput(),
                output=AddEmailOutput())

    def run(self, params={}):
        filename, file_obj = utils.file_from_params(**params['file'])
        response = self.connection.crits.add_email(
            type_=params['type'],
            filename=filename,
            file_obj=file_obj,
            source=params['source'],
            params=params['params']
        )
        return {'response': utils.make_response(response)}

    def test(self):
        """TODO: Test action"""
        return {}
