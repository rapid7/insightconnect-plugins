from insightconnect_plugin_runtime.helper import clean
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException
from logging import Logger
from typing import Union
import requests
import json



class PagerDutyAPI:
    def __init__(self, api_key: str, logger: Logger):
        self.headers = {
            "Authorization": f"Token token={api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        self.session = requests.session()
        self.logger = logger

    def get_on_calls(self, schedule_id: str) -> dict:
        """
            Formats the request to fetch the on-call users for a given schedule

        Args:
            schedule_id (str): The id of the schedule that the user info will be fetched for

        Returns:
            dict: _description_
        """
        return self.send_request("GET", f"/schedules/{schedule_id}/")

    def resolve_event(self, email: str, incident_id: str) -> dict:
        """
            Formats the request to call for an incident to be resolved

        Args:
            email (str): The email address of the user that is resolving the event
            incident_id (str): The id of the incident to be resolved

        Returns:
            dict: The full incident object with its updated values will be returend
        """
        headers = {"From": f"{email}"}
        headers.update(self.headers)
        data = {"incident": {"type": "incident", "status": "resolved"}}
        return self.send_request(
            method="PUT", path=f"/incidents/{incident_id}/", headers=headers, data=json.dumps(data)
        )

    def acknowledge_event(self, email: str, incident_id: str) -> dict:
        """
            Formats the request to call for an incident to be acknowledged

        Args:
            email (str): The email address of the user that is acknowledging the event
            incident_id (str): The id of the incident to be acknowledged

        Returns:
            dict: The full incident object with its updated values will be returend
        """
        headers = {"From": f"{email}"}
        headers.update(self.headers)
        data = {"incident": {"type": "incident", "status": "acknowledged"}}
        return self.send_request(
            method="PUT", path=f"/incidents/{incident_id}/", headers=headers, data=json.dumps(data)
        )

    def trigger_event(
        self,
        email: str,
        title: str,
        service: dict,
        dict_of_optional_fields: dict,
    ) -> dict:
        """
            Formats the request to allow the user to trigger an incident

        Args:
            email (str): The email of the user triggering the event
            title (str): The title of the description
            service (dict): The service id and the type that will be incident will be associated to
            dict_of_optional_fields (dict): Optional fields that can also be added to an incident, these can include:
                [urgency, incident_key, priority, escalation_policy, conference_bridge, body, assignments]
        Returns:
            dict: This will return the full object of the newly created incident
        """
        headers = {"From": f"{email}"}
        headers.update(self.headers)

        payload = {"incident": {"type": "incident", "title": title, "service": service}}

        for key, value in dict_of_optional_fields.items():
            if value:
                payload["incident"][key] = value

        return self.send_request(method="POST", path="/incidents/", headers=headers, payload=payload)

    def create_user(
        self,
        from_email: str,
        new_users_email: str,
        name: str,
        dict_of_optional_fields: dict,
    ) -> dict:
        """
            Formats the request to all for a new user to be created

        Args:
            from_email (str): The email for the account that is creating the new user
            new_users_email (str): The email for the new account
            name (str): The name for the new account
            dict_of_optional_fields (dict): Optional fields that can also be used when creating a new user, these include:
                [time_zone, color, role, description, job_title, license]

        Returns:
            dict: The newly cerated user object
        """
        headers = {"From": f"{from_email}"}
        headers.update(self.headers)

        payload = {"user": {"name": name, "email": new_users_email}}

        for key, value in dict_of_optional_fields.items():
            if value:
                payload["user"][key] = value

        return self.send_request(method="POST", path="/users/", headers=headers, payload=payload)

    def delete_user_by_id(self, email: str, user_id: str) -> bool:
        """
            Formats the request to allow for a user to be deleted

        Args:
            email (str): The email of the user that is deleteing the account
            user_id (str): The id of the user that is to be deleted

        Returns:
            dict: True if the user has been deleted
        """
        headers = {"From": f"{email}"}
        headers.update(self.headers)
        return self.send_request(method="DELETE", path=f"/users/{user_id}/", headers=headers)

    def get_user_by_id(self, user_id: str) -> dict:
        """
            formats the request to allow for the information of a user to be fetched

        Args:
            user_id (str): The id of the user to get information on

        Returns:
            dict: The information on the user
        """
        return self.send_request(method="GET", path=f"/users/{user_id}/")

    def list_users(self) -> dict:
        """
            formatch the request to get a list of all of the users in pagerduty

        Returns:
            dict: This will return a list of user objects
        """
        return self.send_request(method="GET", path="/users/")

    def send_request(
        self, method: str, path: str, params: dict = None, payload: dict = None, headers: dict = None, data: dict = None
    ) -> Union[dict, str]:
        """
            A wrapper with error handling for making requests to the pager duty api

        Args:
            method (str): The type of request that will be made
            path (str): The path that will be appended to the base url
            params (dict, optional): Any paramaters that will be added to the request. Defaults to None.
            payload (dict, optional): Any data that will be added to the json section of the request. Defaults to None.
            headers (dict, optional): Any additional headers that will be added to the request. Defaults to None.
            data (dict, optional): Any data that will be added to the data section of the request. Defaults to None.

        Raises:
            PluginException: If there is an error connecting to the pager duty api or else if there is no valid data returned

        Returns:
            Union[dict, str]:
                dict: The response of the request in json format 
                bool: If the delete request is called then there will be no data returned from the api, so we return True

        """
                 
        if not headers:
            headers = self.headers

        try:
            response = self.session.request(
                method.upper(),
                "https://api.pagerduty.com" + path,
                params=params,
                json=payload,
                headers=headers,
                data=data,
            )

            if method.upper() == "DELETE" and response.status_code == 204:
                return True
            if 200 <= response.status_code < 300:
                return clean(json.loads(response.content))

            self._check_status_code(response)
        except requests.exceptions.HTTPError as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=e)

    def _check_status_code(self, response: dict):
        """
        This will check the status code of the response and the appropriate error message based on the status code will be raised as a PluginError

        Args:
            response (dict): The response object to be checked

        Raises:
            PluginException: The PluginException error will be raised and based on the status code the error messaged will be set, this is based on a set of predefined messages in the insightconnect_plugin_runtime.exceptions class
        """
        if response.status_code == 401:
            raise PluginException(preset=PluginException.Preset.API_KEY, data=response.text)
        if response.status_code == 403:
            raise PluginException(preset=PluginException.Preset.API_KEY, data=response.text)
        if response.status_code == 404:
            raise PluginException(preset=PluginException.Preset.NOT_FOUND, data=response.text)
        if 400 <= response.status_code < 500:
            raise PluginException(
                preset=PluginException.Preset.UNKNOWN,
                data=response.text,
            )
        if response.status_code >= 500:
            raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.text)
        raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
