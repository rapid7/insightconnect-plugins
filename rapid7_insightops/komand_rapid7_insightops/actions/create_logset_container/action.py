import komand
import requests
from .schema import CreateLogsetContainerInput, CreateLogsetContainerOutput


class CreateLogsetContainer(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_logset_container',
                description='Creates a container within the specified logset for the InsightOps service',
                input=CreateLogsetContainerInput(),
                output=CreateLogsetContainerOutput())

    def run(self, params={}):
        service_url = "/management/logs"
        url = self.connection.insighturl + service_url
        headers = {
            'x-api-key': self.connection.api_key,
            "Content-Type": "application/json"
        }
        payload = {
            "log":
                {
                    "name":params["name"],
                    "structures":params["structures"],
                    "user_data":
                     {
                         "le_agent_filename":params["le_agent_filename"],
                         "le_agent_follow":params["le_agent_follow"]
                     },
                    "source_type":params["source_type"],
                    "token_seed":params["token_seed"],
                    "logsets_info":
                        [
                            {"id":params["id"]}
                        ]
                }
        }

        try:
            resp = requests.post(url, headers=headers, json=payload)
            return {"log":resp.json()}
        except Exception:
            self.logger.info(Exception)
            raise

    def test(self):
        url = self.connection.insighturl
        headers = {'x-api-key': self.connection.api_key}
        try:
            resp = requests.get(url, headers=headers)
            return {"status":resp.status_code}
        except Exception:
            self.logger.info(Exception)
            raise
