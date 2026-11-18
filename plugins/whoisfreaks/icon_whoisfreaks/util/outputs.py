from typing import Any, Iterable, Optional

from icon_whoisfreaks.util.client import LookupResult

_TRUE = {"true", "yes", "t", "1", "y"}
_FALSE = {"false", "no", "f", "0", "n"}


def get_path(data: Any, *keys: str) -> Any:
    """Read a nested value, returning None when any level is missing or not an object."""
    for key in keys:
        if not isinstance(data, dict):
            return None
        data = data.get(key)
    return data


def first_of(data: dict, *keys: str) -> Any:
    for key in keys:
        if isinstance(data, dict) and data.get(key) is not None:
            return data[key]
    return None


def to_int(value: Any) -> Optional[int]:
    if isinstance(value, bool) or value is None:
        return None
    if isinstance(value, int):
        return value
    try:
        number = float(str(value).strip())
    except ValueError:
        return None
    return int(number) if number.is_integer() else None


def to_float(value: Any) -> Optional[float]:
    if isinstance(value, bool) or value is None:
        return None
    try:
        return float(str(value).strip())
    except ValueError:
        return None


def to_bool(value: Any) -> Optional[bool]:
    if isinstance(value, bool):
        return value
    text = str(value).strip().lower() if value is not None else ""
    if text in _TRUE:
        return True
    if text in _FALSE:
        return False
    return None


def to_str(value: Any) -> Optional[str]:
    if value is None or isinstance(value, (dict, list)):
        return None
    text = str(value).strip()
    return text or None


def to_str_list(value: Any) -> Optional[list]:
    if not isinstance(value, list):
        return None
    return [text for text in (to_str(item) for item in value) if text]


def to_object_list(value: Any) -> list:
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, dict)]


def compact(output: dict) -> dict:
    return {key: value for key, value in output.items() if value is not None}


def without_keys(data: Any, names: Iterable[str]) -> Any:
    """Return a copy of data with the named keys removed at every level."""
    names = set(names)
    if isinstance(data, dict):
        return {key: without_keys(value, names) for key, value in data.items() if key not in names}
    if isinstance(data, list):
        return [without_keys(item, names) for item in data]
    return data


def not_looked_up(message: str) -> dict:
    return {"found": False, "message": message}


def single(result: LookupResult, extra: Optional[dict] = None, include_response: bool = True) -> dict:
    output = {
        "found": result.found and bool(result.data_dict),
        "status_code": result.status_code,
        "message": result.message or None,
    }
    if include_response and result.data_dict:
        output["response"] = result.data_dict
    if result.found:
        output.update(extra or {})
    return compact(output)


def paged(result: LookupResult, records_key: str, total_keys: tuple, pages_keys: tuple, page_keys: tuple) -> dict:
    data = result.data_dict
    records = to_object_list(data.get(records_key))
    output = {
        "found": result.found and bool(records),
        "status_code": result.status_code,
        "message": result.message or (None if records or not result.found else "No records found"),
        "records": records,
        "total_records": to_int(first_of(data, *total_keys)),
        "total_pages": to_int(first_of(data, *pages_keys)),
        "current_page": to_int(first_of(data, *page_keys)),
    }
    return compact(output)


def bulk(result: Optional[LookupResult], records_key: Optional[str], skipped: list) -> dict:
    if result is None:
        return {"results": [], "skipped": skipped}
    data = result.data
    records = data if records_key is None else get_path(data, records_key)
    return compact({"status_code": result.status_code, "results": to_object_list(records), "skipped": skipped})
