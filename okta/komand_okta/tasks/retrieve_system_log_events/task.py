import insightconnect_plugin_runtime
from .schema import RetrieveSystemLogEventsInput, RetrieveSystemLogEventsOutput, RetrieveSystemLogEventsState, Input, Output, Component, State
Input, Output, Component, State
# Custom imports below
from datetime import datetime, timedelta
import requests
import urllib.parse


class RetrieveSystemLogEvents(insightconnect_plugin_runtime.Task):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='retrieve_system_log_events',
                description=Component.DESCRIPTION,
                input=RetrieveSystemLogEventsInput(),
                output=RetrieveSystemLogEventsOutput(),
                state=RetrieveSystemLogEventsState())

    def run(self, params={}, state={}):
        filter = params.get(Input.FILTER)
        okta_url = self.connection.okta_url
        last_event_time = state.get(State.LAST_EVENT_TIME, None)

        url = requests.compat.urljoin(okta_url, '/api/v1/logs')

        if last_event_time is None:
            # Pull events for past week to start
            now = datetime.utcnow()
            week_ago = now - timedelta(days=7)
            last_event_time = week_ago.strftime("%Y-%m-%dT%H:%M:%SZ")

        payload = {}
        if filter:
            payload['filter'] = filter

        if last_event_time:
            # Format: since=2017-10-01T00:00:00.000Z
            payload['since'] = last_event_time

        # Query for system logs
        self.logger.info(f"Retrieving system log events; only events after {last_event_time} will be retrieved")
        response = self.connection.session.get(url, params=payload)

        self.logger.info(response)

        try:
            data = response.json()
        except ValueError:
            return {Output.EVENTS: []}, {State.LAST_EVENT_TIME: last_event_time}

        if response.status_code == 200:
            return {Output.EVENTS: data}, {State.LAST_EVENT_TIME: datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")}
        else:
            raise_based_on_error_code(response=response)
