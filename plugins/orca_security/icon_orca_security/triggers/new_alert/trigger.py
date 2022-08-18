import insightconnect_plugin_runtime
import time
from .schema import NewAlertInput, NewAlertOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from datetime import datetime
import json


class NewAlert(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="new_alert", description=Component.DESCRIPTION, input=NewAlertInput(), output=NewAlertOutput()
        )

    def run(self, params={}):
        interval = params.get(Input.INTERVAL)
        additional_filters = self.validate_filters(params.get(Input.FILTERS, []))
        filters = [{"field": "state.created_at", "range": {"gte": datetime.now().isoformat()}}]
        filters.extend(additional_filters)
        while True:
            dsl_filter = {"dsl_filter": json.dumps({"filter": filters})}
            filters[0] = {"field": "state.created_at", "range": {"gt": datetime.now().isoformat()}}
            alerts = self.connection.api.query_alerts(dsl_filter).get("data", [])
            for alert in alerts:
                self.send({Output.ALERT: alert})
            time.sleep(interval)

    @staticmethod
    def validate_filters(filters: list) -> list:
        new_filters = []
        for provided_filter in filters:
            field = provided_filter.get("field")
            includes = provided_filter.get("includes")
            excludes = provided_filter.get("excludes")
            if not field:
                raise PluginException(
                    cause=f"The name of the field against which the alerts should be filtered was not specified in the "
                    f"filter: {provided_filter}.",
                    assistance="Please provide a field name and try again.",
                )
            if not includes and not excludes:
                raise PluginException(
                    cause=f"No values were given for the field to include or exclude in the filter: {provided_filter}.",
                    assistance="Please provide 'includes' or 'excludes' fields and try again.",
                )
            if field != "state.created_at":
                new_filters.append(provided_filter)
        return new_filters
