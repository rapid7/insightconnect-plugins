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

        :param str schedule_id: The id of the schedule that the user info will be fetched for
        :return dict: The Schedule object that is returend from the pagerduty api
        """

        return self.send_request("GET", f"/schedules/{schedule_id}/")

    def resolve_event(self, email: str, incident_id: str) -> dict:
        """
        Formats the request to call for an incident to be resolved

        :param str email: The email address of the user that is resolving the event
        :param str incident_id: The id of the incident to be resolved
        :return dict: The full incident object with its updated values will be returend
        """
        data = {"incident": {"type": "incident", "status": "resolved"}}
        return self.send_request(
            method="PUT", path=f"/incidents/{incident_id}/", data=json.dumps(data), from_email=email
        )

    def acknowledge_event(self, email: str, incident_id: str) -> dict:
        """
        Formats the request to call for an incident to be acknowledged

        :param str email: The email address of the user that is acknowledging the event
        :param str incident_id: The id of the incident to be acknowledged
        :return dict: The full incident object with its updated values will be returend
        """
        data = {"incident": {"type": "incident", "status": "acknowledged"}}
        return self.send_request(
            method="PUT", path=f"/incidents/{incident_id}/", data=json.dumps(data), from_email=email
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

        :param str email: The email of the user triggering the event
        :param str title: The title of the description
        :param dict service: The service id and the type that will be incident will be associated to
        :param dict dict_of_optional_fields: Optional fields that can also be added to an incident, these can include:
                [urgency, incident_key, priority, escalation_policy, conference_bridge, body, assignments]
        :return dict: This will return the full object of the newly created incident
        """
        payload = {"incident": {"type": "incident", "title": title, "service": service}}

        for key, value in dict_of_optional_fields.items():
            if value:
                payload["incident"][key] = value

        return self.send_request(method="POST", path="/incidents/", payload=payload, from_email=email)

    def create_user(
        self,
        from_email: str,
        new_users_email: str,
        name: str,
        dict_of_optional_fields: dict,
    ) -> dict:
        """
        Formats the request to all for a new user to be created

        :param str from_email: The email for the account that is creating the new user
        :param str new_users_email: The email for the new account
        :param str name: The name for the new account
        :param dict dict_of_optional_fields: Optional fields that can also be used when creating a new user, these include:
                [time_zone, color, role, description, job_title, license]
        :return dict: The newly cerated user object
        """
        payload = {"user": {"name": name, "email": new_users_email}}

        for key, value in dict_of_optional_fields.items():
            if value:
                payload["user"][key] = value

        return self.send_request(method="POST", path="/users/", payload=payload, from_email=from_email)

    def delete_user_by_id(self, email: str, user_id: str) -> bool:
        """
        Formats the request to allow for a user to be deleted

        :param str email: The email of the user that is deleteing the account
        :param str user_id: The id of the user that is to be deleted
        :return bool: True if the user has been deleted
        """
        return self.send_request(method="DELETE", path=f"/users/{user_id}/", from_email=email)

    def get_user_by_id(self, user_id: str) -> dict:
        """
        formats the request to allow for the information of a user to be fetched

        :param str user_id: The id of the user to get information on
        :return dict: The information on the user
        """
        return self.send_request(method="GET", path=f"/users/{user_id}/")

    def list_users(self) -> dict:
        """
        Formats the request to get a list of all of the users in pagerduty


        :return dict: This will return a list of user objects
        """
        return self.send_request(method="GET", path="/users/")

    def send_request(
        self,
        method: str,
        path: str,
        params: dict = None,
        payload: dict = None,
        headers: dict = None,
        data: dict = None,
        from_email: str = "",
    ) -> Union[dict, bool]:
        """
        A wrapper with error handling for making requests to the pager duty api

        :param str method: The type of request that will be made
        :param str path: The path that will be appended to the base url
        :param dict params: Any paramaters that will be added to the request, defaults to None
        :param dict payload: Any data that will be added to the json section of the request, defaults to None
        :param dict headers: Any additional headers that will be added to the request, defaults to None
        :param dict data: Any data that will be added to the data section of the request, defaults to None
        :raises PluginException: If there is an error connecting to the pager duty api or else if there is no valid data returned
        :return Union[dict, bool]:
                dict: The response of the request in json format
                bool: If the delete request is called then there will be no data returned from the api, so we return True
        """

        # in the case that the from email is added, we need to update a new headers var and not self.headers
        if not headers:
            headers = {}
            headers.update(self.headers)

        if from_email:
            headers.update({"From": f"{from_email}"})

        self.logger.info(f"{headers = }")

        try:
            response = self.session.request(
                method.upper(),
                "https://api.pagerduty.com" + path,
                params=params,
                json=payload,
                headers=headers,
                data=data,
            )

            if response.status_code == 204:
                return True
            if 200 <= response.status_code < 300:
                return clean(json.loads(response.content))

            self._check_status_code(response)
        except requests.exceptions.HTTPError as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

    def _check_status_code(self, response: dict):
        """
        This will check the status code of the response and the appropriate error message based on the status code will be raised as a PluginError

        :param dict response: The response object to be checked
        :raises PluginException: PluginException: The PluginException error will be raised and based on the status code the error messaged will be set, this is based on a set of predefined messages in the insightconnect_plugin_runtime.exceptions class
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
