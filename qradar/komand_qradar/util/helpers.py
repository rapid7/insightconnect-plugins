import requests

from urllib.parse import quote
import base64


def encode_basic_auth(username, password):
    """Returns the content of an Auth header given a username and password"""
    creds = username + ":" + password
    return b'Basic ' + base64.b64encode(bytes(creds, "utf-8"))


def get_offenses(log, host, basic_auth=None, token=None, fields=None, filter=None, range=None):
    url = host + "/api/siem/offenses?"
    if fields: url += "fields=" + quote(fields) + "&"
    if filter: url += "filter=" + quote(filter)
    if token:
        headers = {"SEC": token, "Accept": "application/json"}
    else:
        headers = {"Authorization": basic_auth, "Accept": "application/json"}
    if range: headers["Range"] = range
    try:
        resp = requests.get(url, headers=headers, verify=False)
        if resp.status_code == 200:
            return resp.json()
        elif resp.status_code == 422:
            log.error("Get Offenses: invalid parameter")
        elif resp.status_code == 500:
            log.error("Get Offenses: internal service error")
    except requests.exceptions.HTTPError:
        log.error("Requests: HTTPError: status code %s for %s" % (str(resp.status_code), url))
    except requests.exceptions.Timeout:
        log.error("Requests: Timeout for %s" % url)
    except requests.exceptions.TooManyRedirects:
        log.error("Requests: TooManyRedirects for %s" % url)
    except requests.exceptions.ConnectionError:
        log.error("Requests: ConnectionError for %s" % url)
    return None

def post_offense(log, host, offense_id, basic_auth=None, token=None, params=None):
    url = host + "/api/siem/offenses/" + str(offense_id) + "?"

    if params:
        d = [k + "=" + quote(v) for k, v in params.items()]
        url += "&".join(d)
    if token:
        headers = {"SEC": token, "Accept": "application/json", "Content-Type": "application/json"}
    else:
        headers = {"Authorization": basic_auth, "Accept": "application/json", "Content-Type": "application/json"}
    try:
        resp = requests.post(url, data=None, json=None, headers=headers, verify=False)
        if resp.status_code == 200:
            return resp.json()
        elif resp.status_code == 403:
            log.error("Get Offenses: user does not have permission to assign an offense")
        elif resp.status_code == 404:
            log.error("Get Offenses: no offense found for provided id")
        elif resp.status_code == 409:
            log.error("Get Offenses: request cannot be completed due to state of the offense")
        elif resp.status_code == 422:
            log.error("Get Offenses: invalid parameter")
        elif resp.status_code == 500:
            log.error("Get Offenses: internal service error")
    except requests.exceptions.HTTPError:
        log.error("Requests: HTTPError: status code %s for %s" % (str(resp.status_code), url))
    except requests.exceptions.Timeout:
        log.error("Requests: Timeout for %s" % url)
    except requests.exceptions.TooManyRedirects:
        log.error("Requests: TooManyRedirects for %s" % url)
    except requests.exceptions.ConnectionError:
        log.error("Requests: ConnectionError for %s" % url)
    return None


def new_ariel_query(log, host, basic_auth=None, token=None, query=""):
    status_codes = {
        409: "The search cannot be created. The requested search ID that was provided in the query expression is already in use. Please use a unique search ID (or allow one to be generated)",
        422: "The query_expression contains invalid AQL syntax",
        500: "An error occurred during the attempt to create a new search",
        503: "The Ariel server might be temporarily unavailable or offline. Please try again later"
    }

    url = host + "/api/ariel/searches"

    if token:
        headers = {"SEC": token, "Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded"}
    else:
        headers = {"Authorization": basic_auth, "Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded"}

    payload = {
        "query_expression": query
    }

    try:
        r = requests.post(url, data=payload, headers=headers, verify=False)
        if r.status_code == 201:
            return r.json()
        else:
            error_message = status_codes[r.status_code]
            log.error(error_message)
    except requests.exceptions.HTTPError:
        log.error("Requests: HTTPError: status code %s for %s" % (str(r.status_code), url))
    except requests.exceptions.Timeout:
        log.error("Requests: Timeout for %s" % url)
    except requests.exceptions.TooManyRedirects:
        log.error("Requests: TooManyRedirects for %s" % url)
    except requests.exceptions.ConnectionError:
        log.error("Requests: ConnectionError for %s" % url)
    return None


