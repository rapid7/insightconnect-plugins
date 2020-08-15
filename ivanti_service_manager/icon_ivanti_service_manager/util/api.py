import json
import requests
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean

class IvantiServiceManagerAPI:
    def __init__(self, api_key: str, url: str, verify_ssl: bool, logger: object):
        self.url = url + "/api/"
        self.verify_ssl = verify_ssl
        self.logger = logger
        self.api_key = api_key

    def get_employees(self):
        return self._call_api("GET", "odata/businessobject/employees")

    def search_employee(self, identifier: str):
        employees = self._call_api("GET", f"odata/businessobject/employees?$search={identifier}").get("value")
        
        if len(employees) > 1:
            raise PluginException(
            cause='Multiple employees found.',
            assistance=f'Multiple employees found using email provided - {identifier}. Please provide a full email address.'
        )
        if len(employees) == 0:
            raise PluginException(
            cause='No employees found.',
            assistance=f'No employees found using email provided - {identifier}. Please validate and try again.'
        )

        return employees[0]

    def search_incident(self, incident_number):
        return self._call_api("GET", f"odata/businessobject/incidents?$search={incident_number}")

    def post_incident(self, payload: dict):
        return clean(self._call_api("POST", "odata/businessobject/incidents", json_data=payload))

    def _call_api(self, method: str, path: str, json_data: dict = None, params: dict = None):
        response = {"text": ""}
        headers = {
            'Authorization': f'rest_api_key={self.api_key}'
        }

        try:
            response = requests.request(
                method, self.url + path,
                json=json_data,
                params=params,
                headers=headers,
                verify=self.verify_ssl
            )

            if response.status_code == 401:
                raise PluginException(preset=PluginException.Preset.API_KEY)
            if response.status_code == 403:
                raise PluginException(preset=PluginException.Preset.UNAUTHORIZED)
            if response.status_code >= 400:
                response_data = response.text
                raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response_data)
            if response.status_code == 204:
                return {}
            if 200 <= response.status_code < 300:
                return response.json()

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError as e:
            self.logger.info(f"Invalid JSON: {e}")
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)
        except requests.exceptions.HTTPError as e:
            self.logger.info(f"Call to Ivanti Service Manager API failed: {e}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
