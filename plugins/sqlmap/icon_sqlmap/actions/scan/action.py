import insightconnect_plugin_runtime
from .schema import ScanInput, ScanOutput

# Custom imports below
import requests
import time
import json


class Scan(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="scan",
            description="Performs a SQLMap scan on target",
            input=ScanInput(),
            output=ScanOutput(),
        )

        self.scan_url = ""
        self.api_host = ""
        self.api_port = ""
        self.headers = ""
        self.taskid = ""
        self.data = {}
        self.status = ""
        self.url = {}
        self.cleaned_options = {}
        self.sql_url = ""

    def run(self, params={}):
        try:
            return self.orchestrator(params)
        except Exception as error:
            self.logger.error(error)
            self.connection.f.close()
            with open("sqlmap_logs.txt", encoding="UTF-8") as r:
                for line in r.readlines():
                    self.logger.info("*" + line)
            raise error

    def orchestrator(self, params={}):
        self.api_host = self.connection.api_host
        self.api_port = self.connection.api_port
        self.url = params.get("url").encode("utf-8", "ignore")
        self.new_task()
        self.headers = params.get("headers")
        params["url"] = self.url
        params["taskid"] = self.taskid
        params["id"] = self.taskid
        params["headers"] = self.headers
        self.set_options()
        self.start_scan()

        while True:
            time.sleep(10)
            self.get_status_code()
            if self.status == "not running":
                time.sleep(10)
                self.logger.info("Not Running")
            elif self.status == "running":
                time.sleep(5)
                self.logger.info("Running")
                time.sleep(10)
            elif self.status == "terminated":
                self.logger.info("Terminated")
                break
            else:
                break
        self.get_data()
        if self.data:
            self.delete_task()
            return {"log": self.data}

    def new_task(self):
        time.sleep(5)
        self.taskid = json.loads(requests.get(f"http://{self.api_host}:{self.api_port}/task/new", timeout=10).text)[
            "taskid"
        ]

    def set_options(self, params={}):
        if not self.headers:
            self.headers = {"Content-Type": "application/json"}
        self.headers = {str(key): str(value) for key, value in self.headers.items()}
        params = {str(key): str(value) for key, value in params.items()}
        set_options = requests.post(  # pylint: disable=unused-variable  # noqa: F841
            f"http://{self.api_host}:{self.api_port}/option/{self.taskid}/set",
            data=json.dumps(params),
            headers=self.headers,
            timeout=10,
        )

    def start_scan(self):
        payload = {"url": self.url}
        payload = {str(key): str(value) for key, value in payload.items()}
        self.sql_url = f"http://{self.api_host}:{self.api_port}/scan/{self.taskid}/start"
        start_scan = json.loads(  # pylint: disable=unused-variable  # noqa: F841
            requests.post(self.sql_url, data=json.dumps(payload), headers=self.headers, timeout=10).text
        )

    def get_data(self):
        self.data = json.loads(
            requests.get(f"http://{self.api_host}:{self.api_port}/scan/{self.taskid}/log", timeout=10).text
        )["log"]

    def get_status_code(self):
        self.status = json.loads(
            requests.get(f"http://{self.api_host}:{self.api_port}/scan/{self.taskid}/status", timeout=10).text
        )["status"]

    def delete_task(self):
        if json.loads(
            requests.get(f"http://{self.api_host}:{self.api_port}/task/{self.taskid}/delete", timeout=10).text
        )["success"]:
            return True
        return False

    def test(self):
        self.api_host = self.connection.api_host
        self.api_port = self.connection.api_port
        time.sleep(5)
        req_check = json.loads(requests.get(f"http://{self.api_host}:{self.api_port}/task/new", timeout=10).text)
        taskid = req_check["taskid"]
        failed = {"result": "failed"}
        if taskid:
            delete_task = json.loads(  # pylint: disable=unused-variable  # noqa: F841
                requests.get(f"http://{self.api_host}:{self.api_port}/task/{taskid}/delete", timeout=10).text
            )
            return req_check
        else:
            return failed
