import insightconnect_plugin_runtime
from .schema import ListCloudsInput, ListCloudsOutput, Input, Output, Component

# Custom imports below


class ListClouds(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_clouds",
            description=Component.DESCRIPTION,
            input=ListCloudsInput(),
            output=ListCloudsOutput(),
        )

    def run(self, params={}):

        # Iterates through all input fields and retrieves the value as if it was `offset = params.get(Input.OFFSET)`. If null it's not included in body
        response = self.connection.api.list_clouds(
            {
                key: value
                for key, value in (
                    (key, params.get(getattr(Input, key.upper())))
                    for key in [
                        "filters",
                        "limit",
                        "offset",
                        "order_by",
                        "badges",
                        "badge_filter_operator",
                        "search_string",
                        "advanced_search",
                        "empty_badges",
                        "exclusion_badges",
                    ]
                )
                if value not in (None, {}, "")
            }
        )

        return {Output.CLOUDS: response.get("clouds", []), Output.TOTAL_COUNT: response.get("total_count", 0)}
