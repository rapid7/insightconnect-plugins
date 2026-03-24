import datetime
import time

import insightconnect_plugin_runtime

# Custom imports below

from icon_azure_sentinel.util.tools import generate_query_params
from .schema import Component, GetNewIncidentsInput, GetNewIncidentsOutput, Input, Output

STATE_LAST_INCIDENT_TIME = "last_incident_time"


class GetNewIncidents(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_new_incidents",
            description=Component.DESCRIPTION,
            input=GetNewIncidentsInput(),
            output=GetNewIncidentsOutput(),
        )

    def _get_last_incident_time(self, interval: int) -> datetime.datetime:
        """Retrieve the last processed incident time from persistent state, or fall back to now - interval."""
        saved_time = self.state.get(STATE_LAST_INCIDENT_TIME)
        if saved_time:
            try:
                return datetime.datetime.fromisoformat(saved_time)
            except (ValueError, TypeError):
                self.logger.warning(f"Invalid saved state for {STATE_LAST_INCIDENT_TIME}, falling back to default")
        return datetime.datetime.now() - datetime.timedelta(seconds=interval)

    def _update_last_incident_time(self, incidents: list):
        """Update persistent state with the latest incident's createdTimeUtc."""
        latest_time = None
        for incident in incidents:
            props = incident.get("properties", {})
            created_str = props.get("createdTimeUtc")
            if created_str:
                try:
                    created = datetime.datetime.fromisoformat(created_str.replace("Z", ""))
                    if latest_time is None or created > latest_time:
                        latest_time = created
                except (ValueError, TypeError):
                    continue
        if latest_time:
            self.state[STATE_LAST_INCIDENT_TIME] = latest_time.isoformat()
            self.logger.info(f"Updated checkpoint to {latest_time.isoformat()}")

    def run(self, params={}):
        subscription_id = params.get(Input.SUBSCRIPTIONID)
        resource_group_name = params.get(Input.RESOURCEGROUPNAME)
        workspace_name = params.get(Input.WORKSPACENAME)
        interval = abs(params.get(Input.INTERVAL))

        status = params.get(Input.STATUS)
        last_update_time = (
            datetime.datetime.fromisoformat(params.get(Input.LAST_UPDATE_TIME)).replace(tzinfo=None)
            if params.get(Input.LAST_UPDATE_TIME)
            else None
        )

        assigned_to = params.get(Input.ASSIGNED_TO)

        while True:
            checkpoint_time = self._get_last_incident_time(interval)
            self.logger.info(f"Polling incidents from checkpoint: {checkpoint_time.isoformat()}")

            filters = generate_query_params(status, checkpoint_time, last_update_time, assigned_to)
            incidents, _ = self.connection.api_client.list_incident(
                resource_group_name, workspace_name, filters, subscription_id
            )
            if incidents:
                self.send({Output.INCIDENTS: incidents})
                self._update_last_incident_time(incidents)
            else:
                self.logger.info("No new incidents have been found!")
            self.logger.info(f"Sleeping for {interval} seconds...\n")
            time.sleep(interval)
