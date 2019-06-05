import komand
from requests import Session, Request
from json import JSONDecodeError
import mimetypes
import magic


class VMRay:

    SUPPORTED_FILETYPES = [".exe", ".scr", ".lnk2", ".dll", ".sys", ".ocx",
                           ".pdf", ".doc", ".docx", ".docm", ".dot", ".dotx",
                           ".dotm", ".xls", ".xlsx", ".xlsm", ".xlt", ".xltx",
                           ".xltm", ".xlb", ".xlsb", ".iqy", ".slk", ".ppt",
                           ".pptx", ".pptm", ".pot", ".potx", ".potm", ".mpp",
                           ".accdb", ".adn", ".accdr", ".accdt", ".accda",
                           ".mdw", ".accde", ".ade", ".mdb", ".mda", ".vsd",
                           ".vsdx", ".vss", ".vst", ".vsw", ".vdx", ".vtx",
                           ".vsdx", ".vsdm", ".vssx", ".vssm", ".vstx",
                           ".vstm", ".pub", ".puz", ".rtf", ".url", ".html",
                           ".htm", ".hta", ".swf", ".msi", ".bat", ".vbs",
                           ".vbe", ".js", ".jse", ".wsf", ".jar", ".class",
                           ".ps1"]

    def __init__(self, url, api_key, logger):
        self.url = url
        self.api_key = api_key
        self.logger = logger
        self.s = Session()

    def test_call(self):
        return self._call_api("GET", "/rest/system_info")

    def _call_api(self, method, endpoint_url, files=None, params=None, data=None, json=None, action_name=None):
        url = self.url + endpoint_url
        headers = {
            "Authorization": f"api_key {self.api_key}"
        }
        req = Request(
            url=url,
            method=method,
            params=params,
            data=data,
            json=json,
            files=files,
            headers=headers
        )

        try:
            req = req.prepare()
            resp = self.s.send(req)
            if resp.status_code == 405:
                raise Exception(f"An error was received when running {action_name}."
                                f"Request status code of {resp.status_code} was returned."
                                "Please make sure connections have been configured correctly")
            elif resp.status_code != 200:
                raise Exception(f"An error was received when running {action_name}."
                                f" Request status code of {resp.status_code} was returned."
                                " Please make sure connections have been configured correctly "
                                f"as well as the correct input for the action. Response was: {resp.text}")

        except Exception as e:
            self.logger.error(f"An error has occurred: {e}")
            raise

        try:
            results = resp.json()
            return results
        except JSONDecodeError:
            raise Exception(
                f"Error: Received an unexpected response from {action_name}"
                f"(non-JSON or no response was received). Response was: {resp.text}")

    def get_analysis(self, analysis_id, id_type, optional_params):
        if id_type not in ["all", "analysis_id"]:
            endpoint_url = f"/rest/analysis/{id_type}/{analysis_id}"
        elif id_type is "analysis_id":
            endpoint_url = f"/rest/analysis/{analysis_id}"
        else:
            endpoint_url = "/rest/analysis"
        return self._call_api("GET", endpoint_url=endpoint_url, params=optional_params, action_name="Get Analysis")

    def get_samples(self, sample_type, sample, optional_params):
        if sample_type not in ["all", "sample_id"]:
            endpoint_url = f"/rest/sample/{sample_type}/{sample}"
        elif sample_type is "sample_id":
            endpoint_url = f"/rest/sample/{sample}"
        else:
            endpoint_url = "/rest/sample"

        return self._call_api("GET", endpoint_url=endpoint_url, params=optional_params, action_name="Get Samples")

    def submit_file(self, name, file_bytes, optional_params):
        files = {
            "sample_file": (f"{name}", file_bytes)
        }
        endpoint_url = "/rest/sample/submit"

        return self._call_api("POST", endpoint_url=endpoint_url, files=files, params=optional_params, action_name= "Submit File")

    def submit_url(self, url, optional_params):
        optional_params.update({"sample_url": url})
        endpoint_url = "/rest/sample/submit"

        return self._call_api("POST", endpoint_url=endpoint_url, params=optional_params, action_name="Submit URL")


    def check_filetype(self, content, filename=None):
        '''
        :param content: contents of file
        :param filename: name of file being passed in
        :return: mime type that matches or a list of all mime extensions that
        '''
        api_magic = magic.Magic(mime=True)
        content_mime_type = api_magic.from_buffer(content)
        all_extensions = mimetypes.guess_all_extensions(content_mime_type)
        for mime_type in all_extensions:
            if mime_type in self.SUPPORTED_FILETYPES:
                return all_extensions, True

        return all_extensions, False


        #for filetype in self.SUPPORTED_FILETYPES:
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
