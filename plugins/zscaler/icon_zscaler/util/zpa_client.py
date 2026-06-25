from insightconnect_plugin_runtime.exceptions import PluginException

from icon_zscaler.util.base_client import BaseClient


class ZPAClient(BaseClient):
    """Zscaler Private Access (ZPA) client using OneAPI OAuth 2.0 authentication."""

    def __init__(self, client_id: str, private_key: str, vanity_domain: str, cloud: str, logger: object):
        super().__init__(client_id, private_key, vanity_domain, cloud, logger)
        self.service_prefix = "/zpa/api/v1"

    def list_application_segments(self, next_link: str = None) -> dict:
        """List ZPA application segments with optional pagination.

        Args:
            next_link: Full URL for the next page of results. If provided, used directly.

        Returns:
            Dict containing application segments and optional next_link for pagination.
        """
        if next_link:
            return self._call_api("GET", next_link, headers={"Authorization": f"Bearer {self._get_token()}"}).json()
        return self._make_request("GET", "application").json()

    def get_application_segment(self, segment_id: str) -> dict:
        """Get a specific ZPA application segment by ID.

        Args:
            segment_id: The unique identifier of the application segment.

        Returns:
            Dict containing the application segment details.
        """
        return self._make_request("GET", f"application/{segment_id}").json()

    def list_server_groups(self, next_link: str = None) -> dict:
        """List ZPA server groups with optional pagination.

        Args:
            next_link: Full URL for the next page of results. If provided, used directly.

        Returns:
            Dict containing server groups and optional next_link for pagination.
        """
        if next_link:
            return self._call_api("GET", next_link, headers={"Authorization": f"Bearer {self._get_token()}"}).json()
        return self._make_request("GET", "serverGroup").json()

    def get_server_group(self, group_id: str) -> dict:
        """Get a specific ZPA server group by ID.

        Args:
            group_id: The unique identifier of the server group.

        Returns:
            Dict containing the server group details.
        """
        return self._make_request("GET", f"serverGroup/{group_id}").json()

    def test(self) -> dict:
        """Test connectivity to the ZPA API by listing application segments.

        Returns:
            Dict with success status.

        Raises:
            PluginException: If the test request fails.
        """
        self._make_request("GET", "application")
        return {"success": True}
