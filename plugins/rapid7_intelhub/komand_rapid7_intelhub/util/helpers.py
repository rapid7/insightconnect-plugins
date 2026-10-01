from typing import Any, Dict

from insightconnect_plugin_runtime.helper import clean

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
