import os
import json
import shutil
from tempfile import mkdtemp
from base64 import b64decode
from requests import request, HTTPError
import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException


def is_key_field(key_to_check):
    """
    Check if the key passed in matches oen of the known key type fields
    """
    if key_to_check == "id" or key_to_check.endswith("_id") or key_to_check.endswith("_ids"):
        return True
    else:
        return False


def update_id_values_to_integers(data):
    """
    According to the Solarwinds (Samanage) API, Ids can be returned as either integers or strings
    In order to ensure consistency and allow output checking, convert all ids to be strings
    """
    for key, value in data.items():
        if isinstance(value, dict):
            # Item is a dict - recursive use of function
            update_id_values_to_integers(value)
        elif isinstance(value, list):
            # Item is a list - recursive use of function if dict else update any id fields
            for i in range(0, len(value)):
                if isinstance(value[i], dict):
                    update_id_values_to_integers(value[i])
                elif is_key_field(key):
                    value[i] = int(value[i])

        else:
            if is_key_field(key):
                # Item is a key field - update
                data[key] = int(value)


class SamanageAPI:
    def __init__(self, token, is_eu_customer, logger):
        self.token = token
        self.logger = logger
        self.api_url = "https://apieu.samanage.com/" if is_eu_customer else "https://api.samanage.com/"
        # Test the connection
        # self.list_incidents_check()

    def list_incidents_check(self):
        # This function is to check that an API call can be successfully made  - no cleaning of the output is required
        response = self._call_api("GET", "incidents")
        return response

    def list_incidents(self):
        response = self._call_api("GET", "incidents")
        # Update response data to change ids to integers if necessary
        for item in response:
            update_id_values_to_integers(item)
        return response

    def get_incident(self, incident_id):
        url = "incidents/{}".format(incident_id)

        response = self._call_api("GET", url, params={"layout": "long", "audit_archive": True})
        # Update response data to change ids to integers if necessary
        update_id_values_to_integers(response)
        return response

    def add_tags_to_incident(self, incident_id, tags):
        url = "incidents/{}".format(incident_id)
        json = {"incident": {"add_to_tag_list": ", ".join(tags)}}
        response = self._call_api("PUT", url, json=json, params={"layout": "long", "audit_archive": True})
        # Update response data to change ids to integers if necessary
        update_id_values_to_integers(response)
        return response

    def create_incident(
        self,
        name,
        requester,
        priority,
        description=None,
        due_at=None,
        assignee=None,
        incidents=None,
        problem=None,
        solutions=None,
        category_name=None,
    ):
        url = "incidents"

        json = {
            "incident": {
                "name": name,
                "requester": {"email": requester},
                "priority": priority,
                "description": description,
                "due_at": due_at,
                "assignee": {"email": assignee} if assignee else None,
                "incidents": [{"number": i} for i in incidents] if incidents else None,
                "problem": {"number": problem} if problem else None,
                "solutions": [{"number": i} for i in solutions] if solutions else None,
                "category": {"name": category_name} if category_name else None,
            }
        }
        json = insightconnect_plugin_runtime.helper.clean(json)
        response = self._call_api("POST", url, json=json, params={"layout": "long", "audit_archive": True})
        # Update response data to change ids to integers if necessary
        update_id_values_to_integers(response)
        return response

    def delete_incident(self, incident_id):
        url = "incidents/{}".format(incident_id)
        return self._call_api("DELETE", url)

    def comment_incident(self, incident_id, body, is_private):
        url = "incidents/{}/comments".format(incident_id)
        json = {"comment": {"body": body, "is_private": is_private}}

        response = self._call_api("POST", url, json=json)
        # Update response data to change ids to integers if necessary
        update_id_values_to_integers(response)
        return response

    def get_comments(self, incident_id):
        url = "incidents/{}/comments".format(incident_id)

        response = self._call_api("GET", url)
        # Update response data to change ids to integers if necessary
        for value in response:
            update_id_values_to_integers(value)
        return response

    def assign_incident(self, incident_id, assignee):
        url = "incidents/{}".format(incident_id)

        json = {"incident": {"assignee": {"email": assignee}}}
        response = self._call_api("PUT", url, json=json, params={"layout": "long", "audit_archive": True})
        # Update response data to change ids to integers if necessary
        update_id_values_to_integers(response)
        return response

    def change_incident_state(self, incident_id, state):
        url = "incidents/{}".format(incident_id)

        json = {"incident": {"state": state}}
        response = self._call_api("PUT", url, json=json, params={"layout": "long", "audit_archive": True})
        # Update response data to change ids to integers if necessary
        update_id_values_to_integers(response)
        return response

    def attach_file_to_incident(self, incident_id, attachment_bytes, attachment_name):
        self.logger.info("Attaching a file to an incident {}".format(incident_id))
        try:
            temp_dir = mkdtemp()
            file_path = os.path.join(temp_dir, attachment_name)

            with open(file_path, "w+b") as temp_file:
                temp_file.write(b64decode(attachment_bytes))

            curl_command = (
                'curl -H "X-Samanage-Authorization: Bearer {}" '
                '-F "file[attachable_type]=Incident" '
                '-F "file[attachable_id]={}" '
                '-F "file[attachment]=@{}" '
                '-H "Accept: application/vnd.samanage.v2.1+json" '
                '-H "Content-Type: multipart/form-data" --insecure '
                "-X POST {}attachments.json"
            ).format(self.token, incident_id, file_path, self.api_url)
            result = insightconnect_plugin_runtime.helper.exec_command(curl_command)

            shutil.rmtree(temp_dir)
        except Exception as e:
            raise PluginException(
                cause="Failed creating a temporary file: {}".format(e),
                assistance="Check if a temporary file can be created",
            )

        if result["rcode"] != 0:
            raise PluginException(
                cause="Failure running curl command while attaching file: {}".format(result["stderr"]),
                assistance="Check if there are sufficient permissions for the curl command to run",
            )

        try:
            attachment = json.loads(result["stdout"])
            update_id_values_to_integers(attachment)
            return attachment
        except json.JSONDecodeError:
            raise PluginException(
                cause="Failure in return response while attaching file: {}".format(result["stdout"]),
                assistance="Check if there are sufficient permissions for file attachment",
            )

    def list_users(self):
        response = self._call_api("GET", "users")
        # Update response data to change ids to integers if necessary
        for item in response:
            update_id_values_to_integers(item)
        return response

    def create_user(self, email, name=None, phone=None, mobile_phone=None, role=None, department=None):
        json = {
            "user": {
                "email": email,
                "name": name,
                "phone": phone,
                "mobile_phone": mobile_phone,
                "role": {"name": role} if role else None,
                "department": {"name": department} if department else None,
            }
        }
        json = insightconnect_plugin_runtime.helper.clean(json)
        response = self._call_api("POST", "users", json=json)
        # Update response data to change ids to integers if necessary
        update_id_values_to_integers(response)
        return response

    def delete_user(self, user_id):
        url = "users/{}".format(user_id)
        return self._call_api("DELETE", url)

    def _call_api(self, method, url, params=None, json=None, data=None, files=None):
        api_url = "{}{}.json".format(self.api_url, url)
        self.logger.info("Calling API URL {}".format(api_url))

        try:
            response = request(
                method,
                api_url,
                params=params,
                data=data,
                json=json,
                files=files,
                headers={
                    "X-Samanage-Authorization": "Bearer {}".format(self.token),
                    "Accept": "application/vnd.samanage.v2.1+json",
                },
            )
            response.raise_for_status()
        except HTTPError:
            if response.status_code == 401:
                # Auth failure returns: HTTP/1.1" 401 None b''
                if not response.content:
                    raise ConnectionTestException(preset=ConnectionTestException.Preset.API_KEY)
            raise PluginException(
                cause="API returned an error: {} {}".format(response.status_code, response.content),
                assistance="Check input and retry. If this error continues contact support",
            )
        return insightconnect_plugin_runtime.helper.clean(response.json())
