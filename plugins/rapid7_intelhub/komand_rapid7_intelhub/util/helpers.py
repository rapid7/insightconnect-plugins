import re
from typing import Any, Dict

from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean

# Matches a CVE ID on its own or inside a Rapid7 vulnerability ID, such as apple-itunes-cve-2019-8835
CVE_ID_PATTERN = re.compile(r"(?<![a-z0-9])cve-(\d{4})-(\d{4,})(?![0-9])", re.IGNORECASE)

CVE_FIELDS = [
    "cve_id",
    "title",
    "published_date",
    "modified_date",
    "cvss_v3_base_score",
    "cvss_v3_severity",
    "cvss_v3_vector",
    "cvss_v4_base_score",
    "cvss_v4_severity",
    "cvss_v4_vector",
    "epss_score",
    "epss_percentile",
    "active_risk_score",
    "exploitable",
    "exploited_in_the_wild",
    "cisa_kev",
    "campaign_count",
    "threat_actor_count",
    "references",
]
SEVERITY_FIELDS = ["cvss_v3_severity", "cvss_v4_severity"]


def extract_cve_id(identifier: str) -> str:
    # Intelligence Hub looks CVEs up by the upper-case CVE ID only
    match = CVE_ID_PATTERN.search(identifier.strip())
    if not match:
        raise PluginException(
            cause=f"'{identifier}' does not contain a CVE ID.",
            assistance="Provide a CVE ID, such as CVE-2024-3400, or a Rapid7 vulnerability ID that contains one, "
            "such as apple-itunes-cve-2019-8835.",
        )
    return f"CVE-{match.group(1)}-{match.group(2)}"


def map_cve(cve_profile: Dict[str, Any]) -> Dict[str, Any]:
    cve = {field: cve_profile.get(field) for field in CVE_FIELDS}

    # The same severity comes back as "HIGH" or "High" depending on the source of the CVE record
    for field in SEVERITY_FIELDS:
        if cve.get(field):
            cve[field] = cve[field].capitalize()

    # Description and tags exist only for CVEs that have Rapid7 vulnerability content
    rapid7_content = cve_profile.get("ivm_cve_data")
    if isinstance(rapid7_content, dict):
        cve["description"] = rapid7_content.get("description")
        cve["tags"] = rapid7_content.get("tags")
    return clean(cve)
