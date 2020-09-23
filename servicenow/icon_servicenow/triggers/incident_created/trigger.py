import komand
import time
from .schema import IncidentCreatedInput, IncidentCreatedOutput, Input, Output, Component
# Custom imports below


class IncidentCreated(komand.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='incident_created',
                description=Component.DESCRIPTION,
                input=IncidentCreatedInput(),
                output=IncidentCreatedOutput())
        self.found = {}
        self.url = ""
        self.method = "get"
        self.query = ""

    def initialize(self):
        if self.query:
            response = self.connection.request.make_request(
                self.url, self.method, params=self.query)
        else:
            response = self.connection.request.make_request(self.url, self.method)

        try:
            results = response.get("resource").get("result")
        except KeyError as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN,
                                  data=response.text) from e

        sys_ids = [result.get("sys_id") for result in results]
        for sys_id in sys_ids:
            self.found[sys_id] = True

    def poll(self):
        if self.query:
            response = self.connection.request.make_request(
                self.url, self.method, params=self.query)
        else:
            response = self.connection.request.make_request(self.url, self.method)

        try:
            new_results = response.get("resource").get("result")
        except KeyError as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN,
                                  data=response.text) from e

        new_sys_ids = [result.get("sys_id") for result in new_results]

        for new_sys_id in new_sys_ids:
            if new_sys_id not in self.found:
                self.logger.info("Found new incident: %s", new_sys_id)
                self.found[new_sys_id] = True
                self.send({Output.SYSTEM_ID: new_sys_id})

    def run(self, params={}):
        self.url = self.connection.incident_url

        if params.get(Input.QUERY):
            self.query = {"sysparm_query": params.get(Input.QUERY)}

        self.initialize()

        while True:
            self.poll()
            time.sleep(params.get(Input.INTERVAL, 5))
