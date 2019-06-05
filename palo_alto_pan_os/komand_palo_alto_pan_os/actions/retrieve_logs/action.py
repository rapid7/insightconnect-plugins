import komand
from .schema import RetrieveLogsInput, RetrieveLogsOutput
# Custom imports below
import requests
import xmltodict
import time


class RetrieveLogs(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='retrieve_logs',
                description='Query firewall logs',
                input=RetrieveLogsInput(),
                output=RetrieveLogsOutput())

    def run(self, params={}):
        log_type = params.get("log_type")
        query = params.get("filter")
        direction = params.get("direction")
        count = params.get("count")
        skip = params.get("skip")
        max_tries = params.get("max_tries")
        interval = params.get("interval")

        querystring = {"type": "log", "log-type": log_type, "key": self.connection.request.key,
                       "query": query, "dir": direction, "nlogs": str(count), "skip": str(skip)}
        try:
            response = requests.get(self.connection.request.url, params=querystring,
                                    verify=self.connection.request.verify_cert)
            dict_response = xmltodict.parse(response.text)
            job_id = dict_response["response"]["result"]["job"]
            tries_completed = 0
        except KeyError:
            self.logger.error('The output did not contain a proper response.')
            self.logger.error(dict_response)
            raise
        except BaseException as e:
            self.logger.error("Could not complete specified operation. Error: " + str(e))
            raise

        while tries_completed <= max_tries:
            self.logger.info("Polling for job completion...")
            try:
                querystring = {"type": "log", "action": "get",
                               "key": self.connection.request.key, "job-id": job_id}
                job_poll_response = requests.get(self.connection.request.url, params=querystring,
                                                 verify=self.connection.request.verify_cert)
                dict_job_poll_response = xmltodict.parse(job_poll_response.text)
            except BaseException as e:
                self.logger.error("Could not complete specified operation. Error: " + str(e))
                raise
            if dict_job_poll_response['response']['@status'] == 'error':
                self.logger.error('Palo Alto PAN-OS returned an error in response to the request: ')
                self.logger.error(dict_job_poll_response)
                raise Exception('Palo Alto PAN-OS error')
            if dict_job_poll_response["response"]["result"]["job"]["status"] == 'FIN':
                return {"response": dict_job_poll_response["response"]["result"]["log"]}
            tries_completed += 1
            if tries_completed != max_tries:
                self.logger.info("Job not completed, waiting before re-polling...")
                time.sleep(interval)
                raise Exception("Maximum polling attempts reached before response could be returned."
                                " Queued job had ID " + str(job_id))

    def test(self):
        if self.connection.request.key:
            return {"response": {"message": "Access token obtained"}}
