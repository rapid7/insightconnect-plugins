SetSource = "SetSource,{source_id}\n"
AddHost = "AddHost,{address}\n"
SetOS = "SetOS,{address},{vendor},{name},{version}\n"
AddResult = (
    'AddScanResult,{ip_addr},"{scanner_id}",{vuln_id},{port},'
    '{protocol_id},"{vuln_title}","{description}","cve_ids: {'
    'cve_ids}","bugtraq_ids: {bugtraq_ids}"\n '
)
Unknown = "-1"


def generate_add_host_command(ip):
    return AddHost.format(address=ip)


def generate_set_os_command(host_dict, ip):
    os = host_dict.get("operating_system", {})
    return SetOS.format(name=os.get("name"), vendor=os.get("vendor"), version=os.get("version"), address=ip)


def generate_set_source_command(source_id):
    return SetSource.format(source_id=source_id)


def generate_add_result_command(details, ip):
    port = details.get("port", "")
    port = "" if port == Unknown else port
    protocol_id = details.get("protocol_id", "")
    protocol_id = "" if protocol_id == Unknown else protocol_id
    return AddResult.format(
        ip_addr=ip,
        scanner_id=details.get("scanner_id", ""),
        vuln_id=details.get("vulnerability_id", ""),
        port=port,
        protocol_id=protocol_id,
        description=details.get("description", ""),
        vuln_title=details.get("vulnerability_title", ""),
        cve_ids=details.get("cve_ids", ""),
        bugtraq_ids=details.get("bugtraq_ids", ""),
    )
