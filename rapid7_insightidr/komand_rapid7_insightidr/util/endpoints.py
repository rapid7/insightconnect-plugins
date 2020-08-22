class Investigations:

    # Methods to populate Investigation endpoints

    @staticmethod
    def list_investigations(console_url: str):
        """
        URI for listing investigations
        :param console_url: URL to the InsightIDR console
        :return: pre-populated /idr/v1/investigations/
        """

        return f'{console_url}idr/v1/investigations'

    @staticmethod
    def close_investigations_in_bulk(console_url: str):
        """
        URI for closing investigations in bulk
        :param console_url: URL to the InsightIDR console
        :return: TODO
        """

    @staticmethod
    def set_the_status_of_an_investigation(console_url: str, idr_id: str, status: str):
        """
        URI for setting the status of an investigation
        :param console_url: URL to the InsightIDR console
        :param idr_id: the ID of the investigation
        :param status: The status to change the investigation to
        :return: pre-populated /idr/v1/investigations/{id}/status/{status}
        """

        return f'{console_url}idr/v1/investigations/{idr_id}/status/{status}'

    @staticmethod
    def set_user_for_investigation(base_url: str, investigation_id: str)->str:
        return f'{base_url}idr/v1/investigations/{investigation_id}/assignee'


class Threats:

    @staticmethod
    def add_indicators_to_a_threat(console_url: str, key: str):
        """
        URI for adding indicators_to_a_threat
        :param console_url: URL to the InsightIDR console
        :param key: The key of a threat for which the indicators are going to be added
        :return: pre-populated /idr/v1/customthreats/key/{key}/indicators/add
        """

        return f'{console_url}idr/v1/customthreats/key/{key}/indicators/add'
