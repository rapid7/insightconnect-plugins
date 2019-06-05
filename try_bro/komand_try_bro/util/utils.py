import komand
import base64
import hashlib
import requests


def load_scripts(scripts, log):
    # main.bro is required first file name
    # main.bro gets renamed to trybro.bro server side'''
    sources=[]
    # Remove empty strings and None types so count is correct
    scripts = komand.helper.clean_list(scripts)
    script_count = len(scripts)
    log.info('LoadScripts: %i scripts found', script_count)
    if script_count != 0:
      for index, i in enumerate(scripts):
        script  = base64.b64decode(i)
        if index == 0:
          name = 'main.bro'
        else:
          name = i[0] + str(len(script)) + '.bro'
        sources.append({ 'name': name, 'content': script })
    else:
      # Default to loading local.bro if no scripts provided
      log.info('LoadScripts: No scripts supplied, defaulting to local.bro')
      sources=[ { 'name': 'main.bro', 'content': '@load local.bro' } ]
    return sources

def md5(s):
    m = hashlib.md5()
    m.update(s)
    return m.hexdigest()

def maybe_upload_pcap(server, pcap, log):
    checksum = md5(pcap)
    log.info('MaybeUploadPcap: Checking for existing PCAP')
    is_exists = requests.get(server + "/pcap/" + checksum).json()["status"]
    if not is_exists:
        files = { 'pcap': ('file.pcap', pcap) }
        log.info('MaybeUploadPcap: Uploading PCAP')
        status = requests.post(server + "/pcap/upload/" + checksum, files=files).json()['status']
        assert status
    else:
      log.info('MaybeUploadPcap: PCAP already exists, not uploading')

    return checksum
