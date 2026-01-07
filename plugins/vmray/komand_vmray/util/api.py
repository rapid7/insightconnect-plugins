import insightconnect_plugin_runtime
import requests
from insightconnect_plugin_runtime.exceptions import PluginException
from requests import RequestException
from json import JSONDecodeError
import mimetypes
import magic
from logging import Logger
from typing import Optional, Dict, Any, Tuple, List


class VMRay:

    SUPPORTED_FILETYPES = [
        ".exe",
        ".scr",
        ".lnk2",
        ".dll",
        ".sys",
        ".ocx",
        ".pdf",
        ".doc",
        ".docx",
        ".docm",
        ".dot",
        ".dotx",
        ".dotm",
        ".xls",
        ".xlsx",
        ".xlsm",
        ".xlt",
        ".xltx",
        ".xltm",
        ".xlb",
        ".xlsb",
        ".iqy",
        ".slk",
        ".ppt",
        ".pptx",
        ".pptm",
        ".pot",
        ".potx",
        ".potm",
        ".mpp",
        ".accdb",
        ".adn",
        ".accdr",
        ".accdt",
        ".accda",
        ".mdw",
        ".accde",
        ".ade",
        ".mdb",
        ".mda",
        ".vsd",
        ".vsdx",
        ".vss",
        ".vst",
        ".vsw",
        ".vdx",
        ".vtx",
        ".vsdx",
        ".vsdm",
        ".vssx",
        ".vssm",
        ".vstx",
        ".vstm",
        ".pub",
        ".puz",
        ".rtf",
        ".url",
        ".html",
        ".htm",
        ".hta",
        ".swf",
        ".msi",
        ".bat",
        ".vbs",
        ".vbe",
        ".js",
        ".jse",
        ".wsf",
        ".jar",
        ".class",
        ".ps1",
    ]

    def __init__(self, url: str, api_key: str, logger: Logger) -> None:
        self.url = url
        self.api_key = api_key
        self.logger = logger

    def test_call(self) -> Dict[str, Any]:
        return self._call_api("GET", "system_info")

    def _call_api(
        self,
        method: str,
        endpoint_url: str,
        files: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        action_name: Optional[str] = None,
    ) -> Dict[str, Any]:
        try:
            response = requests.request(
                method,
                f"{self.url}/rest/{endpoint_url}",
                params=params,
                data=data,
                json=json,
                files=files,
                headers={"Authorization": f"api_key {self.api_key}"},
            )
            if response.status_code == 405:
                raise PluginException(
                    cause=f"An error was received when running {action_name}.",
                    assistance=f"Request status code of {response.status_code} was returned."
                    "Please make sure connections have been configured correctly",
                    data=response.text,
                )
            elif response.status_code != 200:
                raise PluginException(
                    cause=f"An error was received when running {action_name}.",
                    assistance=f"Request status code of {response.status_code} was returned."
                    " Please make sure connections have been configured correctly "
                    "as well as the correct input for the action.",
                    data=response.text,
                )
        except RequestException as exception:
            self.logger.error(f"An error has occurred: {exception}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=str(exception))

        try:
            return response.json()
        except JSONDecodeError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)

    def get_analysis(self, analysis_id: str, id_type: str, optional_params: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        if id_type not in ["all", "analysis_id"]:
            endpoint_url = f"analysis/{id_type}/{analysis_id}"
        elif id_type == "analysis_id":
            endpoint_url = f"analysis/{analysis_id}"
        else:
            endpoint_url = "analysis"
        return self._call_api("GET", endpoint_url=endpoint_url, params=optional_params, action_name="Get Analysis")

    def get_samples(self, sample_type: str, sample: str, optional_params: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        if sample_type not in ["all", "sample_id"]:
            endpoint_url = f"sample/{sample_type}/{sample}"
        elif sample_type == "sample_id":
            endpoint_url = f"sample/{sample}"
        else:
            endpoint_url = "sample"

        return self._call_api("GET", endpoint_url=endpoint_url, params=optional_params, action_name="Get Samples")

    def submit_file(self, name: str, file_bytes: bytes, optional_params: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        files = {"sample_file": (f"{name}", file_bytes)}
        endpoint_url = "sample/submit"

        return self._call_api(
            "POST",
            endpoint_url=endpoint_url,
            files=files,
            params=optional_params,
            action_name="Submit File",
        )

    def submit_url(self, url: str, optional_params: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        optional_params.update({"sample_url": url})
        return self._call_api("POST", endpoint_url="sample/submit", params=optional_params, action_name="Submit URL")

    def check_filetype(self, content: bytes) -> Tuple[List[str], bool]:
        """
        :param content: contents of file
        :return: mime type that matches or a list of all mime extensions that
        """

        api_magic = magic.Magic(mime=True)
        content_mime_type = api_magic.from_buffer(content)
        all_extensions = mimetypes.guess_all_extensions(content_mime_type)
        for mime_type in all_extensions:
            if mime_type in self.SUPPORTED_FILETYPES:
                return all_extensions, True
        return all_extensions, False

        # for filetype in self.SUPPORTED_FILETYPES:
        #    if filename.startswith(filename):
        #        return filetype, True

    # TODO: Get submission
    # TODO: Delete Submission
    # TODO: Get sample file
    # TODO: Get sample IOCs
    # TODO: Get sample Threat Indicators
    # TODO: Get prescript(s)
    # TODO: Get prescript file
    # TODO: Get dynamic and static analysis(es)
    # TODO: Get analysis archive
    # TODO: Get reputation lookup(s)
    # TODO: Get whois lookup(s)
    # TODO: Get Metadefender analysis(es)
    # TODO: Get VirusTotal analysis(es)
    # TODO: Get dynamic and static analysis job(s)
    # TODO: Delete dynamic or static analysis job
    # TODO: Get reputation job(s)
    # TODO: Get whois job(s)
    # TODO: Get Metadefender job(s)
    # TODO: Get VirusTotal job(s)
    # TODO: Get billing information
    # TODO: Retrieve information
    # TODO: Get tag(s)
    # TODO: Get tag analyses
    # TODO: Get tag submissions
    # TODO: Add tag to analysis
    # TODO: Delete tag from analysis
    # TODO: Add tag to submission
    # TODO: Delete tag from submission
    # TODO: Get cached continuation items
    # TODO: Get quota information
    # endregion
