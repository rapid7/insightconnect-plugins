import insightconnect_plugin_runtime
from .schema import AddSightingsInput, AddSightingsOutput, Input, Output, Component

# Custom imports below


class AddSightings(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_sightings",
            description=Component.DESCRIPTION,
            input=AddSightingsInput(),
            output=AddSightingsOutput(),
        )

    def run(self, params={}):
        client = self.connection.client
        try:
            item = client.add_sighting({"values": params.get(Input.SIGHTINGS)})
            # API spells this wrong
            # {'url': '/sighting/add', 'message': '3 sightings successfuly added.', 'name': '3 sightings successfully added.'}
            if "successfuly added" in item["message"] or "successfully added" in item["message"]:
                return {Output.STATUS: True}
            else:
                self.logger.info(item)
                return {Output.STATUS: False}
        except Exception as error:
            self.logger.error(error)
            return {Output.STATUS: False}
