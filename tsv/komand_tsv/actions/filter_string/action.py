import komand
from .schema import FilterStringInput, FilterStringOutput
from komand.exceptions import PluginException
# Custom imports below
import json
from komand_tsv.util import utils

class FilterString(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='filter_string',
                description='Keep fields from TSV string',
                input=FilterStringInput(),
                output=FilterStringOutput())

    def run(self, params={}):
        tsv_good = utils.tsv_syntax_good(params['tsv']) 
        fields_good = utils.fields_syntax_good(params['fields'])        

        if tsv_good and fields_good:
            tsv_array = utils.parse_tsv_string(params['tsv'])
            fields = utils.get_field_list(params['fields'], len(tsv_array[0]))
            if fields:
                filtered = []
                for line in tsv_array:
                    filtered.append(utils.keep_fields(line, fields))
                return {'filtered': utils.convert_tsv_array(filtered)}
            else:
                raise PluginException(cause='Invalid field indices')
        elif not tsv_good:
            raise PluginException(cause='Improper syntax in TSV string')
        else:
            raise PluginException(cause='Improper syntax in fields string')

    def test(self):
        # TODO: Implement test function
        return {}
