import functools
import requests
from insightconnect_plugin_runtime.exceptions import (
    APIException,
    PluginException,
    HTTPStatusCodes,
    ResponseExceptionData,
)
from insightconnect_plugin_runtime.helper import extract_json, make_request, rate_limiting, response_handler
from logging import Logger
from requests import Response, Request
from io import BytesIO
from icon_mimecast_v2.util.constants import Endpoints
from typing import Dict, List, Tuple, Iterator
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
        read_page_filenames: List[str] = [],
        saved_file_position: int = 0,
    ) -> Tuple[List[str], str, bool]:
        batch_download_urls, result_next_page, caught_up, new_filenames = self.get_siem_batches(
            log_type, query_date, next_page, page_size
        )
        merged_page_filenames = list(set(read_page_filenames + new_filenames))
        pool_data = self.resume_from_batch(batch_download_urls, starting_url, saved_file_position)
        pool_data = self.remove_read_download_urls(batch_download_urls, read_page_filenames)
        self.logger.info(f"API: Getting SIEM logs from batches for log type {log_type}...")
        self.logger.info(f"API: Applying page size limit of {page_size}")
        log_count = 0
        manager = Manager()
        saved_file = None
        saved_position = 0
        total_count = manager.Value("i", log_count)
        logs = manager.list()
        lock = manager.Lock()
        with Pool(max_threads) as pool:
            result = pool.imap(
                functools.partial(
                    self.get_siem_logs_from_batch, saved_url=starting_url, saved_position=starting_position
                ),
                pool_data,
            )
            for content, url in result:
                with lock:
                    for index, new_line in enumerate(content):
                        try:
                            decoded_line = new_line.decode("utf-8").strip()
                            json_log = json.loads(decoded_line)
                            logs.append(json_log)
                        except (json.JSONDecodeError, UnicodeDecodeError) as error:
                            self.logger.info(f"API: JSON or decode error in file {url}. Skipping file...")
                            self.logger.info(f"API: Error is {error}")
                            break
                        total_count.value = total_count.value + 1
                        if total_count.value >= log_size_limit:
                            batch_logs_count = 0
                            if starting_url and starting_url in url:
                                if starting_position:
                                    batch_logs_count = starting_position
                            saved_position = 1 + batch_logs_count + index
                            saved_file = url
                            caught_up = False
                            result_next_page = next_page
                            self.logger.info(f"API: Log limit reached for log type {log_type} at {log_size_limit}")
                            self.logger.info(f"API: Saving file for next run: {saved_file} at line {saved_position}")
                            return logs, result_next_page, caught_up, saved_file, saved_position, saved_page_filenames
        self.logger.info(f"API: Discovered {len(logs)} logs for log type {log_type}")
        return logs, result_next_page, caught_up, saved_file, saved_position, []

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
        filenames = []
        for url in urls:
            filenames.append(self.retrieve_filename(url))
        return urls, batch_response.get("@nextPage"), caught_up, filenames

    def retrieve_filename(self, url: str) -> str:
        stripped_url = self.strip_query_params(url)
        return stripped_url.rsplit('/', 1)[-1].replace('.json.gz', '')


    def resume_from_batch(self, list_of_batches: List[str], saved_url: str, saved_file_position: int = 0) -> Tuple[str, int]:
        """
        Attempt to find a previously fully unread file if available, and trim list of URLs to that starting point.
        If file is not found, default to using file positions and attempt to continue
        :param list_of_batches:
        :param saved_url:
        :return list_of_batches: Trimmed list of batches
        """
        batch_length = len(list_of_batches)
        sub_list = list_of_batches[
            next(
                (index for index, url in enumerate(list_of_batches) if saved_url and saved_url in url),
                batch_length,
            ) :
        ]
        if sub_list:
            self.logger.info(f"API: Resuming log collection of {saved_url}")
            return sub_list
        if saved_url:
            self.logger.info(f"API: Saved URL {saved_url} not found in list of batches")
            next_position = saved_file_position + 1
            if next_position > batch_length:
                self.logger.info(f"API: No more files left to process in list: {next_position}/{batch_length}")
                return []
            self.logger.info(f"API: Processing from saved file position: {next_position}/{batch_length}")
            list_of_batches = list_of_batches[next_position:]
        return list_of_batches

    def remove_read_download_urls(self, list_of_batches: List[str] = [], read_page_filenames: List[str] = []):
        read_filename_set = set(read_page_filenames)
        filtered_batch_list = [url for url in list_of_batches if not any(filename in url for filename in read_filename_set)]
        return filtered_batch_list

    def get_siem_logs_from_batch(self, url: str, saved_url: str, saved_position: int) -> Tuple[Iterator[bytes], str]:
        try:
            line_start = 0
            if saved_url and saved_url in url:
                line_start = saved_position
            response = requests.request(method="GET", url=url)
            url = self.strip_query_params(url)
            response_handler(response=response, data_location=ResponseExceptionData.RESPONSE)
            content = self.get_gzip_content(response.content, line_start, url)
            return content, url
        except PluginException as error:
            self.logger.info(f"API: Error requesting file {url}. Skipping...")
            self.logger.info(f"API: Error is {error}")
            return iter([]), url

    def get_gzip_content(self, content: bytes, line_start: int, url: str) -> Iterator[bytes]:
        if not content:
            return iter([])
        lines_count = 0
        try:
            with BytesIO(content) as byte_io:
                with gzip.GzipFile(fileobj=byte_io, mode="rb") as file_:
                    for line in file_:
                        lines_count += 1
                        if lines_count > line_start:
                            yield line
        except gzip.BadGzipFile:
            self.logger.error(f"API: Bad GZIP file found: {url}. Skipping...")
        except Exception as error:
            self.logger.error(f"API: Error in processing log file for url {self.strip_query_params(url)}")
            self.logger.error(f"API: Error was {error}")
            self.logger.error("Skipping...")
        return iter([])

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
