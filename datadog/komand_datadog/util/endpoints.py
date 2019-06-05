class Events:

    @staticmethod
    def events(console_url: str):
        """
        URI for all events operations
        :param console_url: URL to the Datadog console
        :return: pre-populated events
        """
        return f'{console_url}events/'

class Metrics:

    @staticmethod
    def post_metrics(console_url: str):
        """
        URI for all events operations
        :param console_url: URL to the Datadog console
        :return: pre-populated events
        """
        return f'{console_url}series/'

