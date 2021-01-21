from requests import Session, Request
from json import JSONDecodeError
from komand.exceptions import PluginException


class ThreatGrid:
    def __init__(self, base_url, logger, api_key, ssl_verify=False):
        self._base_url = base_url
        self.logger = logger
        self.api_key = api_key
        self.session = Session()
        self.session.verify = ssl_verify

    def test_api(self):
        return self._call_api(
            "GET",
            "/api/v3/docs",
            action_name="Connection Test",
            params={"api": "/api/v3/users/:login/api-key"},
            authentication="data",
        )

    def _call_api(
        self, method, endpoint, params=None, data=None, json=None, action_name=None, authentication=None, files=None
    ):
        url = self._base_url + endpoint

        # API Key Auth Mux
        if authentication == "data":
            if data:
                data["api_key"] = self.api_key
            else:
                data = {"api_key": self.api_key}
        if authentication == "query":
            if params:
                params["api_key"] = self.api_key
            else:
                params = {"api_key": self.api_key}
        if authentication == "form":
            if files:
                files["api_key"] = self.api_key
            else:
                files = {"api_key": self.api_key}

        # Build request
        req = Request(
            url=url, method=method, params=params, data=data, json=json, headers=self.session.headers, files=files
        )
        # Prep request
        req = req.prepare()
        resp = self.session.send(req)
        if resp.status_code == 401:
            raise PluginException(
                cause=f"ThreatGrid request for {action_name} failed. Invalid API key provided.",
                assistance="Verify your API key is correct and try again.",
            )
        if resp.status_code == 403:
            raise PluginException(
                cause=f"ThreatGrid request for {action_name} failed. Unauthorized access to this service.",
                assistance="Verify the permissions for your account and try again.",
            )
        if resp.status_code == 404:
            raise PluginException(
                cause=f"ThreatGrid request for {action_name} failed. The requested item was not found.",
                assistance="Check the syntax of your query and try again.",
            )
        if 400 <= resp.status_code < 500:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=resp.text)
        if resp.status_code >= 500:
            raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=resp.text)
        try:
            return resp.json()
        except JSONDecodeError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=resp.text)

    def submit_sample(self, data: object, files: object):
        """
        Submit Sample to Threat Grid for analysis
        :param data:
        :param files:
        :return:
        """
        return self._call_api(
            "POST", "/api/v2/samples", data=data, files=files, action_name="Submit Sample", authentication="data"
        )

    def search_domain(self, domain: str):
        """
        Makes a query to Threat Grid looking for a specific Domain
        :param domain: Domain
        :return: request
        """

        data = {"term": "domain", "q": domain, "advance": "true"}
        self.logger.info(f"Looking for sample with domain filename: {domain}")
        return self._call_api(
            "GET", "/api/v2/search/submissions", data=data, action_name="Search by Domain", authentication="data"
        )

    def search_id(self, query_id: str):
        """
        Makes a query to Threat Grid, looking for a specific ID
        :param query_id: ID
        :return: request
        """
        data = {"term": "sample.filename", "q": query_id, "advance": "true"}
        return self._call_api(
            "GET", "/api/v2/search/submissions", data=data, action_name="Search by ID", authentication="data"
        )

    def search_sha256(self, sha256: str):
        data = {"term": "checksum", "q": sha256, "advance": "true"}
        return self._call_api(
            "GET", "/api/v2/search/submissions", data=data, action_name="Search by SHA256", authentication="data"
        )

    def get_artifact_analysis(self, sample_id: str):
        return self._call_api(
            method="GET",
            endpoint=f"/api/v2/samples/{sample_id}/analysis/artifacts",
            action_name="Get Artifact Analysis",
            authentication="data",
        )

    def get_ioc_analysis(self, sample_id: str):
        return self._call_api(
            method="GET",
            endpoint=f"/api/v2/samples/{sample_id}/analysis/iocs",
            action_name="Get IOC Analysis",
            authentication="data",
        )

    def get_network_streams_analysis(self, sample_id: str):
        return self._call_api(
            method="GET",
            endpoint=f"/api/v2/samples/{sample_id}/analysis/network_streams",
            action_name="Get Network Streams Analysis",
            authentication="data",
        )

    def get_processes_analysis(self, sample_id: str):
        return self._call_api(
            method="GET",
            endpoint=f"/api/v2/samples/{sample_id}/analysis/processes",
            action_name="Get Processes Analysis",
            authentication="data",
        )

    def get_annotations_analysis(self, sample_id: str):
        return self._call_api(
            method="GET",
            endpoint=f"/api/v2/samples/{sample_id}/analysis/annotations",
            action_name="Get Annotation Analysis",
            authentication="data",
        )

    def get_metadata_analysis(self, sample_id: str):
        return self._call_api(
            method="GET",
            endpoint=f"/api/v2/samples/{sample_id}/analysis/metadata",
            action_name="Get Metadata Analysis",
            authentication="data",
        )
