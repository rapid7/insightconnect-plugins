from typing import Optional
import datetime


class SiemUtils:
    @staticmethod
    def search_subject(all_results: list, subject: str) -> list:
        data = []
        for result in all_results:
            if result.get("subject") == subject:
                data.append(result)
        return data

    @staticmethod
    def search_url(all_results: list, url: str) -> list:
        data = []
        for result in all_results:
            if result.get("url") == url:
                data.append(result)
        return data

    @staticmethod
    def prepare_time_range(time_start: Optional[str], time_end: Optional[str], query_params: dict) -> dict:
        if not time_start and not time_end:
            query_params["sinceSeconds"] = "3600"
            return query_params
        elif not time_start:
            end = datetime.datetime.fromisoformat(time_end.lower().replace("z", ""))
            query_params["interval"] = f"{(end-datetime.timedelta(hours=1)).isoformat()}/{end.isoformat()}"
            return query_params
        elif not time_end:
            start = datetime.datetime.fromisoformat(time_start.lower().replace("z", ""))
            query_params["interval"] = f"{start.isoformat()}/{(start+datetime.timedelta(hours=1)).isoformat()}"
            return query_params
        else:
            start = datetime.datetime.fromisoformat(time_start.lower().replace("z", ""))
            end = datetime.datetime.fromisoformat(time_end.lower().replace("z", ""))
            query_params["interval"] = f"{start.isoformat()}/{end.isoformat()}"
            return query_params
