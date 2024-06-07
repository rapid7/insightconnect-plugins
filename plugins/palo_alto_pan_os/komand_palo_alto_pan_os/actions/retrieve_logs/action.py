import insightconnect_plugin_runtime
from .schema import RetrieveLogsInput, RetrieveLogsOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import requests
import xmltodict
import time
import json

TIMEOUT = 60


class RetrieveLogs(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="retrieve_logs",
            description=Component.DESCRIPTION,
            input=RetrieveLogsInput(),
            output=RetrieveLogsOutput(),
        )

    def run(self, params={}):  # noqa: MC0001
        log_type = params.get(Input.LOG_TYPE)
        query = params.get(Input.FILTER)
        direction = params.get(Input.DIRECTION)
        count = params.get(Input.COUNT)
        skip = params.get(Input.SKIP)
        max_tries = params.get(Input.MAX_TRIES)
        interval = params.get(Input.INTERVAL)

        querystring = {
            "type": "log",
            "log-type": log_type,
            "key": self.connection.request.key,
            "query": query,
            "dir": direction,
            "nlogs": str(count),
            "skip": str(skip),
        }

        response = requests.get(
            self.connection.request.url, params=querystring, verify=self.connection.request.verify_cert, timeout=TIMEOUT
        )
        try:
            dict_response = xmltodict.parse(response.text)
        except TypeError:
            raise PluginException(
                cause="The response from PAN-OS was not the correct data type.",
                assistance="Contact support for help.",
                data=response.text,
            )
        except SyntaxError:
            raise PluginException(
                cause="The response from PAN-OS was malformed.",
                assistance="Contact support for help.",
                data=response.text,
            )
        except BaseException as e:
            raise PluginException(
                cause="An unknown error occurred when parsing the PAN-OS response.",
                assistance="Contact support for help.",
                data=f"Error {e}",
            )

        try:
            job_id = dict_response["response"]["result"]["job"]

        except KeyError:
            raise PluginException(
                cause="The response from PAN-OS did not contain the expected data.",
                assistance="Contact support for help.",
                data=dict_response,
            )
        tries_completed = 0
        while tries_completed <= max_tries:
            self.logger.info("Polling for job completion...")
            try:
                querystring = {
                    "type": "log",
                    "action": "get",
                    "key": self.connection.request.key,
                    "job-id": job_id,
                }
                job_poll_response = requests.get(
                    self.connection.request.url,
                    params=querystring,
                    verify=self.connection.request.verify_cert,
                    timeout=TIMEOUT,
                )
                dict_job_poll_response = xmltodict.parse(job_poll_response.text)
            except BaseException as e:
                raise PluginException(
                    "Could not complete specified operation.",
                    assistance="Contact support for help.",
                    data=str(e),
                )
            if dict_job_poll_response["response"]["@status"] == "error":
                error = dict_job_poll_response["response"]["msg"]
                error = json.dumps(error)
                raise PluginException(
                    cause="PAN-OS returned an error in response to the request.",
                    assistance="Double that check inputs are valid. Contact support if this issue persists.",
                    data=error,
                )
            if dict_job_poll_response["response"]["result"]["job"]["status"] == "FIN":
                return {Output.RESPONSE: dict_job_poll_response["response"]["result"]["log"]}
            tries_completed += 1
            if tries_completed != max_tries:
                self.logger.info("Job not completed, waiting before re-polling...")
                time.sleep(interval)
        raise PluginException(
            cause="Maximum polling attempts reached before response could be returned." " Queued job had ID.",
            assistance="Try again later. If the issue persists, please contact support.",
            data=str(job_id),
        )
