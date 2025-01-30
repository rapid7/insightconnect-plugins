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
from multiprocessing.dummy import Pool
import gzip
import json

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
        self, log_type: str, query_date: str, next_page: str, page_size: int = 100, max_threads: int = 10
    ) -> Tuple[List[str], str, bool]:
        batch_download_urls, result_next_page, caught_up = self.get_siem_batches(
            log_type, query_date, next_page, page_size
        )
        logs = []
        self.logger.info(f"API: Getting SIEM logs from batches for log type {log_type}...")
        self.logger.info(f"API: Applying page size limit of {page_size}")
        with Pool(max_threads) as pool:
            batch_logs = pool.imap(self.get_siem_logs_from_batch, batch_download_urls)
            for result in batch_logs:
                if isinstance(result, (List, Dict)):
                    logs.extend(result)
        self.logger.info(f"API: Discovered {len(logs)} logs for log type {log_type}")
        return logs, result_next_page, caught_up

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

    def get_siem_logs_from_batch(self, url: str):
        response = requests.request(method=GET, url=url, stream=False)
        with gzip.GzipFile(fileobj=BytesIO(response.content), mode="rb") as file_:
            logs = []
            # Iterate over lines in the decompressed file, decode and load the JSON
            for line in file_:
                decoded_line = line.decode("utf-8").strip()
                logs.append(json.loads(decoded_line))
        return logs

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
        if (
            response.status_code == HTTPStatusCodes.UNAUTHORIZED
            and extract_json(response).get("fail", [{}])[0].get("code") == "token_expired"
        ):
            self.authenticate()
            self.logger.info("API: Token has expired, attempting re-authentication...")
            return self.make_api_request(url, method, headers, json, data, params, return_json, auth)
        elif response.status_code == HTTPStatusCodes.UNAUTHORIZED:
            raise APIException(
                preset=PluginException.Preset.API_KEY, data=response.text, status_code=response.status_code
            )
        if return_json:
            json_data = extract_json(response)
            return json_data
        return response
