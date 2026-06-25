import requests
from typing import Dict, Any, Optional
from insightconnect_plugin_runtime.exceptions import PluginException


class IntelHubAPI:
    """Wrapper class for Rapid7 Intelligence Hub API calls"""

    TIMEOUT = 30

    def __init__(self, connection, logger):
        self.connection = connection
        self.logger = logger
        self.base_url = connection.base_url
        self.headers = connection.get_headers()

    def _make_request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        json_data: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Make an API request to the Intelligence Hub API"""
        url = f"{self.base_url}/{endpoint}"

        try:
            response = requests.request(
                method=method,
                url=url,
                headers=self.headers,
                params=params,
                json=json_data,
                timeout=self.TIMEOUT,
            )

            if response.status_code == 200:
                return response.json()
            elif response.status_code == 401:
                raise PluginException(
                    cause="Unauthorized",
                    assistance="Please verify your API key is valid and has access to Intelligence Hub.",
                )
            elif response.status_code == 403:
                raise PluginException(
                    cause="Forbidden",
                    assistance="Your API key does not have permission to access this resource.",
                )
            elif response.status_code == 404:
                raise PluginException(
                    cause="Resource not found",
                    assistance="The requested resource was not found.",
                )
            elif response.status_code == 429:
                raise PluginException(
                    cause="Rate limit exceeded",
                    assistance="Please wait before making additional requests.",
                )
            elif response.status_code in range(500, 599):
                raise PluginException(
                    cause="Server error",
                    assistance="The Intelligence Hub API is experiencing issues. Please try again later.",
                )
            else:
                raise PluginException(
                    cause=f"Unknown error occurred. Status code: {response.status_code}",
                    assistance=f"Response: {response.text}",
                )
        except requests.exceptions.Timeout:
            raise PluginException(
                cause="Request timed out",
                assistance="The request to the Intelligence Hub API timed out. Please try again.",
            )
        except requests.exceptions.RequestException as e:
            raise PluginException(
                cause=f"Request failed: {str(e)}",
                assistance="Please check your network connection and try again.",
            )

    def search_cves(
        self,
        search: str = "",
        page: int = 1,
        page_size: int = 10,
        cvss_score: str = "",
        exploitable: Optional[bool] = None,
        epss_score: str = "",
        cisa_kev: Optional[bool] = None,
        last_updated: str = "",
    ) -> Dict[str, Any]:
        """
        Search CVEs in the Intelligence Hub database

        Args:
            search: Search query string
            page: Page number (starts at 1)
            page_size: Number of results per page
            cvss_score: Filter by CVSS severity (critical, high, medium, low)
            exploitable: Filter by exploitability
            epss_score: Filter by EPSS score range (e.g., 0-0.5)
            cisa_kev: Filter by CISA KEV catalog
            last_updated: Filter by last updated time (e.g., 'last 24 hours', 'last 72 hours')

        Returns:
            Dictionary containing CVE results and pagination info
        """
        params = {
            "page": page,
            "page-size": page_size,
        }

        if search:
            params["search"] = search
        if cvss_score:
            params["cvss-score"] = cvss_score
        if exploitable is not None:
            params["exploitable"] = str(exploitable).lower()
        if epss_score:
            params["epss-score"] = epss_score
        if cisa_kev is not None:
            params["cisa-kev"] = str(cisa_kev).lower()
        if last_updated:
            params["last-updated"] = last_updated

        self.logger.info(f"Searching CVEs with params: {params}")
        return self._make_request("GET", "cve", params=params)

    def get_cve(self, cve_id: str) -> Dict[str, Any]:
        """
        Get detailed information about a specific CVE

        Args:
            cve_id: The CVE identifier (e.g., CVE-2025-12345)

        Returns:
            Dictionary containing CVE details
        """
        self.logger.info(f"Getting CVE: {cve_id}")
        return self._make_request("GET", f"cve/{cve_id}")

    def search_threat_actors(
        self,
        search: str = "",
        page: int = 1,
        page_size: int = 10,
    ) -> Dict[str, Any]:
        """
        Search threat actors in the Intelligence Hub database

        Args:
            search: Search query string (name or alias)
            page: Page number (starts at 1)
            page_size: Number of results per page

        Returns:
            Dictionary containing threat actor results and pagination info
        """
        params = {
            "page": page,
            "page-size": page_size,
        }

        if search:
            params["search"] = search

        self.logger.info(f"Searching threat actors with params: {params}")
        return self._make_request("GET", "threat-actor", params=params)

    def get_threat_actor(self, uuid: str) -> Dict[str, Any]:
        """
        Get detailed information about a specific threat actor

        Args:
            uuid: The threat actor UUID

        Returns:
            Dictionary containing threat actor details
        """
        self.logger.info(f"Getting threat actor: {uuid}")
        return self._make_request("GET", f"threat-actor/{uuid}")

    def get_threat_actor_cves(
        self,
        uuid: str,
        page: int = 1,
        page_size: int = 10,
    ) -> Dict[str, Any]:
        """
        Get CVEs associated with a specific threat actor

        Args:
            uuid: The threat actor UUID
            page: Page number (starts at 1)
            page_size: Number of results per page

        Returns:
            Dictionary containing CVE list and pagination info
        """
        params = {
            "page": page,
            "page-size": page_size,
        }

        self.logger.info(f"Getting CVEs for threat actor: {uuid}")
        return self._make_request("GET", f"threat-actor/{uuid}/cves", params=params)
