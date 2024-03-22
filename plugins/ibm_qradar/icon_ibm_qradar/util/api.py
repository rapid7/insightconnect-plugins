import requests

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_ibm_qradar.util.url import URL
from icon_ibm_qradar.util.constants.endpoints import (
    POST_OFFENSES_NOTES,
    GET_OFFENSES_NOTES,
    GET_OFFENSES_NOTES_BY_ID,
    GET_CLOSING_REASON_ENDPOINT,
    GET_OFFENSES_ENDPOINT,
    UPDATE_OFFENSES_ENDPOINT,
    GET_ASSETS_ENDPOINT,
    START_ARIEL_SEARCH_ENDPOINT,
    GET_ARIEL_SEARCH_BY_ID_ENDPOINT,
)
from icon_ibm_qradar.util.constants.constant import REQUEST_TIMEOUT
from icon_ibm_qradar.util.utils import prepare_request_params, handle_response, get_default_header


class IBMQRadarAPI:
    def __init__(self, connection, logger) -> None:
        self.connection = connection
        self.logger = logger

    def add_notes_to_offense_request(self, offense_id, params, query_params, fields):
        url_obj = URL(self.connection.host_url, POST_OFFENSES_NOTES)
        basic_url = url_obj.get_basic_url()
        if offense_id:
            basic_url = basic_url.format(offense_id=offense_id)
        url_obj.set_basic_url(basic_url)
        basic_url, headers = prepare_request_params(params, self.logger, url_obj, fields, query_params)

        return self.make_request(method="POST", url=basic_url, headers=headers)

    def get_offense_note_request(self, offense_id, params, fields):
        url_obj = URL(self.connection.host_url, GET_OFFENSES_NOTES)
        basic_url = url_obj.get_basic_url()
        if offense_id:
            basic_url = basic_url.format(offense_id=offense_id)
        url_obj.set_basic_url(basic_url)
        basic_url, headers = prepare_request_params(params, self.logger, url_obj, fields)

        return self.make_request(method="GET", url=basic_url, headers=headers)

    def get_offense_note_by_id_request(self, offense_id, note_id, params, fields):
        url_obj = URL(self.connection.host_url, GET_OFFENSES_NOTES_BY_ID)
        basic_url = url_obj.get_basic_url()
        if offense_id:
            basic_url = basic_url.format(offense_id=offense_id, note_id=note_id)
        url_obj.set_basic_url(basic_url)
        basic_url, headers = prepare_request_params(params, self.logger, url_obj, fields)

        return self.make_request(method="GET", url=basic_url, headers=headers)

    def get_offenses_request(self, params, fields):
        url_obj = URL(self.connection.host_url, GET_OFFENSES_ENDPOINT)
        basic_url = url_obj.get_basic_url()
        url_obj.set_basic_url(basic_url)
        basic_url, headers = prepare_request_params(params, self.logger, url_obj, fields)

        return self.make_request(method="GET", url=basic_url, headers=headers)

    def get_offense_closing_reasons_request(self, params, query_params, fields):
        url_obj = URL(self.connection.host_url, GET_CLOSING_REASON_ENDPOINT)
        basic_url = url_obj.get_basic_url()
        url_obj.set_basic_url(basic_url)
        basic_url, headers = prepare_request_params(params, self.logger, url_obj, fields, query_params)

        return self.make_request(method="GET", url=basic_url, headers=headers)

    def get_assets_request(self, params, fields):
        url_obj = URL(self.connection.host_url, GET_ASSETS_ENDPOINT)
        basic_url = url_obj.get_basic_url()
        url_obj.set_basic_url(basic_url)
        basic_url, headers = prepare_request_params(params, self.logger, url_obj, fields)

        return self.make_request(method="GET", url=basic_url, headers=headers)

    def update_offense_request(self, offense_id, params, query_params, fields):
        url_obj = URL(self.connection.host_url, UPDATE_OFFENSES_ENDPOINT)
        basic_url = url_obj.get_basic_url()
        if offense_id:
            basic_url = basic_url.format(offense_id=offense_id)
        url_obj.set_basic_url(basic_url)
        basic_url, headers = prepare_request_params(params, self.logger, url_obj, fields, query_params)

        return self.make_request(method="POST", url=basic_url, headers=headers)

    def start_ariel_request(self, params, query_params, fields):
        url_obj = URL(self.connection.host_url, START_ARIEL_SEARCH_ENDPOINT)
        basic_url = url_obj.get_basic_url()
        url_obj.set_basic_url(basic_url)
        basic_url, headers = prepare_request_params(params, self.logger, url_obj, fields, query_params)

        return self.make_request(method="POST", url=basic_url, headers=headers)

    def get_ariel_request(self, search_id, poll_interval):
        url_obj = URL(self.connection.host_url, GET_ARIEL_SEARCH_BY_ID_ENDPOINT)
        basic_url = url_obj.get_basic_url()
        if search_id:
            basic_url = basic_url.format(search_id=search_id)

        headers = get_default_header()
        if poll_interval != 0:
            headers["Prefer"] = f"wait={poll_interval}"

        return self.make_request(method="GET", url=basic_url, headers=headers)

    def make_request(self, method, url, headers):
        auth = (self.connection.username, self.connection.password)
        try:
            self.logger.debug(f"Final URL: {url}")
            response = requests.request(
                method,
                url=url,
                headers=headers,
                data={},
                auth=auth,
                verify=self.connection.verify_ssl,
                timeout=REQUEST_TIMEOUT,
            )
        except requests.exceptions.ConnectionError:
            raise PluginException(preset=PluginException.Preset.SERVICE_UNAVAILABLE)

        return handle_response(response)
