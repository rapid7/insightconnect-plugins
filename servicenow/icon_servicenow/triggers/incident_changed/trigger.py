import komand
import time
from .schema import IncidentChangedInput, IncidentChangedOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException
import time


class IncidentChanged(komand.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='incident_changed',
                description=Component.DESCRIPTION,
                input=IncidentChangedInput(),
                output=IncidentChangedOutput())

    def run(self, params={}):
        url = f'{self.connection.incident_url}/{params.get(Input.SYSTEM_ID)}'
        method = "get"

        response = self.connection.request.make_request(
            url, method, params=f"sysparm_fields={params.get(Input.MONITORED_FIELDS)}")

        # Initial pull of incident
        try:
            prev_incident = response["resource"].get("result")
        except KeyError as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN,
                                  data=response.text) from e

        while True:
            response = self.connection.request.make_request(
                url, method, params=f"sysparm_fields={params.get(Input.MONITORED_FIELDS)}")
            try:
                current_incident = response["resource"].get("result")
            except KeyError as e:
                raise PluginException(preset=PluginException.Preset.UNKNOWN,
                                      data=response.text) from e

            # Compare previous and new incident results
            changed_fields = {}
            for field, value in prev_incident.items():
                if current_incident.get(field) != value:
                    changed_fields[field] = {'previous': value, 'current': current_incident.get(field)}

            # Send if field changes identified
            if len(changed_fields) > 0:
                self.send({Output.CHANGED_FIELDS: changed_fields})

            # Set previous incident state to current incident
            prev_incident = current_incident

            # Sleep for configured frequency in minutes
            time.sleep(params.get(Input.INTERVAL, 5) * 60)
