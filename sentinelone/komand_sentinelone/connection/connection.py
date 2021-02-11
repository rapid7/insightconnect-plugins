import insightconnect_plugin_runtime
import requests
from .schema import ConnectionSchema, Input

from komand_sentinelone.util.api import SentineloneAPI
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
import zipfile
import io
import base64
import time
from komand_sentinelone.util.helper import Helper


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.username = None
        self.password = None
        self.url = None
        self.api_version = None
        self.token = None

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

    def get_auth_token(self, url, username, password, version="2.1"):
        # TODO: Need to make a token timeout here for 7 days
        final_url = f"{url}web/api/v{version}/users/login"

        auth_headers = {
            "username": username,
            "password": password
        }

        r = requests.post(final_url, json=auth_headers)
        if r.status_code == 401:
            raise ConnectionTestException(
                cause=f"Could not authorize with SentinelOne instance at: {final_url}.",
                assistance="Your 'username' in connection configuration should be an e-mail address. Check if your e-mail address is correct. Response was: " + r.text
            )

        token = ""

        # Some consoles do not support v2.1 but some actions are not included in 2.0
        # Instead, try getting an auth token from 2.1 first, then rollback to 2.0 if needed
        # Find the list of supported consoles for each API in the SentinelOne API docs
        if r.status_code != 200:
            if version == "2.1":
                self.logger.info("API v2.1 failed... trying v2.0")
                token = self.get_auth_token(url, username, password, version="2.0")

            # We know the connection failed when both 2.1 and 2.0 do not give 200 responses
            if not token:
                raise ConnectionTestException(
                    cause=f"Could not authorize with SentinelOne instance at: {final_url}.",
                    assistance=f"Response was: {r.text}"
                )

        if version == "2.0":
            return r.json().get('data').get('token')

        # When we do not have a token, we know that 2.1 responded with no problems
        # If we do, we know that it came from 2.0 and we can use that in our actions
        if token:
            self.token = token
            self.api_version = "2.0"
        else:
            self.token = r.json().get('data').get('token')
            self.api_version = "2.1"

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

    def agents_summary(self, site_ids, account_ids):
        return self._call_api("GET", "private/agents/summary", None, {"siteIds": site_ids, "accountIds": account_ids})

    def agents_action(self, action: str, agents_filter: str):
        return self._call_api("POST", f"agents/actions/{action}", {"filter": agents_filter})

    def download_file(self, agent_filter: dict, password: str):
        self.get_auth_token(self.url, self.username, self.password)
        agent_filter["activityTypes"] = 86
        agent_filter["sortBy"] = "createdAt"
        agent_filter["sortOrder"] = "desc"
        activities = self.activities_list(agent_filter)
        while not activities["data"]:
            self.logger.info("Waiting 5 seconds for successful threat file upload...")
            time.sleep(5)
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
        return self._call_api("POST", f"private/agents/support-actions/{action}", {
            "filter": agents_filter,
            "data": {"module": module}
        })

    def get_threat_summary(self, limit: int = 1000):
        first_page_endpoint = f"threats?limit={limit}"

        # API v2.0 and 2.1 have different responses -- revert to 2.0
        threats = self._call_api("GET", first_page_endpoint, override_api_version="2.0")
        all_threads_data = threats["data"]
        next_cursor = threats["pagination"]["nextCursor"]

        while next_cursor:
            next_threats = self._call_api("GET", f"{first_page_endpoint}&cursor={next_cursor}", override_api_version="2.0")
            all_threads_data += next_threats["data"]
            next_cursor = next_threats["pagination"]["nextCursor"]

        threats["data"] = all_threads_data
        return threats

    def blacklist_by_content_hash(self, hash_value: str):
        endpoint = f"{self.url}web/api/v{self.api_version}/threats/add-to-blacklist"
        self.logger.info("Attempting to blacklist file: " + hash_value)
        self.logger.info("Using endpoint: " + endpoint)

        headers = self.make_token_header()
        body = {
            "filter": {
                "contentHashes": hash_value
            },
            "data": {
                "targetScope": "site"
            }
        }

        results = requests.post(endpoint, json=body, headers=headers)
        if results.status_code != 200:
            raise PluginException(cause="Could not blacklist file hash.",
                                  assistance=f"Result was: {results.text}")

        return results.json()

    def create_ioc_threat(self, hash_, group_id, path, agent_id, note=""):
        body = {
            "data": [{
                "hash": hash_,
                "groupId": group_id,
                "path": path,
                "agentId": agent_id,
                "note": note,
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
        # Mark as threat does not exist in v2.1
        return self._call_api(
            "POST", "threats/mark-as-benign", body, override_api_version="2.0"
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

        # Mark as threat does not exist in v2.1
        return self._call_api(
            "POST", "threats/mark-as-threat", body, override_api_version="2.0"
        )["data"]["affected"]

    def get_threats(self, params):
        # GET /threats has different response schemas for 2.1 and 2.0
        # Use 2.0 endpoint to be consistent and support as many S1 consoles as possible
        return self._call_api("GET", "threats", params=params, override_api_version="2.0")

    def create_blacklist_item(self, blacklist_hash: str, description: str):
        sites = self._call_api("GET", "sites").get("data", {}).get("sites", [])
        site_ids = []
        for site in sites:
            site_ids.append(site.get("id"))
        errors = []

        already_blacklisted = self.get_existing_blacklist(blacklist_hash)

        if already_blacklisted:
            self.logger.info(f"{blacklist_hash} has already been blacklisted.")
        else:
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

    def get_existing_blacklist(self, blacklist_hash: str):
        ids = self.get_item_ids_by_hash(blacklist_hash)
        ids = Helper.join_or_empty(ids)
        if not ids:
            return False

        response = self._call_api("GET", "restrictions", params={
            "type": "black_hash",
            "ids": ids,
        })

        existing_os_types = []
        for blacklist_entry in response.get("data", []):
            existing_os_types.append(blacklist_entry.get("osType"))

        return set(existing_os_types) == {"linux", "windows", "macos"}

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

        errors = "\n".join(response.get("errors"))

        raise PluginException(cause="An error occurred when trying to unblacklist.",
                              assistance=f"The following error(s) occurred: {errors}")

    def delete_blacklist_item_by_hash(self, item_ids: str):
        return self._call_api("DELETE", "restrictions", json={
            "data": {
                "type": "black_hash",
                "ids": item_ids
            }
        }).get("errors", [])

    def _call_api(self, method, endpoint, json=None, params=None, full_response: bool = False,
                  override_api_version: str = ""):

        # We prefer to use the same api version from the token creation,
        # But some actions require 2.0 and not 2.1 (and vice versa), in that case just pass in the right version
        api_version = self.api_version
        if override_api_version:
            api_version = override_api_version
        endpoint = self.url + f"web/api/v{api_version}/" + endpoint

        headers = self.make_token_header()

        if json:
            json = insightconnect_plugin_runtime.helper.clean(json)
        if params:
            params = insightconnect_plugin_runtime.helper.clean(params)

        response = requests.request(
            method, endpoint, json=json, params=params, headers=headers
        )

        try:
            response.raise_for_status()
            if full_response:
                return response

            return response.json()
        except requests.HTTPError:
            raise PluginException(cause="API call failed: " + response.text)

    def test(self):
        self.get_auth_token(self.url, self.username, self.password)
        return
