from datetime import datetime
from typing import Dict, Any

from dateutil.parser import parse


class EventLogs:
    DATETIME = "datetime"
    FILTER_DATETIME = "filter_datetime"

    def __init__(self, data: Dict[str, Any]) -> None:
        self.data: Dict[str, Any] = data
        self._convert_datetime()

    def _convert_datetime(self) -> None:
        if date := self.data.get(self.DATETIME):
            self.data[self.FILTER_DATETIME] = parse(date, ignoretz=True)

    def get_dict(self) -> Dict[str, Any]:
        return self.__dict__["data"]

    def compare_datetime(self, other: datetime):
        return self.data[self.FILTER_DATETIME] >= other
