import insightconnect_plugin_runtime
from .schema import AddSightingsInput, AddSightingsOutput

# Custom imports below


class AddSightings(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_sightings",
            description="Add sightings to organization",
            input=AddSightingsInput(),
            output=AddSightingsOutput(),
        )

    def run(self, params={}):
        client = self.connection.client
        try:
            item = client.set_sightings({"values": params.get("sightings")})
            # API spells this wrong
            # {'url': '/sighting/add', 'message': '3 sightings successfuly added.', 'name': '3 sightings successfully added.'}
            if "successfuly added" in item["message"] or "successfully added" in item["message"]:
                return {"status": True}
            else:
                self.logger.info(item)
                return {"status": False}
        except Exception as error:
            self.logger.error(error)
            return {"status": False}
