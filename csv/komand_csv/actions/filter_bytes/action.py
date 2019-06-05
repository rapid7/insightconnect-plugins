import komand
from .schema import FilterBytesInput, FilterBytesOutput
# Custom imports below
import base64
from komand_csv.util import utils


class FilterBytes(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='filter_bytes',
                description='Keep fields from base64 CSV file',
                input=FilterBytesInput(),
                output=FilterBytesOutput())

    def run(self, params={}):
        decoded = base64.b64decode(params['csv'])
        csv_good = utils.csv_syntax_good(decoded)
        fields_good = utils.fields_syntax_good(params['fields'])

        if csv_good and fields_good:
            csv_array = utils.parse_csv_string(decoded)
            fields = utils.get_field_list(params['fields'], len(csv_array[0]))
            if fields:
                filtered = []
                for line in csv_array:
                    filtered.append(utils.keep_fields(line, fields))
                converted = utils.convert_csv_array(filtered)
                return {'filtered': base64.b64encode(converted)}
            else:
                raise ValueError('Invalid field indices')
        elif not csv_good:
            raise ValueError('Improper syntax in CSV bytes')
        else:
            raise ValueError('Improper syntax in fields string')

    def test(self):
        filtered = []
        filtered.append({"test", "c", "s", "v"})
        converted = utils.convert_csv_array(filtered)
        return {"filtered": base64.b64encode(converted)}
