class Util:
    @staticmethod
    def map_region(region: str) -> str:
        """
        URI for listing investigations
        :param region: The region code for the InsightIDR API to be mapped
        :return: Region-code
        """
        region_map = {
            "United States 1": "us",
            "United States 2": "us2",
            "United States 3": "us3",
            "Europe": "eu",
            "Canada": "ca",
            "Australia": "au",
            "Japan": "ap",
        }
        return region_map.get(region, "us")


class Investigations:
    # Methods to populate Investigation endpoints

    @staticmethod
    def connection_api_url(region_code: str) -> str:
        """
        URI for listing investigations
        :param region_code: The region code for the InsightIDR API to be mapped
        :return: pre-populated /idr/v2/investigations/
        """
        return f"https://{Util.map_region(region_code)}.api.insight.rapid7.com/"

    @staticmethod
    def list_investigations(console_url: str) -> str:
        """
        URI for listing investigations
        :param console_url: URL to the InsightIDR console
        :return: pre-populated /idr/v2/investigations/
        """

        return f"{console_url}idr/v2/investigations"

    @staticmethod
    def create_investigation(console_url: str) -> str:
        """
        URI for creating investigation
        :param console_url: URL to the InsightIDR console
        :return: pre-populated /idr/v2/investigations/
        """

        return f"{console_url}idr/v2/investigations"

    @staticmethod
    def search_investigation(console_url: str) -> str:
        """
        URI for searching investigation
        :param console_url: URL to the InsightIDR console
        :return: pre-populated /idr/v2/investigations/
        """

        return f"{console_url}idr/v2/investigations/_search"

    @staticmethod
    def update_or_get_investigation(console_url: str, identifier: str) -> str:
        """
        URI for updating investigation
        :param console_url: URL to the InsightIDR console
        :param identifier: The ID or RRN of investigation
        :return: pre-populated /idr/v2/investigations/
        """

        return f"{console_url}idr/v2/investigations/{identifier}"

    @staticmethod
    def set_the_priority_of_an_investigation(console_url: str, identifier: str, priority: str) -> str:
        """
        URI for setting the status of an investigation
        :param console_url: URL to the InsightIDR console
        :param identifier: the ID or RRN of the investigation
        :param priority: The priority to change the investigation to
        :return: pre-populated /idr/v1/investigations/{identifier}/priority/{priority}
        """

        return f"{console_url}idr/v2/investigations/{identifier}/priority/{priority}"

    @staticmethod
    def set_the_disposition_of_an_investigation(console_url: str, identifier: str, disposition: str) -> str:
        """
        URI for setting the status of an investigation
        :param console_url: URL to the InsightIDR console
        :param identifier: the ID or RRN of the investigation
        :param disposition: The disposition to change the investigation to
        :return: pre-populated /idr/v1/investigations/{identifier}/disposition/{disposition}
        """

        return f"{console_url}idr/v2/investigations/{identifier}/disposition/{disposition}"

    @staticmethod
    def list_alerts_for_investigation(console_url: str, identifier: str) -> str:
        """
        URI for setting the status of an investigation
        :param console_url: URL to the InsightIDR console
        :param identifier: the ID or RRN of the investigation
        :return: pre-populated /idr/v1/investigations/{identifier}/alerts
        """

        return f"{console_url}idr/v2/investigations/{identifier}/alerts"

    @staticmethod
    def close_investigations_in_bulk(console_url: str) -> str:
        """
        URI for closing investigations in bulk
        :param console_url: URL to the InsightIDR console
        :return: TODO
        """

        return f"{console_url}idr/v1/investigations/bulk_close"

    @staticmethod
    def set_the_status_of_an_investigation(console_url: str, identifier: str, status: str) -> str:
        """
        URI for setting the status of an investigation
        :param console_url: URL to the InsightIDR console
        :param identifier: the ID of the investigation
        :param status: The status to change the investigation to
        :return: pre-populated /idr/v1/investigations/{id}/status/{status}
        """

        return f"{console_url}idr/v2/investigations/{identifier}/status/{status}"

    @staticmethod
    def set_user_for_investigation(base_url: str, investigation_id: str) -> str:
        return f"{base_url}idr/v2/investigations/{investigation_id}/assignee"


