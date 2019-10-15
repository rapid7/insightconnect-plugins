import komand
from .schema import UpdateIncidentStatusInput, UpdateIncidentStatusOutput, Input, Output, Component
# Custom imports below
import requests
from komand.exceptions import PluginException
import urllib.parse


class UpdateIncidentStatus(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='update_incident_status',
            description=Component.DESCRIPTION,
            input=UpdateIncidentStatusInput(),
            output=UpdateIncidentStatusOutput())

    def run(self, params={}):
        # To update the status on a ticket, we have to get the original ticket, update the status, then
        # send the original back with the updated status.

        incident_id = params.get(Input.INCIDENT_ID)
        status = params.get(Input.STATUS)

        uri = f"api/arsys/v1/entry/HPD%3AIncidentInterface/{incident_id}|{incident_id}"
        url = urllib.parse.urljoin(self.connection.url, uri)

        headers = self.connection.make_headers_and_refresh_token()

        original_incident_response = requests.get(url, headers=headers)

        if not original_incident_response.status_code == 200:
            raise PluginException(cause=f"Unexpected server response: {original_incident_response.status_code} ",
                                  assistance="This may be an invalid incident number. Please verify that you have the "
                                             "correct incident number.",
                                  data=original_incident_response.text)

        original_incident = komand.helper.clean(original_incident_response.json())

        original_incident.get("values")["Status"] = status
        original_incident.get("values")["z1D Action"] = "Modify"

        result = requests.put(url, headers=headers, json=original_incident)

        if not result.status_code == 204:
            raise PluginException(cause=f"Unexpected server response: {result.status_code} ",
                                  assistance="You may have given an invalid status for this ticket. Please check with "
                                             "your BMC Remedy administrator that the status given for this ticket is "
                                             "valid in your workflow.",
                                  data=result.text)

        original_incident_response = requests.get(url, headers=headers)

        # If we made it this far, and this call fails, something really unexpected happened.
        if not original_incident_response.status_code == 200:
            raise PluginException(PluginException.Preset.SERVER_ERROR,
                                  data=original_incident_response.text)

        original_incident = original_incident_response.json()

        return {Output.INCIDENT: komand.helper.clean(original_incident)}
