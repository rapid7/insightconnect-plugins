from datetime import datetime
from typing import Dict, Any

from dateutil.parser import parse


class EventLogs:
    DATETIME = "datetime"

    def __init__(self, data: Dict[str, Any]) -> None:
        self.data: Dict[str, Any] = data
        self._convert_datetime()

    def _convert_datetime(self) -> None:
        if date := self.data.get(self.DATETIME):
            self.data[self.DATETIME] = parse(date, ignoretz=True)

    def get_dict(self) -> Dict[str, Any]:
        temp_dict = self.__dict__["data"]
        if date := temp_dict.get(self.DATETIME):
            temp_dict[self.DATETIME] = date.isoformat()
        return temp_dict

    def compare_datetime(self, other: datetime):
        return self.data[self.DATETIME] >= other
