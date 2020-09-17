import komand
import requests
from .schema import ConnectionSchema, Input

from komand_sentinelone.util.api import SentineloneAPI
from komand.exceptions import ConnectionTestException, PluginException
import zipfile
import io
import base64


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.username = None
        self.password = None
        self.url = None

    def connect(self, params):
        """
        Connection config params are supplied as a dict in
        params or also accessible in self.parameters['key']

        The following will setup the var to be accessed
          self.blah = self.parameters['blah']
        in the action and trigger files as:
          blah = self.connection.blah
        """
        self.logger.info("Connect: Connecting...")

        self.username = params.get(Input.CREDENTIALS).get('username')
        self.password = params.get(Input.CREDENTIALS).get('password')
        self.url = params.get(Input.URL)

        index = self.url.find("/", self._get_start_index(self.url))
        if index >= 0:
            self.url = self.url[:index]

        # Add trailing slash if needed
        if not self.url.endswith("/"):
            self.url = self.url + "/"

        token = self.get_auth_token(self.url, self.username, self.password)
        self.client = SentineloneAPI(self.url, self.make_token_header())
        self.logger.info("Token: " + "*************" + str(token[len(token) - 5:len(token)]))

    @staticmethod
    def _get_start_index(url):
        if url.startswith("https://"):
            return 9
        return 0

    def get_auth_token(self, url, username, password):
        # TODO: Need to make a token timeout here for 7 days
        final_url = url + "web/api/v2.0/users/login"

        auth_headers = {
            "username": username,
            "password": password
        }

        r = requests.post(final_url, json=auth_headers)
        if r.status_code == 401:
            raise ConnectionTestException(
                cause="Could not authorize with SentinelOne instance at: " + final_url,
                assistance="Your 'username' in connection configuration should be an e-mail address. Check if your e-mail address is correct. Response was: " + r.text
            )
        if r.status_code is not 200:
            raise ConnectionTestException(
                cause="Could not authorize with SentinelOne instance at: " + final_url,
                assistance="Response was: " + r.text
            )

        self.token = r.json().get('data').get('token')

        return self.token

    def make_token_header(self):
        self.header = {
            'Authorization': 'Token %s' % (self.token),
            'Content-Type': 'application/json',
        }

        return self.header

    def activities_list(self, parameters):
        return self._call_api("GET", "activities", None, parameters)

    def name_available(self, name):
        return self._call_api("GET", "private/accounts/name-available", None, {"name": name})

    def activities_types(self):
        return self._call_api("GET", "activities/types")

    def ad_settings(self, parameters):
        return self._call_api("GET", "settings/active-directory", None, parameters)

    def agent_info(self, identifier: str):
        return self._call_api("GET", "settings/active-directory", None, {"id": identifier})

    def apps_by_agent_ids(self, identifiers: str):
        return self._call_api("GET", "agents/applications", None, {"ids": identifiers})

    def agents_processes(self, identifiers: str):
        return self._call_api("GET", "agents/processes", None, {"ids": identifiers})

    def agents_summary(self, site_ids, account_ids):
        return self._call_api("GET", "private/agents/summary", None, {"siteIds": site_ids, "accountIds": account_ids})

    def agents_action(self, action: str, agents_filter: str):
        return self._call_api("POST", "agents/actions/{}".format(action), {"filter": agents_filter})

    def download_file(self, agent_filter: dict, password: str):
        self.get_auth_token(self.url, self.username, self.password)
        agent_filter["activityTypes"] = 86
        agent_filter["sortBy"] = "createdAt"
        agent_filter["sortOrder"] = "desc"
        activities = self.activities_list(agent_filter)
        self.get_auth_token(self.url, self.username, self.password)
        response = self._call_api("GET", activities["data"][0]["data"]["filePath"][1:], full_response=True)
        downloaded_zipfile = zipfile.ZipFile(io.BytesIO(response.content))
        downloaded_zipfile.setpassword(password.encode("UTF-8"))

        return {
            "filename": activities["data"][-1]["data"]["fileDisplayName"],
            "content": base64.b64encode(downloaded_zipfile.read(downloaded_zipfile.infolist()[-1])).decode("utf-8")
        }

    def threats_fetch_file(self, password: str, agents_filter: dict) -> int:
        self.get_auth_token(self.url, self.username, self.password)
        return self._call_api("POST", "threats/fetch-file", {
            "data": {
                "password": password
            },
            "filter": agents_filter
        })

    def agents_support_action(self, action: str, agents_filter: str, module: str):
        return self._call_api("POST", "private/agents/support-actions/{}".format(action), {
            "filter": agents_filter,
            "data": {"module": module}
        })

    def get_threat_summary(self):
        """ Output a summary of current threats in the system grouped by
        mitigation level. """

        endpoint = self.url + 'web/api/v2.0/threats'
        self.logger.info("Getting summary of threats from: " + endpoint)
        headers = self.make_token_header()
        results = requests.get(endpoint, headers=headers)

        if results.status_code is not 200:
            raise ConnectionTestException(
                cause="Request for threat summary failed at: " + endpoint,
                assistance="Repsonse was: " + results.text
            )

        return results.json()

    def blacklist_by_content_hash(self, hash_value: str):
        endpoint = self.url + 'web/api/v2.0/threats/add-to-blacklist'
        self.logger.info("Attempting to blacklist file: " + hash_value)
        self.logger.info("Using endpoint: " + endpoint)

        headers = self.make_token_header()
        body = {
            "filter": {
                "contentHash": hash_value
            },
            "data": {
                "targetScope": "site"
            }
        }

        results = requests.post(endpoint, json=body, headers=headers)
        if results.status_code is not 200:
            raise Exception("Could not blacklist file hash, result was: " + results.text)

        self.logger.info("Blacklist result: " + str(results))  # Will nicely print status code
        return results.json()

    def blacklist_by_ioc_hash(self, hash_value: str, agent_id: str):
        endpoint = self.url + 'web/api/v2.0/private/threats/ioc-add-to-blacklist'
        self.logger.info("Attempting to blacklist IoC hash: " + hash_value)
        self.logger.info("Using endpoint: " + endpoint)

        headers = self.make_token_header()

        # Note: AgentID according to the API is optional, however, api will throw error if omitted
        body = {
            "data": [{
                "hash": hash_value,
                "agentId": agent_id
            }]
        }

        results = requests.post(endpoint, json=body, headers=headers)
        if results.status_code is not 200:
            raise Exception("Could not blacklist IoC hash, result was: " + results.text)

        self.logger.info("Blacklist result: " + str(results))  # Will nicely print status code
        return results.json()

    def create_ioc_threat(
            self, hash_, group_id, path, agent_id,
            annotation=None, annotation_url=None
    ):
        body = {
            "data": [{
                "hash": hash_,
                "group_id": group_id,
                "path": path,
                "agent_id": agent_id,
                "annotation": annotation,
                "annotation_url": annotation_url,
            }]
        }
        response = self._call_api(
            "POST", "private/threats/ioc-create-threats", body
        )

        return response.json()["data"]["affected"]

    def mitigate_threat(self, threat_id, action):
        body = {
            "filter": {
                "ids": [threat_id]
            }
        }
        action_url = "threats/mitigate/" + action
        return self._call_api("POST", action_url, body)["data"]["affected"]

    def mark_as_benign(self, threat_id, whitening_option, target_scope):
        body = {
            "filter": {
                "ids": [threat_id]
            },
            "data": {
                "whiteningOption": whitening_option,
                "targetScope": target_scope
            }
        }
        return self._call_api(
            "POST", "threats/mark-as-benign", body
        )["data"]["affected"]

    def mark_as_threat(self, threat_id, whitening_option, target_scope):
        body = {
            "filter": {
                "ids": [threat_id]
            },
            "data": {
                "whiteningOption": whitening_option,
                "targetScope": target_scope
            }
        }
        return self._call_api(
            "POST", "threats/mark-as-threat", body
        )["data"]["affected"]

    def get_threats(self, params):
        return self._call_api("GET", "threats", params=params)

    def create_blacklist_item(self, blacklist_hash: str, description: str):
        sites = self._call_api("GET", "sites").get("data", {}).get("sites", [])
        site_ids = []
        for site in sites:
            site_ids.append(site.get("id"))
        errors = []
        for os_type in ["linux", "windows", "macos"]:
            errors.extend(self._call_api("POST", "restrictions", json={
                "data": {
                    "value": blacklist_hash,
                    "type": "black_hash",
                    "osType": os_type,
                    "description": description
                },
                "filter": {
                    "siteIds": site_ids
                }
            }).get("errors", []))

        return errors

    def get_item_ids_by_hash(self, blacklist_hash: str):
        response = self._call_api("GET", "restrictions", params={
            "type": "black_hash",
            "value": blacklist_hash
        })

        if len(response.get("errors", [])) == 0:
            ids = []
            restrictions = response.get("data", [])
            for restriction in restrictions:
                ids.append(restriction.get("id"))
            return ids

        raise PluginException(cause="The hash does not exist to unblacklist.", assistance="Please enter a hash that has been blacklisted.")

    def delete_blacklist_item_by_hash(self, item_ids: str):
        return self._call_api("DELETE", "restrictions", json={
          "data": {
            "type": "black_hash",
            "ids": item_ids
          }
        }).get("errors", [])

    def _call_api(self, method, endpoint, json=None, params=None, full_response: bool = False):
        endpoint = self.url + "web/api/v2.0/" + endpoint
        headers = self.make_token_header()

        if json:
            json = komand.helper.clean(json)
        if params:
            params = komand.helper.clean(params)

        response = requests.request(
            method, endpoint, json=json, params=params, headers=headers
        )

        try:
            response.raise_for_status()
            if full_response:
                return response

            return response.json()
        except requests.HTTPError:
            raise Exception("API call failed: " + response.text)

    def test(self):
        self.get_auth_token(self.url, self.username, self.password)
        return
