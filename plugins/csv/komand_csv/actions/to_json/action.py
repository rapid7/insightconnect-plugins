import insightconnect_plugin_runtime
from .schema import ToJsonInput, ToJsonOutput, Input, Output, Component

# Custom imports below
import base64
from komand_csv.util import utils
from insightconnect_plugin_runtime.exceptions import PluginException


class ToJson(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="to_json",
            description=Component.DESCRIPTION,
            input=ToJsonInput(),
            output=ToJsonOutput(),
        )

    def run(self, params={}):
        decoded = base64.b64decode(params.get(Input.CSV, "")).decode()

        validation = params.get(Input.VALIDATION)
        if validation:
            csv_good = utils.csv_syntax_good(decoded)
            if not csv_good:
                raise PluginException(cause="Malformed CSV.", assistance="Wrong CSV syntax.")

        list_of_dicts = utils.csv_to_dict(decoded, self)

        return {Output.JSON: list_of_dicts}
