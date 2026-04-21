import io
import re
import csv
import json
import base64

from typing import Union
from datetime import datetime

from insightconnect_plugin_runtime.exceptions import PluginException


HASH_REGEX = {
    "md5": re.compile(r"^[a-fA-F0-9]{32}$"),
    "sha1": re.compile(r"^[a-fA-F0-9]{40}$"),
    "sha256": re.compile(r"^[a-fA-F0-9]{64}$"),
}


def prepare_file_payload(
    analysis_uuid: str, report_format: str, payload: Union[dict, list[dict], bytes]
) -> dict[str, bytes]:
    if report_format in ("json", "stix"):
        filename = get_report_name(analysis_uuid, "json")
        content = base64.b64encode(json.dumps(payload).encode()).decode()
    elif report_format == "html":
        filename = get_report_name(analysis_uuid, "html")
        content = base64.b64encode(payload.encode()).decode()

    return {"filename": filename, "content": content}


def prepare_csv_payload(analysis_uuid: str, iocs: list[dict]) -> dict[str, bytes]:
    iocs_csv = list()
    iocs_csv.append(["category", "type", "name", "ioc", "reputation", "discoveringEntryId"])

    for ioc in iocs:
        iocs_csv.append(
            [
                ioc.get("category", ""),
                ioc.get("type", ""),
                ioc.get("name", "No info"),
                ioc.get("ioc", ""),
                {1: "Suspicious", 2: "Malicious"}.get(ioc.get("reputation"), 2),
                ioc.get("discoveringEntryId"),
            ]
        )

    string_buffer = io.StringIO()
    csv_writer = csv.writer(string_buffer, delimiter=",", quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerows(iocs_csv)
    csv_string = string_buffer.getvalue()
    string_buffer.close()

    return {
        "filename": get_report_name(analysis_uuid, "csv"),
        "content": base64.b64encode(csv_string.encode()).decode(),
    }


def get_report_name(analysis_uuid: str, extension: str) -> str:
    return f"ANYRUN_REPORT_{analysis_uuid}_{datetime.now().strftime(f'%Y-%m-%d_%H-%M-%S')}" + f".{extension}"


def check_hash_type(entity_value: str) -> str:
    hash_type = None
    for htype, pattern in HASH_REGEX.items():
        if pattern.match(entity_value):
            hash_type = htype
            break

    if not hash_type:
        raise PluginException("Unsupported hash type. Allowed: SHA1, SHA256, MD5")

    return hash_type
