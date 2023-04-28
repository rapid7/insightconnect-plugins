import insightconnect_plugin_runtime
from .schema import SendPushInput, SendPushOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
import time


class SendPush(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="send_push",
            description=Component.DESCRIPTION,
            input=SendPushInput(),
            output=SendPushOutput(),
        )

    def run(self, params={}):
        response = self.connection.api_client.send_push(params.get(Input.USERID), params.get(Input.FACTORID))

        response["links"] = response.pop("_links")
        links = response.get("links", {})
        poll = links.get("poll")
        if not poll:
            raise PluginException(
                cause=f"An error has occurred retrieving data from the Okta API.",
                assistance="It looks like we didn't get data we were expecting back. Was "
                "the Factor ID supplied a push type and not something else, "
                "such as an SMS?",
            )

        # Time out after 60 seconds
        for _ in range(12):
            poll_response = self.connection.api_client.verify_poll_status(poll.get("href"))
            poll_status = poll_response.get("factorResult")
            if poll_status != "WAITING":
                return {Output.FACTORSTATUS: poll_status}
            time.sleep(5)
        return {Output.FACTORSTATUS: "TIMEOUT"}
