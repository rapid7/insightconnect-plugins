from datetime import datetime, timedelta, timezone

# A day is treated as 24 hours here. Cyber GRC stores due dates as UTC timestamps, so
# there is no tenant time zone to align a day boundary to.
DAY = timedelta(days=1)


def odata_datetime(moment: datetime) -> str:
    """OData v4 wants an unquoted datetimeoffset literal, e.g. 2026-01-21T20:30:44.407Z."""
    return moment.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"


def now() -> datetime:
    return datetime.now(timezone.utc)


def date_window_clauses(field: str, within_days: int, past_only: bool) -> list:
    """OData clauses narrowing a date field to a window ending now or in the future.

    Both options are upper bounds, so asking for both leaves the tighter one in force.
    The explicit null test states the intent that a record with no date in this field is
    not a record that is coming due.
    """
    clauses = []
    if within_days:
        clauses.append(f"{field} ne null and {field} le {odata_datetime(now() + abs(within_days) * DAY)}")
    if past_only:
        clauses.append(f"{field} ne null and {field} lt {odata_datetime(now())}")
    return clauses
