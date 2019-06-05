import komand
from .schema import ModifySavedSearchPropertiesInput, ModifySavedSearchPropertiesOutput
# Custom imports below
import json


class ModifySavedSearchProperties(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='modify_saved_search_properties',
                description='Modifies the properties of a saved search',
                input=ModifySavedSearchPropertiesInput(),
                output=ModifySavedSearchPropertiesOutput())

    def run(self, params={}):
        saved_search_name = params.get("saved_search_name")
        properties = params.get("properties")

        param_dict = json.loads(
            json.dumps(properties, default=lambda o: o.__dict__, indent=4, sort_keys=True)
        )

        try:
            saved_search_to_update = self.connection.client.saved_searches[saved_search_name]
            saved_search_to_update.update(**param_dict).refresh()
        except KeyError as error:
            self.logger.error(error)
            return {"success": False}

        return {"success": True}

    def test(self):
        return {}
