import komand
from .schema import FilterBytesInput, FilterBytesOutput
# Custom imports below
import json
import base64
from komand_tsv.util import utils

class FilterBytes(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='filter_bytes',
                description='Keep fields from base64 TSV file',
                input=FilterBytesInput(),
                output=FilterBytesOutput())

    def run(self, params={}):
        decoded = base64.b64decode(params['tsv'])
        tsv_good = utils.tsv_syntax_good(decoded)
        fields_good = utils.fields_syntax_good(params['fields'])

        if tsv_good and fields_good:
            tsv_array = utils.parse_tsv_string(decoded)
            fields = utils.get_field_list(params['fields'], len(tsv_array[0]))
            if fields:
                filtered = []
                for line in tsv_array:
                    filtered.append(utils.keep_fields(line, fields))
                converted = utils.convert_tsv_array(filtered)
                return {'filtered': base64.b64encode(converted)}
            else:
                raise ValueError('Invalid field indices')
        elif not tsv_good:
            raise ValueError('Improper syntax in TSV bytes')
        else:
            raise ValueError('Improper syntax in fields string')

    def test(self):
        # TODO: Implement test function
        return {}
