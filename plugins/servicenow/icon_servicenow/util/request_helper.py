import requests
import json
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.exceptions import ConnectionTestException


class RequestHelper(object):
    def __init__(self, session, logger):
        """
        Creates a new instance of RequestHelper
        :param session: Session object available to Komand actions/triggers, usually self.connection.session
        :param logger: Logger object available to Komand actions/triggers, usually self.logger
        :return: RequestHelper object
        """
        self.logger = logger
        self.session = session

    def make_request(self, endpoint, method, payload=None, params=None, content_type="application/json"):
        try:
            request_method = getattr(self.session, method.lower())

            headers = {"Content-Type": content_type, "Accept": "application/json"}

            if not params:
                params = {}
            response = request_method(url=endpoint, headers=headers, params=params, json=payload, verify=False)
        except requests.RequestException as e:
            self.logger.error(e)
            raise

        if response.status_code in range(200, 299):
            content_type = response.headers.get("Content-Type", "")

            if response.status_code == 204:
                resource = None
            else:
                if "application/json" in content_type:
                    try:
                        resource = response.json()
                    except json.decoder.JSONDecodeError:
                        raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)
                else:
                    resource = response.content

            return {"resource": resource, "status": response.status_code, "content-type": content_type}

        try:
            error = response.json()
        except json.decoder.JSONDecodeError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)

        raise PluginException(
            cause="Error in API request to ServiceNow. ",
            assistance=f"Status code: {response.status_code}, Error: {error}",
        )
