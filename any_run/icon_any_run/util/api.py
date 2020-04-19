import requests
from insightconnect_plugin_runtime.exceptions import PluginException
import json


class AnyRunAPI:
    def __init__(self, authentication_header, logger):
        self.url = 'https://api.any.run/v1/analysis/'
        self.authentication_header = authentication_header
        self.logger = logger

    def get_history(self, team, skip, limit):
        try:
            r = requests.api.get(self.url,
                                 params={"team": team, "skip": skip, "limit": limit},
                                 headers=self.authentication_header)
            r.raise_for_status()
            return r.json()
        except requests.exceptions.HTTPError as e:
            self.logger.info(f"Call to Any Run raised exception: {e}")
            raise PluginException(cause="Call to Any Run failed",
                                  assistance=r.text,
                                  data=e)

    def get_report(self, task_id):
        try:
            r = requests.api.get(self.url + task_id,
                                 headers=self.authentication_header)
            r.raise_for_status()
            return r.json()
        except requests.exceptions.HTTPError as e:
            self.logger.info(f"Call to Any Run raised exception: {e}")
            raise PluginException(cause="Call to Any Run failed",
                                  assistance=r.text,
                                  data=e)

    def run_analysis(self, params, files):
        try:
            r = requests.api.post(self.url,
                                  files=files,
                                  json=params,
                                  headers=self.authentication_header)
            r.raise_for_status()
            return r.json()
        except requests.exceptions.HTTPError as e:
            self.logger.info(f"Call to Any Run raised exception: {e}")
            raise PluginException(cause="Call to Any Run failed",
                                  assistance=r.text,
                                  data=e)
