import requests
from insightconnect_plugin_runtime.exceptions import (
    APIException,
    PluginException,
    HTTPStatusCodes,
    ResponseExceptionData,
)
from insightconnect_plugin_runtime.helper import extract_json, make_request, rate_limiting
from logging import Logger
from requests import Response, Request
from io import BytesIO
from icon_mimecast_v2.util.constants import Endpoints
from typing import Dict, List, Tuple
from multiprocessing.dummy import Manager, Pool
import gzip
import json
from urllib.parse import urlparse, urlunparse

GET = "GET"
POST = "POST"


class API:
    def __init__(self, client_id: str, client_secret: str, logger: Logger) -> None:
        self.client_id = client_id
        self.client_secret = client_secret
        self.logger = logger
        self.access_token = None

    def authenticate(self) -> None:
        self.logger.info("API: Authenticating...")
        data = {"client_id": self.client_id, "client_secret": self.client_secret, "grant_type": "client_credentials"}
        response = self.make_api_request(
            url=Endpoints.AUTH,
            method=POST,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data=data,
            auth=False,
        )
        self.access_token = response.get("access_token")
        self.logger.info("API: Authenticated")

    def get_siem_logs(
        self,
        log_type: str,
        query_date: str,
        next_page: str,
        page_size: int = 100,
        max_threads: int = 10,
        starting_url: str = None,
        starting_position: int = 0,
        log_size_limit: int = 250,
    ) -> Tuple[List[str], str, bool]:
        batch_download_urls, result_next_page, caught_up = self.get_siem_batches(
            log_type, query_date, next_page, page_size
        )
        pool_data = self.resume_from_batch(batch_download_urls, starting_url, starting_position)
        self.logger.info(f"API: Getting SIEM logs from batches for log type {log_type}...")
        self.logger.info(f"API: Applying page size limit of {page_size}")
        log_count = 0
        manager = Manager()
        saved_file = None
        saved_position = None
        total_count = manager.Value("i", log_count)
        logs = manager.list()
        lock = manager.Lock()
        with Pool(max_threads) as pool:
            result = pool.imap(self.get_siem_logs_from_batch, pool_data)
            for batch_logs, url in result:
                if isinstance(batch_logs, (List, Dict)):
                    with lock:
                        total_count.value = total_count.value + len(batch_logs)
                        if total_count.value >= log_size_limit:
                            leftover_logs_count = total_count.value - log_size_limit
                            subsection_of_logs = batch_logs[0 : (len(batch_logs) - leftover_logs_count)]
                            logs.extend(subsection_of_logs)
                            saved_file = self.strip_query_params(url)
                            saved_position = len(subsection_of_logs)
                            caught_up = False
                            result_next_page = next_page
                            self.logger.info(f"API: Log limit reached for log type {log_type} at {log_size_limit}")
                            self.logger.info(f"API: Saving file for next run: {saved_file} at line {saved_position}")
                            self.logger.info(f"API: {leftover_logs_count} left to process in file")
                            break
                        logs.extend(batch_logs)
        self.logger.info(f"API: Discovered {len(logs)} logs for log type {log_type}")
        return logs, result_next_page, caught_up, saved_file, saved_position

    def get_siem_batches(
        self, log_type: str, query_date: str, next_page: str, page_size: int = 100
    ) -> Tuple[List[str], str, bool]:
        self.logger.info(
            f"API: Getting SIEM batches for log type {log_type} for {query_date} with page token {next_page}..."
        )
        params = {
            "type": log_type,
            "dateRangeStartsAt": query_date,
            "dateRangeEndsAt": query_date,
            "pageSize": page_size,
        }
        if next_page:
            params.update({"nextPage": next_page})
        batch_response = self.make_api_request(url=Endpoints.GET_SIEM_LOGS_BATCH, method=GET, params=params)
        batch_list = batch_response.get("value", [])
        caught_up = batch_response.get("isCaughtUp")
        self.logger.info(
            f"API: Discovered {len(batch_list)} batches for log type {log_type}. Response reporting {caught_up} that logs have caught up to query window"
        )
        urls = [batch.get("url") for batch in batch_list]
        return urls, batch_response.get("@nextPage"), caught_up

    def resume_from_batch(
        self, list_of_batches: List[str], saved_url: str, starting_position: int = 1
    ) -> Tuple[str, int]:
        """
        Return a pairing of download URL and starting position in file in URL. Attempt to find a previously fully unread
        file if available, and trim list of URLs to that starting point.
        :param list_of_batches:
        :param saved_url:
        :param starting_position:
        :return pool_data: Tuple of URL and starting position in file
        """
        if saved_url:
            self.logger.info(f"API: Attempting to resume from last file at {saved_url}")
            list_of_batches = list_of_batches[
                next((index for index, url in enumerate(list_of_batches) if saved_url in url), len(list_of_batches)) :
            ]

        pool_data = [(url, starting_position if saved_url and saved_url in url else 1) for url in list_of_batches]
        return pool_data

    def get_siem_logs_from_batch(self, url_and_position: Tuple[str, int]) -> Tuple[List[Dict], str]:
        url, line_start = url_and_position
        response = requests.request(method=GET, url=url, stream=False)
        with gzip.GzipFile(fileobj=BytesIO(response.content), mode="rb") as file_:
            logs = []
            # Iterate over lines in the decompressed file, decode and load the JSON
            for _, line in enumerate(file_, start=line_start):
                decoded_line = line.decode("utf-8").strip()
                logs.append(json.loads(decoded_line))
        return logs, url

    def strip_query_params(self, url: str) -> str:
        parsed_url = urlparse(url)
        stripped_url = urlunparse(parsed_url._replace(query=""))
        return stripped_url

    @rate_limiting(5)
    def make_api_request(
        self,
        url: str,
        method: str,
        headers: Dict = {},
        json: Dict = None,
        data: Dict = None,
        params: Dict = None,
        return_json: bool = True,
        auth=True,
    ) -> Response:
        if auth:
            headers["Authorization"] = f"Bearer {self.access_token}"
        request = Request(url=url, method=method, headers=headers, params=params, data=data, json=json)
        try:
            response = make_request(
                _request=request,
                allowed_status_codes=[HTTPStatusCodes.UNAUTHORIZED],
                exception_data_location=ResponseExceptionData.RESPONSE,
            )
        except PluginException as exception:
            if isinstance(exception.data, Response):
                raise APIException(
                    cause=exception.cause,
                    assistance=exception.assistance,
                    data=exception.data,
                    status_code=exception.data.status_code,
                )
            raise exception
        if response.status_code == HTTPStatusCodes.UNAUTHORIZED:
            json_data = extract_json(response)
            if json_data.get("fail", [{}])[0].get("code") == "token_expired":
                self.authenticate()
                self.logger.info("API: Token has expired, attempting re-authentication...")
                return self.make_api_request(url, method, headers, json, data, params, return_json, auth)
        if response.status_code == HTTPStatusCodes.UNAUTHORIZED:
            raise APIException(
                preset=PluginException.Preset.API_KEY, data=response.text, status_code=response.status_code
            )
        if return_json:
            json_data = extract_json(response)
            return json_data
        return response
