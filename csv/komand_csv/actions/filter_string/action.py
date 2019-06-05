import komand
from .schema import FilterStringInput, FilterStringOutput
# Custom imports below
from komand_csv.util import utils


class FilterString(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='filter_string',
                description='Keep fields from CSV string',
                input=FilterStringInput(),
                output=FilterStringOutput())

    def run(self, params={}):
        csv_good = utils.csv_syntax_good(params['csv'])
        fields_good = utils.fields_syntax_good(params['fields'])

        if csv_good and fields_good:
            csv_array = utils.parse_csv_string(params['csv'])
            fields = utils.get_field_list(params['fields'], len(csv_array[0]))
            if fields:
                filtered = []
                for line in csv_array:
                    filtered.append(utils.keep_fields(line, fields))
                return {'string': utils.convert_csv_array(filtered)}
            else:
                raise ValueError('Invalid field indices')
        elif not csv_good:
            raise ValueError('Improper syntax in CSV string')
        else:
            raise ValueError('Improper syntax in fields string')

    def test(self, params={}):
        return {"string": "test,c,s,v"}
