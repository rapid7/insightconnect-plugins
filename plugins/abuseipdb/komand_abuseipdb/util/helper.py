from insightconnect_plugin_runtime.exceptions import PluginException


def get_json(response):
    json_ = response.json()
    if "errors" in json_:
        details = ""
        if len(json_["errors"]) > 0 and "detail" in json_["errors"][0]:
            details = json_["errors"][0]["detail"]

        raise PluginException(cause="Received an error response from AbuseIPDB.", assistance=details)

    return json_
