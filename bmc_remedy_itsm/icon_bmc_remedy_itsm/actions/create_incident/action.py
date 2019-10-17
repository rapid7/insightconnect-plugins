import komand
from .schema import CreateIncidentInput, CreateIncidentOutput, Input, Output, Component
# Custom imports below
import requests
from komand.exceptions import PluginException
import urllib.parse


class CreateIncident(komand.Action):
    _URI = "api/arsys/v1/entry/HPD%3AIncidentInterface%5FCreate"
    _CONVERSION_KEY = {"First_Name": "first_name", "Last_Name": "last_name", "Service_Type": "service_type",
                       "Login_ID": "login_id", "Reported Source": "reported_source", "Status": "status",
                       "Impact": "impact", "Urgency": "urgency", "Description": "incident_description"}

    def __init__(self):
        super(self.__class__, self).__init__(
            name='create_incident',
            description=Component.DESCRIPTION,
            input=CreateIncidentInput(),
            output=CreateIncidentOutput())

    def run(self, params={}):
        values = {"values": {"z1D_Action": "CREATE"}}
        other_inputs = params.pop(Input.OTHER_INPUTS)

        for key, value in self._CONVERSION_KEY.items():
            if params.get(value):
                values["values"].update({key: params[value]})
        values["values"].update(other_inputs)

        url = urllib.parse.urljoin(self.connection.url, self._URI)
        headers = self.connection.make_headers_and_refresh_token()

        result = requests.post(url, headers=headers, json=values)

        if result.status_code == 400:
            raise PluginException(cause="An HTTP 400 status code was returned.",
                                  assistance="This status code indicates that the JSON Token was invalid."
                                             " This is normally caused by an incorrect username or password.")
        try:
            result.raise_for_status()
        except requests.HTTPError as e:
            raise PluginException(cause=f"An unexpected status code was returned. Status code was {result.status_code}.",
                                  assistance="Please contact support with the status code and error information.",
                                  data=e)

        return {Output.SUCCESS: True}
