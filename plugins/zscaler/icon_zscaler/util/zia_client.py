import json

from requests import Response

from icon_zscaler.util.base_client import BaseClient

JSON_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}


class ZIAClient(BaseClient):
    """ZIA (Zscaler Internet Access) client for OneAPI.

    Handles all ZIA-specific API operations including URL lookup, blacklist management,
    sandbox reports, user management, URL categories, DLP, firewall, logs, and threat feeds.
    """

    def __init__(self, client_id: str, private_key: str, vanity_domain: str, cloud: str, logger: object):
        super().__init__(client_id, private_key, vanity_domain, cloud, logger)
        self.service_prefix = "/zia/api/v1"

    # -------------------------------------------------------------------------
    # Existing methods (migrated from ZscalerAPI with identical signatures/returns)
    # -------------------------------------------------------------------------

    def url_lookup(self, lookup_url: list):
        """Look up URL categorizations.

        Returns: list of dicts (response JSON)
        """
        response = self._make_request("POST", "urlLookup", data=json.dumps(lookup_url), headers=JSON_HEADERS.copy())
        return response.json()

    def blacklist_url(self, blacklist_step: str, urls: list) -> bool:
        """Add or remove URLs from the blacklist.

        Returns: bool (True if 200 <= status < 300)
        """
        response = self._make_request(
            "POST",
            f"security/advanced/blacklistUrls?action={blacklist_step}",
            data=json.dumps({"blacklistUrls": urls}),
            headers=JSON_HEADERS.copy(),
        )
        return 200 <= response.status_code < 300

    def get_blacklist_url(self):
        """Get the list of blacklisted URLs.

        Returns: dict with blacklistUrls (response JSON)
        """
        return self._make_request("GET", "security/advanced").json()

    def get_hash_report(self, hash_: str):
        """Get full sandbox report for a hash.

        Returns: dict (response JSON)
        """
        return self._make_request("GET", f"sandbox/report/{hash_}?details=full").json()

    def get_users(self, filter_params: dict) -> dict:
        """Get users with optional filter parameters.

        Returns: dict/list (response JSON)
        """
        return self._make_request(method="GET", endpoint="users", params=filter_params).json()

    def search_department(self, department_name: str) -> list:
        """Search for departments by name.

        Returns: list (response JSON)
        """
        return self._make_request(method="GET", endpoint="departments", params={"search": department_name}).json()

    def search_groups(self) -> list:
        """Get all groups.

        Note: The search string used to match against a group's name or comments attributes.
        Returns: list (response JSON)
        """
        return self._make_request(method="GET", endpoint="groups").json()

    def create_user(self, user_data: dict) -> dict:
        """Create a new user.

        Returns: dict (response JSON)
        """
        return self._make_request(
            method="POST", endpoint="users", data=json.dumps(user_data), headers=JSON_HEADERS.copy()
        ).json()

    def delete_user(self, user_id: int) -> bool:
        """Delete a user by ID.

        Returns: bool (True if 200 <= status < 300)
        """
        response = self._make_request(method="DELETE", endpoint=f"users/{user_id}")
        return 200 <= response.status_code < 300

    def list_url_categories(self, custom_only: bool = False) -> list:
        """List URL categories, optionally filtering to custom only.

        Returns: list (response JSON)
        """
        params = {"customOnly": True} if custom_only else {}
        return self._make_request("GET", "urlCategories", params=params).json()

    def get_url_category_by_id(self, url_category_id: str) -> dict:
        """Get a URL category by its ID.

        Returns: dict (response JSON)
        """
        return self._make_request("GET", f"urlCategories/{url_category_id}").json()

    def update_urls_in_url_category(self, category_id: str, action: str, url_category_data: object) -> dict:
        """Update URLs in a URL category.

        Returns: dict (response JSON)
        """
        return self._make_request(
            "PUT",
            f"urlCategories/{category_id}",
            data=json.dumps(url_category_data),
            params={"action": action},
            headers=JSON_HEADERS.copy(),
        ).json()

    def activate_configuration(self) -> Response:
        """Activate the current ZIA configuration changes.

        Returns: Response object
        """
        return self._make_request("POST", "status/activate")

    # -------------------------------------------------------------------------
    # New methods (for new SOC analyst actions)
    # -------------------------------------------------------------------------

    def get_dlp_incidents(self, start_time: str, end_time: str, next_link: str = None) -> dict:
        """Get DLP incidents within a time range.

        Args:
            start_time: Start time for the query range.
            end_time: End time for the query range.
            next_link: Full URL for pagination continuation.

        Returns: dict with incidents and next_link
        """
        if next_link:
            response = self._call_api("GET", next_link, headers={"Authorization": f"Bearer {self._get_token()}"})
            return response.json()

        params = {"startTime": start_time, "endTime": end_time}
        return self._make_request("GET", "dlp/incidents", params=params).json()

    def list_firewall_rules(self, next_link: str = None) -> dict:
        """List firewall filtering rules.

        Args:
            next_link: Full URL for pagination continuation.

        Returns: dict with rules and next_link
        """
        if next_link:
            response = self._call_api("GET", next_link, headers={"Authorization": f"Bearer {self._get_token()}"})
            return response.json()

        return self._make_request("GET", "firewallRules").json()

    def get_firewall_rule(self, rule_id: int) -> dict:
        """Get a specific firewall rule by ID.

        Returns: dict (response JSON)
        """
        return self._make_request("GET", f"firewallRules/{rule_id}").json()

    def create_firewall_rule(self, rule_data: dict) -> dict:
        """Create a new firewall filtering rule.

        Returns: dict (response JSON)
        """
        return self._make_request(
            "POST", "firewallRules", data=json.dumps(rule_data), headers=JSON_HEADERS.copy()
        ).json()

    def update_firewall_rule(self, rule_id: int, rule_data: dict) -> dict:
        """Update an existing firewall filtering rule.

        Returns: dict (response JSON)
        """
        return self._make_request(
            "PUT", f"firewallRules/{rule_id}", data=json.dumps(rule_data), headers=JSON_HEADERS.copy()
        ).json()

    def get_web_logs(self, start_time: str, end_time: str, next_link: str = None) -> dict:
        """Get web transaction logs within a time range.

        Args:
            start_time: Start time for the query range.
            end_time: End time for the query range.
            next_link: Full URL for pagination continuation.

        Returns: dict with logs and next_link
        """
        if next_link:
            response = self._call_api("GET", next_link, headers={"Authorization": f"Bearer {self._get_token()}"})
            return response.json()

        params = {"startTime": start_time, "endTime": end_time}
        return self._make_request("GET", "web/logs", params=params).json()

    def get_firewall_logs(self, start_time: str, end_time: str, next_link: str = None) -> dict:
        """Get firewall logs within a time range.

        Args:
            start_time: Start time for the query range.
            end_time: End time for the query range.
            next_link: Full URL for pagination continuation.

        Returns: dict with logs and next_link
        """
        if next_link:
            response = self._call_api("GET", next_link, headers={"Authorization": f"Bearer {self._get_token()}"})
            return response.json()

        params = {"startTime": start_time, "endTime": end_time}
        return self._make_request("GET", "firewall/logs", params=params).json()

    def submit_threat_feed(self, feed_type: str, indicators: list, description: str = None) -> dict:
        """Submit custom IoCs to the threat feed.

        Args:
            feed_type: Type of indicators (e.g., "IP", "DOMAIN", "URL").
            indicators: List of indicator values to submit.
            description: Optional description for the submission.

        Returns: dict with success status and count
        """
        payload = {
            "feedType": feed_type,
            "indicators": indicators,
        }
        if description:
            payload["description"] = description

        return self._make_request("POST", "threatFeeds", data=json.dumps(payload), headers=JSON_HEADERS.copy()).json()

    # -------------------------------------------------------------------------
    # Status / Test connectivity
    # -------------------------------------------------------------------------

    def get_status(self) -> Response:
        """Get ZIA service status.

        Returns: Response object
        """
        return self._make_request("GET", "status")

    def test(self) -> dict:
        """Test connectivity to ZIA API via status endpoint.

        Returns: dict (response JSON from /zia/api/v1/status)
        """
        response = self._make_request("GET", "status")
        return response.json()
