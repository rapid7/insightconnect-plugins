import insightconnect_plugin_runtime
from .schema import FilterStringInput, FilterStringOutput, Input, Output, Component

# Custom imports below
from komand_csv.util import utils
from insightconnect_plugin_runtime.exceptions import PluginException


class FilterString(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="filter_string",
            description=Component.DESCRIPTION,
            input=FilterStringInput(),
            output=FilterStringOutput(),
        )

    def run(self, params={}):
        csv_string = params.get(Input.CSV, "")
        fields_to_filter = params.get(Input.FIELDS)

        csv_good = utils.csv_syntax_good(csv_string)
        fields_good = utils.fields_syntax_good(fields_to_filter)

        if csv_good and fields_good:
            csv_array = utils.parse_csv_string(csv_string)
            fields = utils.get_field_list(fields_to_filter, len(csv_array[0]))
            if fields:
                filtered = []
                for line in csv_array:
                    filtered.append(utils.keep_fields(line, fields))
                return {Output.STRING: utils.convert_csv_array(filtered)}
            else:
                raise PluginException(cause="Wrong input.", assistance="Invalid field indices.")
        elif not csv_good:
            raise PluginException(cause="Wrong input.", assistance="Improper syntax in CSV string.")
        else:
            raise PluginException(cause="Wrong input.", assistance="Improper syntax in fields string.")
