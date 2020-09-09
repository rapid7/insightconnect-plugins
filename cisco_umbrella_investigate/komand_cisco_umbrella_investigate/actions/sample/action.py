import komand
from .schema import SampleInput, SampleOutput
# Custom imports below
from komand.exceptions import PluginException


class Sample(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='sample',
                description='Return a file, or a file-like object, such as a process running in memory',
                input=SampleInput(),
                output=SampleOutput())

    def run(self, params={}):
        hash = params.get('hash')
        limit = params.get('limit', None)
        offset = params.get('offset', None)
        
        if not limit or limit == 0:
            limit = 10
        
        if not offset:
            offset = 0

        try:
            sample = self.connection.investigate.sample(hash, limit=limit, offset=offset)
        except Exception as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=e)

        return sample

    def test(self):
        return {"threatScore": 100, "md5": "6d8b70d20b1182546bc58ce7f90549d7", "size": 228864, "sha1": "00bf659061121200c1e5469fbe31d100418b149e", "magicType": "PE32 executable (GUI) Intel 80386 (stripped to external PDB), for MS Windows", "lastSeen": 1460762759000, "sha256": "414e38ed0b5d507734361c2ba94f734252ca33b8259ca32334f32c4dba69b01c", "visible": True, "avresults": [], "samples": {"totalResults": 0, "limit": 10, "offset": 0, "samples": [], "moreDataAvailable": False}, "connections": {"totalResults": 10, "limit": 10, "offset": 0, "connections": [], "moreDataAvailable": True}, "firstSeen": 1460762759000, "behaviors": [{"tags": ["executable", "file", "process"], "severity": 90, "hits": 1, "title": "Process Modified a File in a System Directory", "category": ["file"], "threat": 90, "name": "modified-file-in-system-dir", "confidence": 100}, {"tags": ["network", "http", "nginx"], "severity": 25, "hits": 6, "title": "Outbound Communications to Nginx Web Server", "category": ["network"], "threat": 6, "name": "nginx-webserver-detected", "confidence": 25}, {"tags": ["process", "registry", "system"], "severity": 90, "hits": 124, "title": "Process Deleted SafeBoot Registry Key", "category": ["weakening"], "threat": 81, "name": "safeboot-registry-key-deleted", "confidence": 90}, {"tags": ["autorun", "file", "process"], "severity": 100, "hits": 1, "title": "Process Enabled Autorun through the Creation of autorun.inf", "category": ["persistence", "file"], "threat": 100, "name": "drive-autoplay-modification", "confidence": 100}, {"tags": ["process", "registry", "system"], "severity": 90, "hits": 1, "title": "Process Deleted SafeBoot Registry Key Value", "category": ["weakening"], "threat": 81, "name": "safeboot-registry-key-value-deleted", "confidence": 90}, {"tags": ["executable", "file", "process", "PE"], "severity": 60, "hits": 5, "title": "Process Created an Executable in a User Directory", "category": ["file"], "threat": 57, "name": "created-executable-in-user-dir", "confidence": 95}, {"tags": ["file", "dropper"], "severity": 30, "hits": 3, "title": "File Downloaded to Disk", "category": ["network"], "threat": 27, "name": "network-file-downloaded-to-disk", "confidence": 90}, {"tags": ["registry", "process"], "severity": 50, "hits": 1, "title": "Process Added a Service to the ControlSet Registry Key", "category": ["persistence"], "threat": 25, "name": "currentcontrolset-service-added", "confidence": 50}, {"tags": ["suspicious", "threshold"], "severity": 90, "hits": 1, "title": "Excessive Suspicious Activity Detected", "category": ["compound"], "threat": 90, "name": "excessive-suspicious-activity", "confidence": 100}, {"tags": ["memory"], "severity": 50, "hits": 1, "title": "Potential Code Injection Detected", "category": ["evasion"], "threat": 25, "name": "memory-execute-readwrite", "confidence": 50}, {"tags": ["trojan", "host", "process", "lock", "mutex", "RAT"], "severity": 100, "hits": 2, "title": "Sality Default Mutex Detected", "category": ["malware"], "threat": 100, "name": "malware-sality-mutex", "confidence": 100}, {"tags": ["executable", "file", "process", "PE"], "severity": 60, "hits": 8, "title": "Process Modified an Executable File", "category": ["file", "persistence"], "threat": 60, "name": "modified-executable", "confidence": 100}, {"tags": ["executable", "file", "process"], "severity": 70, "hits": 7, "title": "Process Modified File in a User Directory", "category": ["file"], "threat": 56, "name": "modified-file-in-user-dir", "confidence": 80}, {"tags": ["dns", "sinkhole", "botnet", "localhost", "parking", "loopback"], "severity": 25, "hits": 1, "title": "Domain Resolves to Localhost", "category": ["network"], "threat": 6, "name": "localhost-ipaddress-detected", "confidence": 25}, {"tags": ["file", "attributes", "anomaly"], "severity": 40, "hits": 6, "title": "PE Has Sections Marked Executable and Writable", "category": ["attribute"], "threat": 24, "name": "pe-section-execute-writable", "confidence": 60}, {"tags": ["communications", "command and control"], "severity": 25, "hits": 9, "title": "RAT Queried Domain", "category": ["network"], "threat": 6, "name": "feed-domain-rat", "confidence": 25}, {"tags": ["network", "http", "get"], "severity": 75, "hits": 9, "title": "Outbound HTTP GET Request", "category": ["network"], "threat": 56, "name": "network-communications-http-get", "confidence": 75}, {"tags": ["packer", "crypter", "encoding", "PE"], "severity": 30, "hits": 6, "title": "Executable with Encrypted Sections", "category": ["forensics"], "threat": 9, "name": "pe-encrypted-section", "confidence": 30}, {"tags": ["process", "registry"], "severity": 60, "hits": 8, "title": "Process Disables Security Center Notifications", "category": ["weakening"], "threat": 54, "name": "disables-security-center-notifications", "confidence": 90}, {"tags": ["communication"], "severity": 25, "hits": 2, "title": "DNS Query Returned Non-Existent Domain", "category": ["network"], "threat": 18, "name": "dns-query-nxdomain", "confidence": 75}, {"tags": ["network", "ttl", "dns", "fast flux", "command and control"], "severity": 35, "hits": 18, "title": "DNS Response Contains Low Time to Live (TTL) Value", "category": ["network"], "threat": 7, "name": "network-fast-flux-domain", "confidence": 20}, {"tags": ["file"], "severity": 80, "hits": 4, "title": "Artifact Flagged by Antivirus", "category": ["forensics"], "threat": 64, "name": "antivirus-flagged-artifact", "confidence": 80}, {"tags": ["trojan", "RAT"], "severity": 100, "hits": 2, "title": "Artifact Flagged as Known Trojan by Antivirus", "category": ["malware"], "threat": 95, "name": "malware-known-trojan-av", "confidence": 95}]}
