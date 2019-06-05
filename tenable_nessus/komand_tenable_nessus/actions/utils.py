import requests
import logging


def get_scanner_by_name(scanner, conn):
    conn['url'] += '/scanners'
    r = requests.get(**conn)
    scanners = r.json()['scanners']
    for s in scanners:
        if s['name'] == scanner:
            return str(s['id'])
    raise Exception('Requested scanner not found. Please check capitalization')

def get_scan_by_name(scan, conn):
    conn['url'] += '/scans'
    r = requests.get(**conn)
    scans = r.json()['scans']
    for s in scans:
        if s['name'] == scan:
            return str(s['id'])
    raise Exception('Requested scan not found. Please check capitalization')

def get_template_by_name(template, conn):
    conn['url'] += '/editor/scan/templates'
    r = requests.get(**conn)
    templates = r.json()['templates']
    for t in templates:
        if t['title'] == template:
            return t['uuid']
    raise Exception('Requested template not found. Please check capitalization')

def check_scan_status(scan, conn):
    conn['url'] += '/scans'
    r = requests.get(**conn)
    scans = r.json()['scans']
    for s in scans:
        if s['name'] == scan:
            return s['status']
    raise Exception('Requested scan not found. Please check capitalization')

def folder_check(conn):
    try:
        conn['url'] += '/folders'
        r = requests.get(**conn)
        if r.status_code == 200:
            return 'Connection successful'
        raise
    except Exception as e:
        logging.error('Could not authenticate. Error: ' + str(e))
        raise
