import insightconnect_plugin_runtime
from .schema import PublishInput, PublishOutput

# Custom imports below


class Publish(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="publish",
            description="Publish an event",
            input=PublishInput(),
            output=PublishOutput(),
        )

    def run(self, params={}):
        event = params.get("event")

        client = self.connection.client
        in_event = client.get_event(event)
        published = client.publish(in_event, True)
        try:
            published["id"]
        except KeyError:
            self.logger.error("Something went wrong see returned request, %s", published)
            raise
        return {"published": published}
