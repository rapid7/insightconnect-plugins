from requests import Session, Request, HTTPError
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
        self,
        method,
        endpoint,
        params=None,
        data=None,
        json=None,
        action_name=None,
        custom_error=None,
        authentication=None,
        files=None,
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
            url=url,
            method=method,
            params=params,
            data=data,
            json=json,
            headers=self.session.headers,
            files=files,
        )

        try:
            # Prep request
            req = req.prepare()
            resp = self.session.send(req)
            # Check for custom errors
            if custom_error and resp.status_code not in range(200, 299):
                raise PluginException(
                    cause=f"An error was received when running {action_name}.",
                    assistance=f"Request status code of {resp.status_code} was returned.\n{custom_error.get(resp.status_code, 000)}",
                    data=resp.text
                )

            try:
                resp.raise_for_status()
            except HTTPError as e:
                raise PluginException(
                    cause=f"ThreatGrid request for {action_name} failed.",
                    assistance=f"ThreatGrid request failed, check your API key.\n "
                    f"Exception returned was: {e}\nResponse was {resp.text} ",
                )

        except Exception as e:
            self.logger.error(
                f"An error had occurred : {e}"
                "If the issue persists please contact support"
            )
            raise

        try:
            results = resp.json()
            return results
        except JSONDecodeError:
            raise PluginException(cause=f"Error: Received an unexpected response from {action_name}.",
                                  assistance=f"(non-JSON or no response was received). Response was: {resp.text}")

    def submit_sample(self, data, files):
        """
         Submit Sample to Threat Grid for analysis
         :param data:
         :return:
         """
        return self._call_api(
            "POST",
            "/api/v2/samples",
            data=data,
            files=files,
            action_name="Submit Sample",
            authentication="data",
        )

    def search_domain(self, q):
        """
         Makes a query to Threat Grid looking for a specific Domain
         :param q: Domain
         :return: request
         """

        data = {"term": "domain", "q": q, "advance": "true"}
        self.logger.info(f"Looking for sample with domain filename: {q}")
        return self._call_api(
            "GET",
            "/api/v2/search/submissions",
            data=data,
            action_name="Search by Domain",
            authentication="data",
        )

    def search_id(self, q):
        """
         Makes a query to Threat Grid, looking for a specific ID
         :param q: ID
         :return: request
         """
        data = {"term": "sample.filename", "q": q, "advance": "true"}
        return self._call_api(
            "GET",
            "/api/v2/search/submissions",
            data=data,
            action_name="Search by ID",
            authentication="data",
        )

    def search_sha256(self, q):
        data = {"q": q, "advance": "true"}
        return self._call_api(
            "GET",
            "/api/v2/search/submissions",
            data=data,
            action_name="Search by SHA256",
            authentication="data",
        )

    def get_artifact_analysis(self, sample_id):
        return self._call_api(
            method="GET",
            endpoint=f"/api/v2/samples/{sample_id}/analysis/artifacts",
            action_name="Get Artifact Analysis",
            authentication="data",
        )

    def get_ioc_analysis(self, sample_id):
        return self._call_api(
            method="GET",
            endpoint=f"/api/v2/samples/{sample_id}/analysis/iocs",
            action_name="Get IOC Analysis",
            authentication="data",
        )

    def get_network_streams_analysis(self, sample_id):
        return self._call_api(
            method="GET",
            endpoint=f"/api/v2/samples/{sample_id}/analysis/network_streams",
            action_name="Get Network Streams Analysis",
            authentication="data",
        )

    def get_processes_analysis(self, sample_id):
        return self._call_api(
            method="GET",
            endpoint=f"/api/v2/samples/{sample_id}/analysis/processes",
            action_name="Get Processes Analysis",
            authentication="data",
        )

    def get_annotations_analysis(self, sample_id):
        return self._call_api(
            method="GET",
            endpoint=f"/api/v2/samples/{sample_id}/analysis/annotations",
            action_name="Get Annotation Analysis",
            authentication="data",
        )

    def get_metadata_analysis(self, sample_id):
        return self._call_api(
            method="GET",
            endpoint=f"/api/v2/samples/{sample_id}/analysis/metadata",
            action_name="Get Metadata Analysis",
            authentication="data",
        )
