import time
from functools import wraps
from logging import Logger
from typing import Any, Callable, Dict

from dateutil.parser import parse
from insightconnect_plugin_runtime.exceptions import PluginException

from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests

from komand_rapid7_insightvm.util.cache_file_manager import CacheFileManager


def convert_date_to_iso8601(date: str) -> str:
    try:
        date_object = parse(date)
        return date_object.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    except ValueError:
        raise PluginException(
            cause=f"The provided date format {date} is not supported.",
            assistance="Please provide the date in a different format e.g. 2022-01-01T00:00:00Z and try again.",
        )


def adhoc_sql_report(connection, logger, report_payload: dict):
    """
    Fetches all resources from a paged APIv3 endpoint
    :param connection: Connection object populated with session and console URL
    :param logger: Logger object available to actions/triggers, usually self.logger
    :param report_payload: string of generated SQL report contents
    :return: String of generated SQL report contents
    """
    resource_helper = ResourceRequests(connection.session, logger, connection.ssl_verify)

    # Create Report
    endpoint = endpoints.Report.create(connection.console_url)

    logger.info(f"Creating report configuration with name: {report_payload['name']}")
    response = resource_helper.resource_request(endpoint=endpoint, method="post", payload=report_payload)
    report_id = response.get("id")
    # Generate Report
    if report_id is None:
        raise PluginException(
            cause="Error: Failed to create report, report ID was not returned with create request",
            assistance="Review InsightVM console logs and try again.",
        )

    endpoint = endpoints.Report.generate(connection.console_url, report_id)
    logger.info("Generating report")
    response = resource_helper.resource_request(endpoint=endpoint, method="post")
    report_instance_id = response.get("id")

    # Wait for report completion
    if report_instance_id is None:
        raise PluginException(
            cause="Error: Failed to generate report, report instance ID was not returned with " "generate request.",
            assistance="Review the report configuration and InsightVM console logs; then try again.",
        )

    endpoint = endpoints.Report.status(connection.console_url, report_id, report_instance_id)
    report_status_response = resource_helper.resource_request(endpoint=endpoint)
    while report_status_response["status"] != "complete":
        time.sleep(30)
        report_status_response = resource_helper.resource_request(endpoint=endpoint)
        logger.info(
            f"Report ID {report_id}, instance ID {report_instance_id} status: " f"{report_status_response['status']}"
        )

        if ("status" in report_status_response) and (report_status_response["status"] in ("aborted", "failed")):
            raise PluginException(
                cause=f"Error: Report failed to generated with status " f"{report_status_response['status']}.",
                assistance="Review the report configuration and InsightVM logs prior " "to trying again.",
            )

    # Download report
    endpoint = endpoints.Report.download(connection.console_url, report_id, report_instance_id)
    logger.info("Downloading SQL report contents")
    report_contents = resource_helper.resource_request(endpoint=endpoint, json_response=False)

    # Cleanup report
    endpoint = endpoints.Report.delete(connection.console_url, report_id)
    logger.info("Cleaning up report configuration ")
    resource_helper.resource_request(endpoint=endpoint, method="delete")

    return report_contents


def write_to_cache(logger: Logger, filename: str, data: str) -> None:
    with CacheFileManager(logger, filename) as cache_file:
        cache_file.write(data)


def read_from_cache(logger: Logger, filename: str) -> str:
    with CacheFileManager(logger, filename) as cache_file:
        contents = cache_file.read()

        return contents


def check_not_null(account: Dict[str, Any], var_name: str) -> str:
    """
    Checks that a required value is inputted
    :param account: user input
    :param var_name: name of variable we check
    :return: value or PluginException
    """
    value = account.get(var_name)
    if value in (None, ""):
        raise PluginException(
            cause=f"{var_name} has not been entered.",
            assistance=f"Enter valid {var_name}",
        )
    else:
        return value


def retry_request(maximum_tries: int, delay: int = 5) -> Callable:
    def _decorator(function_: Callable) -> Callable:
        @wraps(function_)
        def wrapper(self, *args, **kwargs):
            error_, counter = None, 0
            while counter < maximum_tries:
                try:
                    return function_(self, *args, **kwargs)
                except PluginException as error:
                    self.logger.info(
                        f"{error} Retrying the API call in {delay} seconds... ({counter + 1}/{maximum_tries})"
                    )
                    counter, error_ = counter + 1, error
                    time.sleep(delay)
            raise error_

        return wrapper

    return _decorator