def get_ariel_query_results(log, host, basic_auth=None, token=None, search_id=""):
    status_codes = {
        404: "The search does not exist",
        422: "A request parameter is not valid",
        500: "An error occurred while attempting to retrieve the search information",
        503: "The ariel server may be temporarily unavailable or offline. Please try again later"
    }

    url = host + "/api/ariel/searches/" + search_id

    if token:
        headers = {"SEC": token, "Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded"}
    else:
        headers = {"Authorization": basic_auth, "Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded"}

    try:
        r = requests.get(url, headers=headers, verify=False)
        if r.status_code == 200:
            return r.json()
        else:
            error_message = status_codes[r.status_code]
            log.error(error_message)
    except requests.exceptions.HTTPError:
        log.error("Requests: HTTPError: status code %s for %s" % (str(r.status_code), url))
    except requests.exceptions.Timeout:
        log.error("Requests: Timeout for %s" % url)
    except requests.exceptions.TooManyRedirects:
        log.error("Requests: TooManyRedirects for %s" % url)
    except requests.exceptions.ConnectionError:
        log.error("Requests: ConnectionError for %s" % url)
    return None


def add_data_to_reference_data_lists(log, host, basic_auth=None, token=None, payload={}):
    status_codes = {
        409: "The reference set could not be created, the name provided is already in use. Please change the name and try again",
        422: "A request parameter is not valid",
        500: "An error occurred while attempting to create the reference set",
    }

    url = host + "/api/reference_data/sets"

    if token:
        headers = {"SEC": token, "Accept": "application/json", "Content-Type": "application/json"}
    else:
        headers = {"Authorization": basic_auth, "Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded"}

    try:
        r = requests.post(url, headers=headers, data=payload, verify=False)
        log.info(r.status_code)
        if r.status_code == 201:
            return r.json()
        else:
            error_message = status_codes[r.status_code]
            log.error(error_message)
    except requests.exceptions.HTTPError:
        log.error("Requests: HTTPError: status code %s for %s" % (str(r.status_code), url))
    except requests.exceptions.Timeout:
        log.error("Requests: Timeout for %s" % url)
    except requests.exceptions.TooManyRedirects:
        log.error("Requests: TooManyRedirects for %s" % url)
    except requests.exceptions.ConnectionError:
        log.error("Requests: ConnectionError for %s" % url)
    return None


def test_auth(log, host, basic_auth=None, token=None):
    """Requires Offenses permissions"""
    url = host + "/api/siem/offense_types"

    if token:
        headers = {"SEC": token, "Accept": "application/json"}
    else:
        headers = {"Authorization": basic_auth, "Accept": "application/json"}
    try:
        resp = requests.get(url, headers=headers, verify=False)
        if resp.status_code == 200:
            return resp.json()
        elif resp.status_code == 422:
            log.error("Get Offenses: invalid parameter")
        elif resp.status_code == 500:
            log.error("Get Offenses: internal service error")
    except requests.exceptions.HTTPError:
        log.error("Requests: HTTPError: status code %s for %s" % (str(resp.status_code), url))
    except requests.exceptions.Timeout:
        log.error("Requests: Timeout for %s" % url)
    except requests.exceptions.TooManyRedirects:
        log.error("Requests: TooManyRedirects for %s" % url)
    except requests.exceptions.ConnectionError:
        log.error("Requests: ConnectionError for %s" % url)
    return None
