import komand
from .schema import CreateAnEventInput, CreateAnEventOutput
# Custom imports below
import json


class CreateAnEvent(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_an_event',
                description='Create a MISP event',
                input=CreateAnEventInput(),
                output=CreateAnEventOutput())

    def run(self, params={}):
        dist = {
            "This Organization": "0",
            "This Community": "1",
            "Connected Communities": "2",
            "All Communities": "3"
        }

        try:
            event = self.connection.client.new_event(distribution=dist[params.get("distribution")] or None,
                                                     threat_level_id=params.get("threat_level_id"),
                                                     analysis=params.get("analysis") or None,
                                                     info=params.get("info"),
                                                     date=None,
                                                     published=params.get("published"),
                                                     orgc_id=params.get("orgc_id") or None,
                                                     org_id=params.get("org_id") or None,
                                                     sharing_group_id=params.get("sharing_group_id") or None)
            output = json.loads(json.dumps(event))
        except Exception as e:
            self.logger.error(e)
            raise
        try:
            return output['Event']
        except Exception as e:
            raise Exception(output["message"])


    def test(self):
        client = self.connection.client
        output = client.test_connection()
        return {"id": "", "org_id": "", "date": "", "info": "", "uuid": "", "published": True, "analysis": "",
                "attribute_count": "", "orgc_id": "", "timestamp": "", "distribution": "", "sharing_group_id": "",
                "proposal_email_lock": False, "locked": False, "threat_level_id": "", "publish_timestamp": "",
                "disable_correlation": False, "Org": {"id": "1", "name": "ORGNAME"}, "Orgc": {}, "Attribute": [{}],
                "sharing_group_id": "", "event_creator_email": ""}
