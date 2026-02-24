from copy import deepcopy
from datetime import datetime, timezone
from logging import Logger
from typing import Any, Dict, List, Optional

from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import open_cachefile

from icon_luminar.util.constants import LUMINAR_DATE_FORMAT, STIX_PARSER


def get_last_run(cache_file: str, logger: Logger) -> Optional[str]:
    """Fetch last run time from cache file (if exists)."""
    try:
        with open_cachefile(cache_file) as f:
            f.seek(0)  # move to beginning
            content = f.read().strip()
            return content or None
    except Exception as e:
        logger.error("Failed to read last run: %s", e)
        raise PluginException(
            cause="Error appear while reading contents from cache file.",
            assistance="Please contact support for assistance.",
            data=e,
        )


def save_last_run(cache_file: str, run_time: str, logger: Logger) -> None:
    """Save current run time into cache file."""
    try:
        with open_cachefile(cache_file, append=False) as f:
            f.seek(0)
            f.truncate()  # overwrite file
            f.write(run_time)
            f.flush()
        logger.info("Saved last run to %s : %s", cache_file, run_time)
    except Exception as e:
        logger.error("Failed to save last run: %s", e)
        raise PluginException(
            cause="Error appear while saving contents to cache file.",
            assistance="Please contact support for assistance.",
            data=e,
        )


def next_checkpoint() -> str:
    """Get current UTC time in ISO 8601 format with microseconds."""

    current_time = datetime.now(timezone.utc)
    return (
        current_time.strftime("%Y-%m-%dT%H:%M:%S.") + f"{current_time.microsecond:06d}Z"
    )


def check_created_date(obj_date: str, from_date: str, logger: Logger) -> bool:
    """
    Validate whether the given object creation date is >= from_date.

    Args:
        obj_date: Creation date of the object in ISO 8601 format.
        from_date: Threshold date in ISO 8601 format.
    """
    try:
        return datetime.strptime(obj_date, LUMINAR_DATE_FORMAT) >= datetime.strptime(
            from_date, LUMINAR_DATE_FORMAT
        )
    except Exception as ex:
        logger.info(f"Invalid date format: {obj_date}; {ex}")
        return False


def filtered_records(
    records: List[Dict[str, Any]], from_date: str, logger: Logger
) -> List[Dict[str, Any]]:
    """Filter records created after from_date."""
    return [
        record
        for record in records
        if not record.get("created")
        or check_created_date(record["created"], from_date, logger)
    ]


def is_valid_date(date_str: str) -> bool:
    """
    Checks if a given string is a valid date in the format 'YYYY-MM-DD'.

    Args:
        date_str (str): The date string to validate.

    Returns:
        bool: True if the string is a valid date, False otherwise.
    """
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def get_ioc_from_pattern(pattern: str, logger: Logger) -> List[Dict[str, str]]:
    """
    Extract IOC type and value from a STIX pattern string.

    Returns:
        A list of {"type": ..., "value": ...} dictionaries.
    """
    iocs: List[Dict[str, str]] = []
    if not isinstance(pattern, str):
        logger.error("Unexpected pattern type: %s", type(pattern))
        return iocs

    try:
        matches = STIX_PARSER.findall(pattern)
    except TypeError as err:
        logger.warning("Error parsing STIX pattern: %s (%s)", pattern, err)
        return iocs

    for stix_type, stix_property, value in matches:
        indicator_type = (
            f"{stix_type}:{stix_property}" if stix_type == "file" else stix_type
        )
        iocs.append({"type": indicator_type, "value": value})

    return iocs


def create_lookup_dict(
    list_of_dicts: List[Dict[str, Any]],
) -> Dict[str, Dict[str, Any]]:
    """Convert a list of dictionaries into a lookup dictionary indexed by 'id'."""
    return {d["id"]: d for d in list_of_dicts if "id" in d}


def enrich_indicator(obj: Dict[str, Any], logger: Logger) -> Dict[str, Any]:
    """Add IOCs to indicator object if pattern exists."""
    if obj.get("type") == "indicator":
        iocs = get_ioc_from_pattern(obj.get("pattern", ""), logger)
        if iocs:
            obj["iocs"] = iocs
    return obj


def create_associations(
    records: List[Dict[str, Any]], logger: Logger
) -> List[Dict[str, Any]]:
    """
    Create parent-child associations from STIX relationship objects.
    Enrich child indicators with extracted IOCs.
    """
    lookup = create_lookup_dict(records)
    associations: List[Dict[str, Any]] = []

    # --- relationships ---
    rel_objs = [r for r in records if r.get("type") == "relationship"]
    for rel in rel_objs:
        target = lookup.get(rel.get("target_ref"))
        source = lookup.get(rel.get("source_ref"))
        if not (target and source):
            continue

        parent = deepcopy(target)
        child = deepcopy(source)

        parent["related_as"] = rel.get("relationship_type")
        child["related_obj"] = parent
        associations.append(enrich_indicator(child, logger))

    # --- reports ---
    report_objs = [r for r in records if r.get("type") == "report"]
    for report in report_objs:
        refs = report.get("object_refs")
        if not refs:
            associations.append(report)
            continue

        child_objs = [lookup.get(cid) for cid in refs if cid in lookup]
        if not child_objs:
            associations.append(report)
            continue

        ref_objs = [
            enrich_indicator(deepcopy(obj), logger) for obj in child_objs if obj
        ]
        report["ref_objects"] = ref_objs
        associations.append(report)

    return associations


def pull_feeds(
    client, feed_name: str, from_date: str, logger: Logger
) -> List[Dict[str, Any]]:
    """
    Pull feeds from Luminar API, filter them, and create associations.
    """
    logger.info("Trigger will fetch records created after %s", from_date)
    logger.info("Fetching %s feeds...", feed_name)
    collection_id = client.get_taxi_collections().get(feed_name)
    if not collection_id:
        logger.error("No collection ID found for alias %s", feed_name)
        return []

    params = {"limit": 9999, "added_after": from_date}
    records = client.get_collection_objects(collection_id, params)

    if not records:
        logger.info("No new %s records found", feed_name)
        return []
    filtered = filtered_records(records, from_date, logger)
    return create_associations(filtered, logger)


def build_base_url(url: str) -> str:
    """Ensure API base URL has no trailing slash and is prefixed with https://."""
    return f"https://{url.rstrip('/')}"
