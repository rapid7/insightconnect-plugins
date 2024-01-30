import insightconnect_plugin_runtime
from .schema import (
    ModifySavedSearchPropertiesInput,
    ModifySavedSearchPropertiesOutput,
    Input,
    Output,
    Component,
)

# Custom imports below
import json
from json import JSONDecodeError
from insightconnect_plugin_runtime.exceptions import PluginException


class ModifySavedSearchProperties(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="modify_saved_search_properties",
            description=Component.DESCRIPTION,
            input=ModifySavedSearchPropertiesInput(),
            output=ModifySavedSearchPropertiesOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        saved_search_name = params.get(Input.SAVED_SEARCH_NAME)
        properties = params.get(Input.PROPERTIES)
        # END INPUT BINDING - DO NOT REMOVE

        try:
            param_dict = json.loads(
                json.dumps(properties, default=lambda objects_: objects_.__dict__, indent=4, sort_keys=True)
            )
            saved_search_to_update = self.connection.client.saved_searches[saved_search_name]
            saved_search_to_update.update(**param_dict).refresh()
        except JSONDecodeError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON)
        except KeyError as error:
            self.logger.error(error)
            return {Output.SUCCESS: False}
        return {Output.SUCCESS: True}
