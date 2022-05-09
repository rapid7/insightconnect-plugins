class Investigations:

    # Methods to populate Investigation endpoints

    @staticmethod
    def list_investigations(console_url: str):
        """
        URI for listing investigations
        :param console_url: URL to the InsightIDR console
        :return: pre-populated /idr/v1/investigations/
        """

        return f"{console_url}idr/v1/investigations"

    @staticmethod
    def close_investigations_in_bulk(console_url: str):
        """
        URI for closing investigations in bulk
        :param console_url: URL to the InsightIDR console
        :return: TODO
        """

        return f"{console_url}idr/v1/investigations/bulk_close"

    @staticmethod
    def set_the_status_of_an_investigation(console_url: str, idr_id: str, status: str):
        """
        URI for setting the status of an investigation
        :param console_url: URL to the InsightIDR console
        :param idr_id: the ID of the investigation
        :param status: The status to change the investigation to
        :return: pre-populated /idr/v1/investigations/{id}/status/{status}
        """

        return f"{console_url}idr/v1/investigations/{idr_id}/status/{status}"

    @staticmethod
    def set_user_for_investigation(base_url: str, investigation_id: str) -> str:
        return f"{base_url}idr/v1/investigations/{investigation_id}/assignee"


class Threats:
    @staticmethod
    def add_indicators_to_a_threat(console_url: str, key: str):
        """
        URI for adding indicators_to_a_threat
        :param console_url: URL to the InsightIDR console
        :param key: The key of a threat for which the indicators are going to be added
        :return: pre-populated /idr/v1/customthreats/key/{key}/indicators/add
        """

        return f"{console_url}idr/v1/customthreats/key/{key}/indicators/add"

    @staticmethod
    def create_threat(console_url: str):
        """
        URI for create custom threat
        :param console_url: URL to the InsightIDR console
        :return: pre-populated /idr/v1/customthreats
        """

        return f"{console_url}idr/v1/customthreats"


class QueryLogs:
    @staticmethod
    def get_query_logs(console_url: str, log_id: str):
        """
        URI for adding get_query_logs
        :param console_url: URL to the InsightIDR console
        :param log_id: The ID of a log for which the indicators are going to be added
        :return: pre-populated /query/logs/{log_id}
        """

        return f"{console_url}query/logs/{log_id}"


class Queries:
    @staticmethod
    def get_all_queries(console_url: str):
        """
        URI for retrieving all saved queries
        :param console_url: URL to the InsightIDR console
        :return: pre-populated /query/saved_queries
        """
        return f"{console_url}query/saved_queries"

    @staticmethod
    def get_query_by_id(console_url: str, query_id: str):
        """
        URI for retrieving a query
        :param console_url: URL to the InsightIDR console
        :param query_id: The ID of a query which is to be retrieved
        :return: pre-populated /query/saved_queries/{query_id}
        """
        return f"{console_url}query/saved_queries/{query_id}"


class Logs:
    @staticmethod
    def get_a_log(console_url: str, log_id: str):
        """
        URI for adding get_query_logs
        :param console_url: URL to the InsightIDR console
        :param log_id: The ID of a log for which the indicators are going to be added
        :return: pre-populated /management/logs/{logId}
        """

        return f"{console_url}log_search/management/logs/{log_id}"

    @staticmethod
    def get_all_logs(console_url: str):
        """
        URI for adding get_query_logs
        :param console_url: URL to the InsightIDR console
        :return: pre-populated /management/logs
        """

        return f"{console_url}log_search/management/logs"
