from datetime import datetime, timezone


def datetime_with_timezone(raw_datetime, tz):
    # Apply UTC timezone; pysmb times are float of seconds from epoch with no timezone defined
    dt = datetime.fromtimestamp(raw_datetime).replace(tzinfo=timezone.utc)
    return dt.astimezone(tz)