import re
from logging import Logger

from insightconnect_plugin_runtime.exceptions import PluginException
from requests import RequestException

# A journal field read with sysparm_display_value=true holds every entry of that field in one string,
# each a header line - '2019-09-26 21:19:11 - System Administrator (Work notes)' - followed by its text,
# which may itself contain blank lines. The timestamp honours the caller's date format and time zone and
# the label is the field's own label, so headers are matched by shape rather than against a fixed format,
# with every repetition bounded to keep matching linear on the pasted logs that end up in comments.
journal_entry_header = re.compile(
    r"^(?P<sys_created_on>\d.{1,39}?\d{1,2}:\d{2}.{0,15}?) - (?P<sys_created_by>.{1,200}) \(.{1,120}\)[ \t]*$"
)


def read_journal_from_incident(connection, logger: Logger, system_id: str, entry_type: str) -> list:
    """
    Reads comments and work notes from an incident record rather than from the sys_journal_field
    table. The incident record is gated by the incident's own Access Controls, so this succeeds
    for accounts that cannot read the journal table directly. Returns no entries instead of
    raising when the incident cannot be read, so that a failed attempt to do better never turns
    a successful journal query into an error.

    :param connection: Connection object of the running action
    :param logger: Logger object of the running action
    :type logger: Logger
    :param system_id: System ID of the incident to read comments and work notes from
    :type system_id: str
    :param entry_type: Either 'all', 'comments' or 'work_notes'
    :type entry_type: str
    :return: List of comment and work note objects
    :rtype: list
    """
    if not (system_id or "").isalnum():
        logger.info(f"'{system_id}' is not a system ID, the incident record will not be read")
        return []

    elements = ["comments", "work_notes"] if entry_type == "all" else [entry_type]
    logger.info(
        f"No journal entries were returned for incident {system_id}, reading the comments and "
        "work notes from the incident record instead"
    )

    try:
        response = connection.request.make_request(
            f"{connection.incident_url}/{system_id}",
            "get",
            params={"sysparm_fields": ",".join(elements), "sysparm_display_value": "true"},
        )
    except (PluginException, RequestException) as error:
        logger.warning(
            f"Unable to read incident {system_id}, returning no comments or work notes. The connected "
            "account needs read access either to the incident and its journal fields or to the "
            f"sys_journal_field table. {error}"
        )
        return []

    resource = response.get("resource")
    incident = resource.get("result") if isinstance(resource, dict) else None

    if not isinstance(incident, dict):
        logger.warning(f"Incident {system_id} was not returned in the expected format, returning no entries")
        return []

    entries = []
    for element in elements:
        if element not in incident:
            # A field the caller cannot read is left out of the record rather than returned empty.
            logger.info(f"The incident {system_id} record held no {element} field, none will be returned")
        entries.extend(parse_journal_display_value(incident.get(element), element, system_id))

    if entries:
        logger.warning(
            f"Read {len(entries)} comment and work note entries from the incident {system_id} record "
            "because the sys_journal_field table returned none. The connected account is most likely "
            "unable to read that table, so `sys_id` and `sys_tags` are empty for these entries - grant "
            "it read access to sys_journal_field for complete entries"
        )

    return entries


def parse_journal_display_value(display_value, element: str, element_id: str) -> list:
    """
    Parses the display value of a journal field into the objects returned when the
    sys_journal_field table is queried directly. Header metadata is best effort: a line is read
    as a header only when it opens with a date holding a clock and ends with the parenthesised
    field label, so a date format beginning with the month name is not recognised. Text whose
    header is not recognised keeps its value and is returned with an empty creation date and
    author rather than being discarded.

    :param display_value: Journal field as returned with sysparm_display_value=true
    :param element: Journal field the display value was read from
    :type element: str
    :param element_id: System ID of the incident the display value was read from
    :type element_id: str
    :return: List of comment and work note objects
    :rtype: list
    """
    if not isinstance(display_value, str):
        return []

    entries = []
    for line in display_value.splitlines():
        header = journal_entry_header.match(line)
        if header:
            # The author is the user's display name rather than the user name held in
            # sys_journal_field, and a user with no last name is displayed with a trailing space.
            metadata = {key: value.strip() for key, value in header.groupdict().items()}
            entries.append({**metadata, "header": line, "lines": []})
        elif entries:
            entries[-1]["lines"].append(line)
        else:
            entries.append({"lines": [line]})

    parsed_entries = []
    for entry in entries:
        # A header with no text under it is not an entry, it is entry text that reads like a header,
        # so the line is returned as text of its own rather than being dropped along with the entry.
        text = "\n".join(entry.get("lines")).strip()
        metadata = entry if text else {}
        value = text or entry.get("header", "")
        if not value:
            continue
        parsed_entries.append(
            {
                "sys_id": "",
                "sys_created_on": metadata.get("sys_created_on", ""),
                "name": "incident",
                "element_id": element_id,
                "sys_tags": "",
                "value": value,
                "sys_created_by": metadata.get("sys_created_by", ""),
                "element": element,
            }
        )

    return parsed_entries
