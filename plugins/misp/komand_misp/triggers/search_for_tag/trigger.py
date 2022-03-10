import insightconnect_plugin_runtime
import time
from .schema import SearchForTagInput, SearchForTagOutput

# Custom imports below


class SearchForTag(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="search_for_tag",
            description="This trigger will search MISP for any events with a specified tag",
            input=SearchForTagInput(),
            output=SearchForTagOutput(),
        )

    def run(self, params={}):
        while True:
            interval = params.get("interval")
            tag = params.get("tag")
            remove = params.get("remove")

            client = self.connection.client
            event_id = []
            events = client.search_index(tag=tag)
            try:
                events = events["response"]
            except KeyError:
                self.logger.error("Unexpected search return, %s")
                raise
            for event in events:
                try:
                    event_id.append(event["id"])
                except KeyError:
                    self.logger.error("No id found, %s")
                    raise
            if remove:
                for event in event_id:
                    in_event = client.get_event(event)
                    try:
                        client.untag(in_event["Event"]["uuid"], tag=tag)
                    except KeyError:
                        self.logger.error("While removing the tags something went wrong, %s", in_event)
            if event_id:
                self.send({"events": event_id})
            time.sleep(interval)
