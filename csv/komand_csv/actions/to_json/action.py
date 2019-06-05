import komand
from .schema import ToJsonInput, ToJsonOutput
# Custom imports below
import base64
from komand_csv.util import utils


class ToJson(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='to_json',
                description='Convert CSV to JSON',
                input=ToJsonInput(),
                output=ToJsonOutput())

    def run(self, params={}):
        decoded = base64.b64decode(params['csv'])

        validation = params.get('validation')
        if validation:
            csv_good = utils.csv_syntax_good(decoded)
            if not csv_good:
                self.logger.error('Malformed CSV')
                raise Exception

        list_of_dicts = utils.csv_to_dict(decoded, self)
        return {"json": list_of_dicts}

    def test(self):
        # TODO: Implement test function
        return {"json": []}
