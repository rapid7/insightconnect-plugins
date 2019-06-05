import argparse
import json
from random import randint


parser = argparse.ArgumentParser(
    __file__, description="Scan Result Generator"
)

parser.add_argument(
    "--results", "-r", default="10", help="The number of results to generate"
)


def gen_source():
    x = {}
    x['scanner_id'] = "ProductXReport"
    x['source_id'] = "ProductX"
    y = {}
    y['scanner_id'] = "ProductYScanReport"
    y['source_id'] = "ProductY"
    z = {}
    z['scanner_id'] = "ProductZImport"
    z['source_id'] = "ProductZ"
    return [x, y, z]


def gen_os():
    ubuntu = {}
    ubuntu['version'] = "16.04"
    ubuntu['vendor'] = "Canonical"
    ubuntu['name'] = "Ubuntu"
    mac = {}
    mac['version'] = "High Sierra"
    mac['vendor'] = "Apple"
    mac['name'] = "MacOS"
    windows = {}
    windows['version'] = "Unknown"
    windows['vendor'] = "Microsoft"
    windows['name'] = "Windows Server 2012"
    return [ubuntu, mac, windows]


def gen_vuln_title(index):
    words = [
        "Heart", "Bleed", "Poodle", "Java", "Python", "SSH", "Hack", "Fake",
        "Gox", "Net", "Shock", "Wanna", "Overflow", "Scam", "SSL", "Breach",
        "Worm", "Phish", "PDF", "Chrome", "Struct", "Wire", "Lucker", "Virus"
    ]
    first = randint(0, len(words)-1)
    second = randint(0, len(words)-1)
    return "%s %s %s" % (words[first], words[second], index)


def gen_single_scan_result(os, source, sentence, index):
    scan_result = {}
    scan_result['host'] = {}
    gen_bugtraq_ids = randint(0, 1)
    vuln_id = randint(1, 999999)
    include_protocol_id = randint(0, 1)
    include_port = randint(0, 1)
    include_description = randint(0, 1)

    ip = randint(1, 255)
    scan_result['host']['ip_address'] = "0.0.0.%s" % (ip)

    scan_result['host']['operating_system'] = os

    scan_result_details = source.copy()
    scan_result_details['vulnerability_id'] = str(vuln_id)

    if include_protocol_id:
        scan_result_details['protocol_id'] = "6"
    if include_port:
        scan_result_details['port'] = str(randint(1, 65535))

    if include_description:
        description = ""
        for i in range(randint(1, 2)):
            description += sentence
        scan_result_details['description'] = description

    scan_result_details['vulnerability_title'] = gen_vuln_title(index)

    if gen_bugtraq_ids:
        bugtraqs = []
        cves = []
        for i in range(randint(1, 10)):
            bugtraqs.append(str(randint(1, 999999)))
            cve = "CVE-2049-%s" % randint(1000, 9999)
            cves.append(cve)
        scan_result_details['bugtraq_ids'] = bugtraqs
        scan_result_details['cve_ids'] = cves

    scan_result['scan_result_details'] = scan_result_details
    return scan_result


args = parser.parse_args()
OS = gen_os()
SOURCE = gen_source()
SENTENCE = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec et."

scan_results = []
print("Generating scan results...")
for i in range(int(args.results)):
    os_index = randint(0, len(OS)-1)
    source_index = randint(0, len(SOURCE)-1)
    result = gen_single_scan_result(
        OS[os_index], SOURCE[source_index], SENTENCE, i
    )
    scan_results.append(result)

test_json = {}
test_json['body'] = {}
test_json['body']['input'] = {}
test_json['body']['input']['scan_results'] = scan_results
test_json['body']['input']['operation'] = "ScanFlush"

f = open('scan_results.json', 'w')
f.write(json.dumps(test_json, indent=2, sort_keys=True))
f.close()

print("Test JSON generated.")
