import os
import json
import shutil
from tempfile import mkdtemp
from base64 import b64decode
from requests import request, HTTPError
import komand
from komand.exceptions import ConnectionTestException


class SamanageAPI:
    def __init__(self, token, is_eu_customer, logger):
        self.token = token
        self.logger = logger
        self.api_url = (
            'https://apieu.samanage.com/' if is_eu_customer else
            'https://api.samanage.com/'
        )
        # Test the connection
        self.list_incidents()

    def list_incidents(self):
        return self._call_api('GET', 'incidents')

    def get_incident(self, incident_id):
        url = 'incidents/{}'.format(incident_id)

        return self._call_api('GET', url, params={
            'layout': 'long', 'audit_archive': True
        })

    def add_tags_to_incident(self, incident_id, tags):
        url = 'incidents/{}'.format(incident_id)
        json = {'incident': {'add_to_tag_list': ', '.join(tags)}}

        return self._call_api('PUT', url, json=json, params={
            'layout': 'long', 'audit_archive': True
        })

    def create_incident(
        self, name, requester, priority, description=None, due_at=None,
        assignee=None, incidents=None, problem=None, solutions=None,
        category_name=None
    ):
        url = 'incidents'

        json = {
            'incident': {
                'name': name,
                'requester': {'email': requester},
                'priority': priority,
                'description': description,
                'due_at': due_at,
                'assignee': {'email': assignee} if assignee else None,
                'incidents': [
                    {'number': i} for i in incidents
                ] if incidents else None,
                'problem': {'number': problem} if problem else None,
                'solutions': [
                    {'number': i} for i in solutions
                ] if solutions else None,
                'category': {'name': category_name} if category_name else None,
            }
        }
        json = komand.helper.clean(json)

        return self._call_api('POST', url, json=json, params={
            'layout': 'long', 'audit_archive': True
        })

    def comment_incident(self, incident_id, body, is_private):
        url = 'incidents/{}/comments'.format(incident_id)
        json = {'comment': {'body': body, 'is_private': is_private}}

        return self._call_api('POST', url, json=json)

    def get_comments(self, incident_id):
        url = 'incidents/{}/comments'.format(incident_id)

        return self._call_api('GET', url)

    def assign_incident(self, incident_id, assignee):
        url = 'incidents/{}'.format(incident_id)

        json = {'incident': {'assignee': {'email': assignee}}}

        return self._call_api('PUT', url, json=json, params={
            'layout': 'long', 'audit_archive': True
        })

    def change_incident_state(self, incident_id, state):
        url = 'incidents/{}'.format(incident_id)

        json = {'incident': {'state': state}}

        return self._call_api('PUT', url, json=json, params={
            'layout': 'long', 'audit_archive': True
        })

    def attach_file_to_incident(
        self, incident_id, attachment_bytes, attachment_name
    ):
        self.logger.info(
            'Attaching a file to an incident {}'.format(incident_id)
        )
        try:
            temp_dir = mkdtemp()
            file_path = os.path.join(temp_dir, attachment_name)

            with open(file_path, 'w+b') as temp_file:
                temp_file.write(b64decode(attachment_bytes))

            curl_command = (
                'curl -H "X-Samanage-Authorization: Bearer {}" '
                '-F "file[attachable_type]=Incident" '
                '-F "file[attachable_id]={}" '
                '-F "file[attachment]=@{}" '
                '-H "Accept: application/vnd.samanage.v2.1+json" '
                '-H "Content-Type: multipart/form-data" --insecure '
                '-X POST {}attachments.json'
            ).format(self.token, incident_id, file_path, self.api_url)
            result = komand.helper.exec_command(curl_command)

            shutil.rmtree(temp_dir)
        except Exception as e:
            raise Exception('Failed create a temp file: {}'.format(e))

        if result['rcode'] != 0:
            raise Exception('Failed run cURL: {}'.format(result['stderr']))

        try:
            attachment = json.loads(result['stdout'])
            return attachment
        except json.JSONDecodeError:
            raise Exception(
                'Failed to attach a file: {}'.format(result['stdout'])
            )

    def list_users(self):
        return self._call_api('GET', 'users')

    def create_user(
        self, email, name=None, phone=None, mobile_phone=None, role=None,
        department=None
    ):
        json = {
            'user': {
                'email': email,
                'name': name,
                'phone': phone,
                'mobile_phone': mobile_phone,
                'role': {'name': role} if role else None,
                'department': {'name': department} if department else None
            }
        }
        json = komand.helper.clean(json)

        return self._call_api('POST', 'users', json=json)

    def delete_user(self, user_id):
        url = 'users/{}'.format(user_id)
        return self._call_api('DELETE', url)

    def _call_api(
        self, method, url, params=None, json=None, data=None, files=None
    ):
        api_url = '{}{}.json'.format(self.api_url, url)

        self.logger.info('Calling API URL {}'.format(api_url))

        try:
            response = request(
                method, api_url,
                params=params, data=data, json=json, files=files,
                headers={
                    'X-Samanage-Authorization': 'Bearer {}'.format(self.token),
                    'Accept': 'application/vnd.samanage.v2.1+json'
                }
            )
            response.raise_for_status()
        except HTTPError:
            if response.status_code == 401:
                # Auth failure returns: HTTP/1.1" 401 None b''
                if not response.content:
                    raise ConnectionTestException(preset=ConnectionTestException.Preset.API_KEY)
            raise Exception('API returned an error: {} {}'.format(
                response.status_code, response.content
            ))

        return komand.helper.clean(response.json())
