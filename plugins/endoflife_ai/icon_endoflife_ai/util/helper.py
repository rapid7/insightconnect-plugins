import json
from urllib.parse import quote

import requests
from insightconnect_plugin_runtime.exceptions import PluginException

# Every tier of the endoflife.ai API accepts a batch of at least this many items,
# so chunking at this size works with or without an API key.
BATCH_CHUNK_SIZE = 5

# Fields copied from an API score object into a flat action output, in output order.
SCORE_FIELDS = (
    "product",
    "version",
    "status",
    "eol_date",
    "days_until_eol",
    "days_past_eol",
    "score",
    "band",
    "grade",
    "extended_support_available",
    "eol_date_source",
    "eol_date_confidence",
    "product_url",
)

# Extra fields kept on each row of the Get Product action.
VERSION_EXTRA_FIELDS = (
    "release_date",
    "latest_release",
    "extended_support_date",
    "score_card_url",
)


def path_segment(value, lowercase: bool = False) -> str:
    """URL-encode one path segment such as a product slug or version."""
    text = str(value if value is not None else "").strip()
    if lowercase:
        text = text.lower()
    return quote(text, safe="")


def request_json(connection, method: str, path: str, json_body=None):
    """
    Call the endoflife.ai API and return (status_code, parsed JSON).

    Network failures, non-JSON bodies, rate limits and server errors raise
    PluginException. 4xx answers that carry an "error" field are returned to the
    caller, which decides whether they mean "not found" or a real failure.
    """
    url = f"{connection.base}{path}"
    try:
        response = requests.request(method, url, headers=connection.headers, json=json_body, timeout=30)
    except requests.exceptions.Timeout as error:
        raise PluginException(preset=PluginException.Preset.TIMEOUT, data=str(error))
    except requests.exceptions.RequestException as error:
        raise PluginException(preset=PluginException.Preset.CONNECTION_ERROR, data=str(error))

    if response.status_code == 401 or response.status_code == 403:
        raise PluginException(preset=PluginException.Preset.API_KEY, data=response.text)
    if response.status_code == 429:
        raise PluginException(preset=PluginException.Preset.RATE_LIMIT, data=response.text)
    if response.status_code >= 500:
        raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.text)

    try:
        json_ = response.json()
    except json.decoder.JSONDecodeError:
        raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)

    if response.status_code == 404:
        return 404, json_
    if response.status_code not in range(200, 299):
        raise PluginException(
            cause="Received an unexpected response from endoflife.ai.",
            assistance=f"Status code was {response.status_code}.",
            data=response.text,
        )
    return response.status_code, json_


def error_message(json_) -> str:
    """The API's own explanation from an error body, with slug suggestions when offered."""
    if not isinstance(json_, dict):
        return "Not found"
    message = str(json_.get("error") or "Not found")
    suggestions = json_.get("suggestions") or json_.get("did_you_mean")
    if isinstance(suggestions, list) and suggestions:
        message = f"{message}. Did you mean: {', '.join(str(s) for s in suggestions)}"
    return message


def score_to_output(obj: dict, extra_fields=()) -> dict:
    """Flatten one API score object into the plugin's output fields."""
    out = {}
    for field in SCORE_FIELDS:
        out[field] = obj.get(field)
    for field in extra_fields:
        out[field] = obj.get(field)
    factors = obj.get("factors") or {}
    out["cisa_kev_exposure"] = factors.get("cisa_kev_exposure")
    return out
