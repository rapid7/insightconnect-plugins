import json
from logging import Logger
from typing import Any, Dict, List
import itertools


import requests
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean
from subprocess import Popen, SubprocessError
import validators
from tempfile import TemporaryFile

from icon_sqlmap.util.constants import (
    POLL_INTERVAL_SECONDS,
    REQUEST_TIMEOUT_SECONDS,
    SCAN_STATUS_TERMINATED,
    MAX_PORT_RANGE,
    DEFAULT_ENCODING,
    MAX_WAIT_FOR_COMPLETION_ITERATIONS,
)
from icon_sqlmap.util.utils import delay
import time


class SqlmapApi:
    def __init__(self, api_host: str, api_port: str, logger: Logger) -> None:
        # Parse arguments
        self.api_host = api_host
        self.api_port = api_port
        self.logger = logger

        # Create class variables
        self.base_url = f"http://{api_host}:{api_port}"
        self._logs = TemporaryFile(mode="w+", encoding=DEFAULT_ENCODING, errors="ignore")

        # Validate and initialize SQL Map server
        self._validate_host_port()
        self._initialize_server()

    def run_scan(self, target_url: str, headers: dict[str, str], parameters: dict[str, Any]) -> list[dict]:
        # Create task
        task_id = self._create_task()

        # Set options for task
        self._set_options(task_id, parameters, headers)

        # Start the SQL Map scan
        self._start_scan(task_id, target_url, headers)

        # Wait for scan completion
        self._wait_for_completion(task_id)

        # Get scan results
        scan_data = self._get_results(task_id)

        # Delete previously created task
        self._delete_task(task_id)

        # Return results
        return scan_data

    @delay(seconds=POLL_INTERVAL_SECONDS)
    def _create_task(self) -> str:
        # Create task and get its ID
        task_id = self._call_api("GET", f"{self.base_url}/task/new").get("taskid")

        # If taskid is None, raise an exception
        if not task_id:
            raise PluginException(
                cause="Failed to create a new task.", assistance="Please check the SQLMap API connectivity."
            )
        self.logger.info(f"Created task: {task_id}")
        return task_id

    def _set_options(self, task_id: str, parameters: dict[str, Any], headers: dict[str, str]) -> None:
        self.logger.info("Attempting to configure scan options...")
        self._call_api("POST", f"{self.base_url}/option/{task_id}/set", headers=headers, payload=clean(parameters))
        self.logger.info("Scan options configured")

    def _start_scan(self, task_id: str, target_url: str, headers: dict[str, str]) -> None:
        self.logger.info(f"Starting scan for URL: {target_url}...")
        self._call_api("POST", f"{self.base_url}/scan/{task_id}/start", headers=headers, payload={"url": target_url})
        self.logger.info(f"Scan started for URL: {target_url}")

    def _wait_for_completion(self, task_id: str) -> None:
        # This is due to limit the time of waiting to ~5 hours
        for _ in itertools.count(MAX_WAIT_FOR_COMPLETION_ITERATIONS):
            time.sleep(POLL_INTERVAL_SECONDS)
            self.logger.info(f"Checking for scan status (task ID: {task_id})...")
            scan_status = self._call_api("GET", f"{self.base_url}/scan/{task_id}/status").get("status")
            self.logger.info(f"Scan status: {scan_status}.")

            # If scan has been terminated, then it's completed
            if scan_status == SCAN_STATUS_TERMINATED:
                self.logger.info("Scan completed")
                return

            # If still checking for status, log sleeping
            self.logger.info(f"Recheck in {POLL_INTERVAL_SECONDS} seconds...")

        # Raise an exception as the scan result has timed out
        raise PluginException(
            cause="Scan timed out.",
            assistance="The scan took too long to complete. Please check the target URL and SQLMap API connectivity.",
        )

    def _get_results(self, task_id: str) -> List[Dict]:
        return self._call_api("GET", f"{self.base_url}/scan/{task_id}/log").get("log", [])

    def _delete_task(self, task_id: str) -> None:
        self.logger.info(f"Deleting task {task_id}...")
        self._call_api("GET", f"{self.base_url}/task/{task_id}/delete")
        self.logger.info(f"Task {task_id} deleted")

    def _call_api(self, method: str, url: str, headers: dict[str, str] = None, payload: dict[str, Any] = None) -> Dict:
        try:
            with requests.request(
                method,
                url,
                headers=self._prepare_headers(headers),
                json=payload,
                timeout=REQUEST_TIMEOUT_SECONDS,
            ) as response:
                return response.json()
        except requests.exceptions.ConnectionError as error:
            raise PluginException(
                cause="Unable to connect to SQLMap REST API.",
                assistance="Please verify the SQLMap REST API server is running and accessible.",
                data=error,
            )
        except json.decoder.JSONDecodeError as error:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=error)

    @staticmethod
    def _prepare_headers(headers: Dict[str, str]) -> Dict[str, str]:
        if not headers:
            return {"Content-Type": "application/json"}
        return {str(key): str(value) for key, value in headers.items()}

    def _initialize_server(self) -> None:
        # Create command to run SQL map server
        command = "python sqlmap-master/sqlmapapi.py -s "
        if self.api_host and self.api_port:
            command += f"--host={self.api_host} --port={self.api_port}"

        # Run SQL map server as a separate process
        try:
            Popen([command], stdout=self._logs, stderr=self._logs, shell=True)
        except SubprocessError as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

    def get_logs(self, cleanup: bool = False) -> None:
        # Iterate over the captured logs and log it to the console
        for log_line in self._logs.readlines():
            self.logger.info(f"* {log_line}")

        # If cleanup is set to True, just clear the StringIO buffer
        if cleanup:
            self._clean_logs()

    def _clean_logs(self) -> None:
        self._logs.seek(0)
        self._logs.truncate(0)

    def _validate_host_port(self) -> None:
        # Validate host for SQL Map server
        if not validators.ipv4(self.api_host, cidr=False):
            raise PluginException(
                cause=f"Invalid API host: {self.api_host}",
                assistance="Please provide a valid IPv4 address for the API host.",
            )

        # Validate port for SQL Map server
        try:
            self.api_port = int(self.api_port)
            if self.api_port <= 0 or self.api_port > MAX_PORT_RANGE:
                raise PluginException(
                    cause=f"API port out of range: {self.api_port}",
                    assistance=f"Please provide a valid port number between 1 and {MAX_PORT_RANGE}.",
                )
        except ValueError:
            raise PluginException(
                cause=f"Invalid API port: {self.api_port}",
                assistance="Please provide a valid integer for the API port.",
            )
