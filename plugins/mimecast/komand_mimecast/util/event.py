from datetime import datetime
from typing import Dict, Any
from logging import Logger

from dateutil.parser import parse
from insightconnect_plugin_runtime.helper import get_time_now


class EventLogs:
    DATETIME = "datetime"
    FILTER_DATETIME = "filter_datetime"

    def __init__(self, data: Dict[str, Any], logger: Logger) -> None:
        self.data: Dict[str, Any] = data
        self.logger = logger
        self._convert_datetime()

    def _convert_datetime(self) -> None:
        if date := self.data.get(self.DATETIME):
            self.data[self.FILTER_DATETIME] = parse(date, ignoretz=True)
        else:
            # if there is no datetime field that is returned from Mimecast we will use the current time as we want to try and ingest the log
            self.logger.warning(f"There was no datetime key for the following event: {self.data}")
            self.data[self.FILTER_DATETIME] = get_time_now()

    def get_dict(self) -> Dict[str, Any]:
        return self.__dict__["data"]

    def compare_datetime(self, other: datetime):
        return self.data[self.FILTER_DATETIME] >= other
