import insightconnect_plugin_runtime
from .schema import AddContextInput, AddContextOutput


class AddContext(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_context",
            description="Add context",
            input=AddContextInput(),
            output=AddContextOutput(),
        )

    def run(self, params={}):
        client = self.connection.client

        dist = {
            "This Organization": "0",
            "This Community": "1",
            "Connected Communities": "2",
            "All Communities": "3",
        }

        try:
            event_cmt = client.get_event(params.get("comment")["event"])
            event_link = client.get_event(params.get("link")["event"])
            event_other = client.get_event(params.get("other")["event"])
            event_txt = client.get_event(params.get("text")["event"])
            proposal = params.get("proposal")

            client.add_internal_comment(
                event_cmt,
                reference=params.get("comment")["comment_in"],
                category="Internal reference",
                to_ids=False,
                comment=params.get("comment")["comment"],
                distribution=dist[params.get("comment")["distribution"]],
                proposal=proposal,
            )

            client.add_internal_link(
                event_link,
                reference=params.get("link")["link"],
                category="Internal reference",
                to_ids=False,
                comment=params.get("link")["comment"],
                distribution=dist[params.get("link")["distribution"]],
                proposal=proposal,
            )

            client.add_internal_other(
                event_other,
                reference=params.get("other")["other"],
                category="Internal reference",
                to_ids=False,
                comment=params.get("other")["comment"],
                distribution=dist[params.get("other")["distribution"]],
                proposal=proposal,
            )

            client.add_internal_text(
                event_txt,
                reference=params.get("text")["text"],
                category="Internal reference",
                to_ids=False,
                comment=params.get("text")["comment"],
                distribution=dist[params.get("text")["distribution"]],
                proposal=proposal,
            )

            return {"status": True}
        except Exception as error:
            self.logger.error(error)
        return {"status": False}
