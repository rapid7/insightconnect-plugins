from datetime import datetime, timedelta


class Util:
    @staticmethod
    def clean_json(obj: dict) -> dict:
        """
        Helper method that cleans json returned from calls to the
        'issues' endpoint.

        :param obj: JSON object to be cleaned.
        :return: Cleaned JSON object
        """
        new_json = []
        for key, value in obj.items():
            if value is None:
                value = ""
            if key in ("assignee", "milestone") and value == "":
                value = {}
            new_json.append((key, value))

        return dict(new_json)

    @staticmethod
    def is_issue_new(date: str) -> bool:
        """
        Method that returns True or False if the input time is before
        or after last 15 seconds.

        :param date: Datetime string
        :return: True or False
        """

        # Get current time
        time_now = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        time_now = datetime.strptime(time_now, "%Y-%m-%dT%H:%M:%S.%fZ")

        # Get current time minus 30 seconds
        acceptable = time_now - timedelta(0, 30)

        # Get and convert the 'updated_at' time
        updated_at_delta = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")
        
        if updated_at_delta > acceptable:
            return False
        return True
