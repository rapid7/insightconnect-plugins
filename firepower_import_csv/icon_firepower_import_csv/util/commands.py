from bs4 import BeautifulSoup
import random

SetSource = 'SetSource,{source_id}\n'
AddHost = 'AddHost,{address}\n'
SetOS = 'SetOS,{address},{vendor},{name},{version}\n'
AddResult = 'AddScanResult,{ip_addr},"{scanner_id}",{vuln_id},{port},' \
            '{protocol_id},"{vuln_title}","{description}","cve_ids: {' \
            'cve_ids}","bugtraq_ids: {bugtraq_ids}"\n '
Unknown = '-1'


def generate_add_host_command(ip):
    return AddHost.format(address=ip)


def generate_set_os_command(host_dict, ip):
    os = host_dict.get('operating_system', {})
    name = os.get('name') if os.get('name') else ''
    vendor = os.get('vendor') if os.get('vendor') else ''
    version = os.get('version') if os.get('version') else ''
    return SetOS.format(
        name=name, vendor=vendor,
        version=version, address=ip
    )


def generate_set_source_command(source_id):
    return SetSource.format(source_id=source_id)


def generate_add_result_command(details, ip):
    # These are written like this because it's possible for the incoming object to have a value like this
    # descripiton: None
    # In that case get will return None, which Firepower chokes on

    scanner_id = details.get('scanner_id', '') if details.get('scanner_id', '') else ''
    vuln_id = details.get('vulnerability_id', '') if details.get('vulnerability_id', '') else ''
    port = details.get('port', '')
    port = '' if (not port or port == Unknown) else port
    protocol_id = details.get('protocol_id', '')
    protocol_id = '' if (not protocol_id or protocol_id == Unknown) else protocol_id
    description = details.get('description', '') if details.get('description', '') else ''
    vuln_title = details.get('vulnerability_title', '') if details.get('vulnerability_title', '') else ''
    cve_ids = details.get('cve_ids', '').replace(':',' ') if details.get('cve_ids', '') else ''
    bugtraq_ids = details.get('bugtraq_ids', '') if details.get('bugtraq_ids', '') else ''

    return AddResult.format(
        ip_addr=ip,
        scanner_id=scanner_id,
        vuln_id=vuln_id,
        port=port,
        protocol_id=protocol_id,
        description=description,
        vuln_title=vuln_title,
        cve_ids=cve_ids,
        bugtraq_ids=bugtraq_ids
    )

