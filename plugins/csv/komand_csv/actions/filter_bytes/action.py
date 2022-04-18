import insightconnect_plugin_runtime
from .schema import FilterBytesInput, FilterBytesOutput, Input, Output, Component

# Custom imports below
import base64
from komand_csv.util import utils
from insightconnect_plugin_runtime.exceptions import PluginException


class FilterBytes(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="filter_bytes",
            description=Component.DESCRIPTION,
            input=FilterBytesInput(),
            output=FilterBytesOutput(),
        )

    def run(self, params={}):
        decoded = base64.b64decode(params[Input.CSV]).decode()
        csv_good = utils.csv_syntax_good(decoded)
        fields_good = utils.fields_syntax_good(params[Input.FIELDS])

        if csv_good and fields_good:
            csv_array = utils.parse_csv_string(decoded)
            fields = utils.get_field_list(params[Input.FIELDS], len(csv_array[0]))
            if fields:
                filtered = []
                for line in csv_array:
                    filtered.append(utils.keep_fields(line, fields))
                converted = utils.convert_csv_array(filtered)
                return {Output.FILTERED: base64.b64encode(converted.encode()).decode()}
            else:
                raise PluginException(cause="Wrong input.", assistance="Invalid field indices.")
        elif not csv_good:
            raise PluginException(cause="Wrong input.", assistance="Improper syntax in CSV bytes.")
        else:
            raise PluginException(cause="Wrong input.", assistance="Improper syntax in fields string.")
