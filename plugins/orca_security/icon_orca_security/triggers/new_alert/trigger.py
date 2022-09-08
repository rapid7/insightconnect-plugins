import insightconnect_plugin_runtime
import time
from .schema import NewAlertInput, NewAlertOutput, Input, Output, Component

# Custom imports below
from datetime import datetime
import json

from icon_orca_security.util.helpers import validate_filters


class NewAlert(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="new_alert", description=Component.DESCRIPTION, input=NewAlertInput(), output=NewAlertOutput()
        )

    def run(self, params={}):
        interval = params.get(Input.INTERVAL)
        additional_filters = validate_filters(params.get(Input.FILTERS, []))
        filters = [{"field": "state.created_at", "range": {"gte": datetime.now().isoformat()}}]
        filters.extend(additional_filters)
        while True:
            dsl_filter = {"dsl_filter": json.dumps({"filter": filters})}
            filters[0] = {"field": "state.created_at", "range": {"gt": datetime.now().isoformat()}}
            alerts = self.connection.api.query_alerts(dsl_filter).get("data", [])
            for alert in alerts:
                self.send({Output.ALERT: alert})
            time.sleep(interval)
