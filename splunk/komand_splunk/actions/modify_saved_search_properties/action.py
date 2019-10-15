import komand
from .schema import ModifySavedSearchPropertiesInput, ModifySavedSearchPropertiesOutput, Input, Output, Component
# Custom imports below
import json
from json import JSONDecodeError
from komand.exceptions import PluginException


class ModifySavedSearchProperties(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='modify_saved_search_properties',
                description=Component.DESCRIPTION,
                input=ModifySavedSearchPropertiesInput(),
                output=ModifySavedSearchPropertiesOutput())

    def run(self, params={}):
        saved_search_name = params.get(Input.SAVED_SEARCH_NAME)
        properties = params.get(Input.PROPERTIES)

        try:
            param_dict = json.loads(
                json.dumps(properties, default=lambda o: o.__dict__, indent=4, sort_keys=True)
            )

            saved_search_to_update = self.connection.client.saved_searches[saved_search_name]
            saved_search_to_update.update(**param_dict).refresh()
        except JSONDecodeError as e:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON) from e
        except KeyError as error:
            self.logger.error(error)
            return {Output.SUCCESS: False}

        return {Output.SUCCESS: True}