class Threats:
    @staticmethod
    def add_indicators_to_a_threat(console_url: str, key: str) -> str:
        """
        URI for adding indicators_to_a_threat
        :param console_url: URL to the InsightIDR console
        :param key: The key of a threat for which the indicators are going to be added
        :return: pre-populated /idr/v1/customthreats/key/{key}/indicators/add
        """

        return f"{console_url}idr/v1/customthreats/key/{key}/indicators/add"

    @staticmethod
    def replace_indicators(console_url: str, key: str) -> str:
        """
        URI for create custom threat
        :param console_url: URL to the InsightIDR console
        :param key: The key of a threat for which the indicators are going to be added
        :return: pre-populated /idr/v1/customthreats/key/{key}/indicators/replace
        """

        return f"{console_url}idr/v1/customthreats/key/{key}/indicators/replace"

    @staticmethod
    def create_threat(console_url: str) -> str:
        """
        URI for create custom threat
        :param console_url: URL to the InsightIDR console
        :return: pre-populated /idr/v1/customthreats
        """

        return f"{console_url}idr/v1/customthreats"


class QueryLogs:
    @staticmethod
    def get_query_logs(region_code: str, log_id: str) -> str:
        """
        URI for adding get_query_logs
        :param region_code: The region code for the InsightIDR API to be mapped
        :param log_id: The ID of a log for which the indicators are going to be added
        :return: pre-populated /query/logs/{log_id}
        """

        return f"https://{Util.map_region(region_code)}.rest.logs.insight.rapid7.com/query/logs/{log_id}"


class Queries:
    @staticmethod
    def get_all_queries(region_code: str) -> str:
        """
        URI for retrieving all saved queries
        :param region_code: The region code for the InsightIDR API to be mapped
        :return: pre-populated /query/saved_queries
        """
        return f"https://{Util.map_region(region_code)}.rest.logs.insight.rapid7.com/query/saved_queries"

    @staticmethod
    def get_query_by_id(region_code: str, query_id: str) -> str:
        """
        URI for retrieving a query
        :param region_code: The region code for the InsightIDR API to be mapped
        :param query_id: The ID of a query which is to be retrieved
        :return: pre-populated /query/saved_queries/{query_id}
        """
        return f"https://{Util.map_region(region_code)}.rest.logs.insight.rapid7.com/query/saved_query/{query_id}"


class Logs:
    @staticmethod
    def get_a_log(console_url: str, log_id: str) -> str:
        """
        URI for adding get_query_logs
        :param console_url: URL to the InsightIDR console
        :param log_id: The ID of a log for which the indicators are going to be added
        :return: pre-populated /management/logs/{logId}
        """

        return f"{console_url}log_search/management/logs/{log_id}"

    @staticmethod
    def get_all_logs(console_url: str) -> str:
        """
        URI for adding get_query_logs
        :param console_url: URL to the InsightIDR console
        :return: pre-populated /management/logs
        """

        return f"{console_url}log_search/management/logs"


class Comments:
    @staticmethod
    def comments(console_url: str) -> str:
        return f"{console_url}idr/v1/comments"

    @staticmethod
    def delete_comment(console_url: str, comment_rrn: str) -> str:
        return f"{console_url}idr/v1/comments/{comment_rrn}"


class Attachments:
    @staticmethod
    def attachment(console_url: str, attachment_rrn: str) -> str:
        return f"{console_url}idr/v1/attachments/{attachment_rrn}"

    @staticmethod
    def attachments(console_url: str) -> str:
        return f"{console_url}idr/v1/attachments"

    @staticmethod
    def get_attachment_information(console_url: str, attachment_rrn: str) -> str:
        return f"{console_url}idr/v1/attachments/{attachment_rrn}/metadata"


class Users:
    @staticmethod
    def get_user_information(console_url: str, attachment_rrn: str) -> str:
        return f"{console_url}idr/v1/users/{attachment_rrn}"


class Assets:
    @staticmethod
    def get_asset_information(console_url: str, attachment_rrn: str) -> str:
        return f"{console_url}idr/v1/assets/{attachment_rrn}"
