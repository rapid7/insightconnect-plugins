from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException
import json
import base64
from .mcafee_request import McAfeeRequest


class McAfeeATDAPI:
    def __init__(self, mc_afee_request: McAfeeRequest, username: str, password: str, logger: object):
        self.mc_afee_request = mc_afee_request
        self.username = username
        self.password = password
        self.logger = logger
        self.STATUSES = {
            'w': 'Whitelisted',
            'b': 'Blacklisted',
            '0': 'Not found',
            'j': 'Previously submitted',
            'Invalid input data': 'Invalid hash value'
        }

    def list_analyzer_profiles(self):
        return self._make_login_request(
            "GET",
            "vmprofiles.php"
        )

    def submit_file(self, file: dict, url_for_file: str) -> dict:
        type_number = "0"
        if url_for_file:
            type_number = "2"
        return self._make_login_request(
                "POST",
                "fileupload.php",
                json_data={'data': json.dumps({'data': {"url": url_for_file, "submitType": type_number}})},
                files={'amas_filename': base64.decodebytes(file.get('content').encode('utf-8'))}
            )

    def submit_url(self, url: str, submit_type: str) -> dict:
        number_type = "1"
        if submit_type == "File from URL":
            number_type = "3"
        return self._make_login_request(
            "POST",
            "fileupload.php",
            {'data': json.dumps({'data': {"url": url, "submitType": number_type}})}
        )

    def check_analysis_status(self, task_id: int, type: str):
        param = "iTaskId"
        if "job" == type:
            param = "jobId"

        return self._make_login_request(
            "GET",
            "samplestatus.php",
            params={param: task_id}
        )

    def submit_hash(self, md5_hash: str):
        submit_hash = self._make_login_request(
            "POST",
            "atdHashLookup.php",
            {'data': json.dumps({"md5": md5_hash})}
        )

        if not submit_hash.get("success", False):
            raise PluginException(
                cause="Unknown error occurred. ",
                assistance="Please contact support or try again later."
            )

        results = {}
        statuses = submit_hash.get("results", {})
        for submitted_hash, status in statuses.items():
            results[submitted_hash.lower()] = self.STATUSES.get(status, status)

        return results

    def _get_login_headers(self):
        session_response = self.mc_afee_request.make_json_request("POST", "session.php", headers={
            "Accept": "application/vnd.ve.v1.0+json",
            "Content-Type": "application/json",
            "VE-SDK-API": base64.encodebytes(
                f"{self.username}:{self.password}".encode()
            ).decode("utf-8").rstrip()
        })

        if session_response.get("success", False):
            session = session_response.get("results", {}).get("session")
            user_id = session_response.get("results", {}).get("userId")
            return {
                "Accept": "application/vnd.ve.v1.0+json",
                "VE-SDK-API": base64.encodebytes(
                    f"{session}:{user_id}".encode()
                ).decode("utf-8").rstrip()
            }

        raise ConnectionTestException(ConnectionTestException.Preset.USERNAME_PASSWORD)

    def _make_login_request(self, method: str, path: str, json_data: dict = None, params: dict = None, files: dict = None):
        headers = None
        try:
            headers = self._get_login_headers()
            response = self.mc_afee_request.make_json_request(
                method,
                path,
                params=params,
                data=json_data,
                files=files,
                headers=headers
            )
            return response
        except ConnectionTestException as e:
            raise PluginException(cause=e.cause, assistance=e.assistance, data=e.data)
        finally:
            self.mc_afee_request.make_json_request("DELETE", "session.php", headers=headers)
