import json
from datetime import datetime


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
        output = json.dumps(dict(new_json))
        return json.loads(output)

    @staticmethod
    def is_issue_new(date: str) -> bool:
        """
        Method that returns True or False if the input time is before
        or after last 15 seconds.

        :param date: Datetime string
        :return: True or False
        """
        acceptable = "0:00:30.000000"  # last 15 sec
        #'0:00:15.761923'
        time_now = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        time_now = datetime.strptime(time_now, "%Y-%m-%dT%H:%M:%S.%fZ")

        date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")

        difference = str(time_now - date)
        if difference > acceptable:
            return False
        return True
