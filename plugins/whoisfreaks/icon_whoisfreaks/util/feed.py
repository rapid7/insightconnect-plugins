import csv
import datetime
import io
from dataclasses import dataclass, field
from typing import Callable, Optional

from icon_whoisfreaks.util import constants
from icon_whoisfreaks.util.outputs import to_float, to_int

_BOOLEAN_TEXT = {"t": True, "true": True, "f": False, "false": False}
_THREAT_BOOLEANS = ("is_seed", "is_extrapolated", "is_dropped", "is_parked")


@dataclass(frozen=True)
class FeedDefinition:
    feed_id: str
    label: str
    path: str
    status_path: tuple
    is_csv: bool
    columns: tuple
    normalizer: Callable[[dict], dict]
    domain_field: str
    params: dict = field(default_factory=dict)

    @property
    def identity(self) -> str:
        """Saved progress is only reused by a trigger configured for the same feed and format."""
        flags = ",".join(f"{key}={value}" for key, value in sorted(self.params.items()))
        return f"{self.feed_id}[{flags}]" if flags else self.feed_id


@dataclass(frozen=True)
class FeedWindow:
    available_from: datetime.date
    last_update: datetime.date

    def contains(self, day: datetime.date) -> bool:
        return self.available_from <= day <= self.last_update


@dataclass
class FeedPage:
    rows: list
    raw_count: int
    last_line: Optional[str] = None
    header_missing: bool = False
    invalid_lines: int = 0


def to_timestamp(value: str) -> str:
    """Convert WhoisFreaks timestamps such as 2026-10-11 00:16:16.035483+00 to ISO 8601."""
    text = value.strip()
    candidate = text[:-3] + "+00:00" if text.endswith("+00") else text
    try:
        return datetime.datetime.fromisoformat(candidate).isoformat()
    except ValueError:
        return text


def _boolean(value: str) -> Optional[bool]:
    return _BOOLEAN_TEXT.get(value.strip().lower())


def normalize_threat_row(row: dict) -> dict:
    result = {}
    for key, value in row.items():
        value = value.strip()
        if not value:
            continue
        if key in _THREAT_BOOLEANS:
            result[key] = _boolean(value)
        elif key == "confidence":
            result[key] = to_float(value)
        elif key in ("first_seen", "last_seen"):
            result[key] = to_timestamp(value)
        elif key == "matched_pivots":
            result[key] = [pivot.strip() for pivot in value.split("|") if pivot.strip()]
        elif key == "domain":
            result[key] = value.lower()
        else:
            result[key] = value
    return {key: value for key, value in result.items() if value is not None}


def normalize_nrd_whois_row(row: dict) -> dict:
    result = {}
    for key, value in row.items():
        value = value.strip()
        if not value:
            continue
        if key == "num":
            result[key] = to_int(value)
        elif key == "query_time":
            result[key] = to_timestamp(value)
        elif key == "domain_name":
            result[key] = value.lower()
        else:
            result[key] = value
    return {key: value for key, value in result.items() if value is not None}


def normalize_nrd_domain(row: dict) -> dict:
    return {"domain_name": row["domain_name"].strip().lower()}


def nrd_feed(family: str, include_whois: bool) -> FeedDefinition:
    return FeedDefinition(
        feed_id=f"newly.{family}",
        label=f"Newly registered {family} domains feed",
        path=constants.PATH_NRD_STREAM.format(family=family),
        status_path=("newly", family),
        is_csv=include_whois,
        columns=tuple(constants.NRD_WHOIS_COLUMNS) if include_whois else ("domain_name",),
        normalizer=normalize_nrd_whois_row if include_whois else normalize_nrd_domain,
        domain_field="domain_name",
        params={"whois": "true" if include_whois else "false"},
    )


def threat_feed(threat_type: str) -> FeedDefinition:
    return FeedDefinition(
        feed_id=f"threat_feed.{threat_type}",
        label=f"{threat_type.capitalize()} threat feed",
        path=constants.PATH_THREAT_STREAM.format(threat_type=threat_type),
        status_path=("threat_feed", threat_type),
        is_csv=True,
        columns=tuple(constants.THREAT_FEED_COLUMNS),
        normalizer=normalize_threat_row,
        domain_field="domain",
    )


def _parse_date(value) -> Optional[datetime.date]:
    try:
        return datetime.datetime.strptime(str(value), constants.DATE_FORMAT).date()
    except ValueError:
        return None


def resolve_window(status: dict, status_path: tuple) -> Optional[FeedWindow]:
    """Read a feed's availability window from the status document. None means the feed has no data."""
    node = status
    for key in status_path:
        node = node.get(key) if isinstance(node, dict) else None
    if not isinstance(node, dict):
        return None
    available_from, last_update = _parse_date(node.get("available_from")), _parse_date(node.get("last_update"))
    if available_from is None or last_update is None or available_from > last_update:
        return None
    return FeedWindow(available_from, last_update)


def _parse_csv(text: str, feed: FeedDefinition) -> FeedPage:
    table = [row for row in csv.reader(io.StringIO(text, newline="")) if any(cell.strip() for cell in row)]
    header_present = bool(table) and table[0][0].strip().lower() == feed.columns[0]
    header = [cell.strip() for cell in table[0]] if header_present else list(feed.columns)
    data = table[1:] if header_present else table
    rows = []
    for values in data:
        values = (values + [""] * len(header))[: len(header)]
        rows.append(feed.normalizer(dict(zip(header, values))))
    return FeedPage(rows=rows, raw_count=len(data), header_missing=bool(data) and not header_present)


def _looks_like_domain(text: str) -> bool:
    return "." in text and " " not in text and "," not in text and len(text) <= 253


def _parse_lines(text: str, feed: FeedDefinition, previous_last_line: Optional[str]) -> FeedPage:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    # Past the end of a date, the plain domain list repeats the last line of the previous page
    if previous_last_line and lines and lines[0] == previous_last_line:
        lines = lines[1:]
    valid = [line for line in lines if _looks_like_domain(line)]
    rows = [feed.normalizer({"domain_name": line}) for line in valid]
    return FeedPage(
        rows=rows,
        raw_count=len(lines),
        last_line=lines[-1] if lines else previous_last_line,
        invalid_lines=len(lines) - len(valid),
    )


def parse_page(text: Optional[str], feed: FeedDefinition, previous_last_line: Optional[str] = None) -> FeedPage:
    if not text or not text.strip():
        return FeedPage(rows=[], raw_count=0, last_line=previous_last_line)
    if feed.is_csv:
        return _parse_csv(text, feed)
    return _parse_lines(text, feed, previous_last_line)


def build_row_filter(feed: FeedDefinition, keywords: list, tlds: list, min_confidence: Optional[float]) -> Callable:
    def accept(row: dict) -> bool:
        domain = str(row.get(feed.domain_field, ""))
        if keywords and not any(keyword in domain for keyword in keywords):
            return False
        if tlds and not any(domain == tld or domain.endswith(f".{tld}") for tld in tlds):
            return False
        if min_confidence is not None:
            confidence = row.get("confidence")
            return confidence is not None and confidence >= min_confidence
        return True

    return accept
