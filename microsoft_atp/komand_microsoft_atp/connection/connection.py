import komand
import json
import requests
import maya
from .schema import ConnectionSchema
from komand.exceptions import ConnectionTestException


# Custom imports below


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.start_from_payload = {"sinceTimeUtc": "2010-01-01T00:00:00.000"}
        self.api_version = "/api"
        self.alert_endpoint = "/Alerts"
        self.machine_endpoint = "/machines"
        self.session = requests.Session()
        self.seconds_ago = 0
        self.current_time = maya.now()
        self.host_url = ""
        self.auth_url = ""
        self.client_id = ""
        self.client_secret = ""
        self.resource_url = "https://api.securitycenter.windows.com"

    def connect(self, params):
        self.logger.info("Connecting...")

        self.seconds_ago = params.get("seconds_ago", 0)
        self.current_time = maya.now().add(seconds=-int(self.seconds_ago))

        self.host_url = params.get("host")

        self.auth_url = params.get("auth_url")
        self.client_id = params.get("client_id")
        self.client_secret = params.get("client_secret")

        self.resource_url = params.get("resource_url")

        self.logger.info("Setup Complete")

    def update_access_token(self):
        self.logger.info("Updating Access Token...")
        o_auth_token = self.get_access_token(self.auth_url, self.client_id, self.client_secret)

        session_headers = {
            'Authorization': 'Bearer {}'.format(o_auth_token),
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        self.session.headers.update(session_headers)

    def get_access_token(self, auth_url, client_id, client_secret):
        payload = {"resource": self.resource_url,
                   "client_id": client_id,
                   "client_secret": client_secret,
                   "grant_type": "client_credentials"}

        response = requests.post(auth_url, payload)
        self.raise_exception_on_token_error(response)
        token = json.loads(response.text)["access_token"]
        return token

    def get_all_alerts(self):
        self.update_access_token()
        self.update_time_from()

        full_endpoint_url = self.setup_alerts_endpoint()
        self.logger.info("Connecting to: " + full_endpoint_url)

        response = self.session.get(full_endpoint_url)

        return komand.helper.clean(response.json())

    def get_alerts_by_key_value(self, key, value):
        self.update_access_token()
        self.update_time_from()

        full_endpoint_url = self.setup_alerts_endpoint()
        self.logger.info("Connecting to: " + full_endpoint_url)

        response = self.session.get(full_endpoint_url)
        self.raise_exception_on_error(response)

        matching_alerts = []

        self.logger.info("Looking for {} matching {}".format(value, key))

        try:
            matching_alerts = list(filter(lambda a: a.get(key) == value, response.json()))
        except json.JSONDecodeError as e:
            self.logger.error("Alerts returned were in an unexpected format!")
            raise e

        return komand.helper.clean(matching_alerts)

    def get_machines_from_alert_id(self, id):
        self.update_access_token()
        alert_machine_id_endpoint = self.setup_get_machines_endpoint(id)

        try:
            machines = self.session.get(alert_machine_id_endpoint)
        except Exception as e:
            raise ConnectionTestException(cause="Connection error occurred while connecting to: {0}. Error "
                                                "was: {1}".format(alert_machine_id_endpoint, str(e)),
                                          assistance="Check connection settings for proper resource URL and host "
                                                     "server. Verify application has Machine.Read.All permissions "
                                                     "in the Azure portal."
                                          )

        return machines.json()

    def get_files_from_alert_id(self, id):
        self.update_access_token()
        file_id_endpoint = self.setup_get_files_endpoint(id)

        try:
            files = self.session.get(file_id_endpoint)
        except Exception as e:
            raise ConnectionTestException(cause="Connection error occurred while connecting to: {0}. Error "
                                                "was: {1}".format(file_id_endpoint, str(e)),
                                          assistance="Check connection settings for proper resource URL and host "
                                                     "server. Verify application has Machine.Read.All permissions "
                                                     "in the Azure portal."
                                          )

        return files.json()

    def isolate_machine(self, id, isolation_type, comment):
        self.update_access_token()
        machine_isolate_endpoint = self.setup_machine_isolate_endpoint(id)
        body = {
            "Comment": comment,
            "IsolationType": isolation_type
        }

        try:
            response = self.session.post(machine_isolate_endpoint, json.dumps(body))
        except Exception as e:
            raise ConnectionTestException(cause="Connection error occurred while connecting to: {0}. Error "
                                                "was: {1}".format(machine_isolate_endpoint, str(e)),
                                          assistance="Check connection settings for proper resource URL and host "
                                                     "server. Verify application has Machine.Isolate permissions "
                                                     "in the Azure portal."
                                          )
        return response.json()

    def unisolate_machine(self, id, comment):
        self.update_access_token()
        machine_isolate_endpoint = self.setup_machine_unisolate_endpoint(id)
        body = {
            "Comment": comment
        }

        try:
            response = self.session.post(machine_isolate_endpoint, json.dumps(body))
        except Exception as e:
            raise ConnectionTestException(cause="Connection error occurred while connecting to: {0}. Error "
                                                "was: {1}".format(machine_isolate_endpoint, str(e)),
                                          assistance="Check connection settings for proper resource URL and host "
                                                     "server. Verify application has Machine.Isolate permissions "
                                                     "in the Azure portal."
                                          )
        return response.json()

    def stop_and_quarantine_file(self, machine_id, sha1_id, comment):
        self.update_access_token()
        quarantine_endpoint = self.setup_stop_and_quarantine_endpoint(machine_id)
        body = {
            "Comment": comment,
            "Sha1": sha1_id
        }

        try:
            response = self.session.post(quarantine_endpoint, json.dumps(body))
        except Exception as e:
            raise ConnectionTestException(cause="Connection error occurred while connecting to: {0}. Error "
                                                "was: {1}".format(quarantine_endpoint, str(e)),
                                          assistance="Check connection settings for proper resource URL and host "
                                                     "server. Verify application has Machine.Isolate permissions "
                                                     "in the Azure portal."
                                          )
        return response.json()

    def run_antivirus_scan(self, machine_id, scan_type, comment):
        self.update_access_token()
        antivirus_endpoint = self.setup_antivirus_endpoint(machine_id)
        body = {
            "Comment": comment,
            "ScanType": scan_type
        }

        try:
            response = self.session.post(antivirus_endpoint, json.dumps(body))
        except Exception as e:
            raise ConnectionTestException(cause="Connection error occurred while connecting to: {0}. Error "
                                                "was: {1}".format(antivirus_endpoint, str(e)),
                                          assistance="Check connection settings for proper resource URL and host "
                                                     "server. Verify application has Machine.Isolate permissions "
                                                     "in the Azure portal."
                                          )
        return response.json()

    def get_machine_action(self, action_id):
        self.update_access_token()
        machine_action_endpoint = self.setup_machine_action_endpoint(action_id)

        try:
            response = self.session.get(machine_action_endpoint)
        except Exception as e:
            raise ConnectionTestException(cause="Connection error occurred while connecting to: {0}. Error "
                                                "was: {1}".format(machine_action_endpoint, str(e)),
                                          assistance="Check connection settings for proper resource URL and host "
                                                     "server. Verify application has Machine.Isolate permissions "
                                                     "in the Azure portal."
                                          )
        return response.json()

    def setup_machine_action_endpoint(self, action_id):
        endpoint_url = self.host_url + "/api/machineactions/" + action_id
        return endpoint_url

    def setup_antivirus_endpoint(self, machine_id):
        endpoint_url = self.host_url + "/api/machines/" + machine_id + "/runAntiVirusScan"
        return endpoint_url

    def setup_stop_and_quarantine_endpoint(self, machine_id):
        endpoint_url = self.host_url + "/api/machines/" + machine_id + "/StopAndQuarantineFile"
        return endpoint_url

    def setup_get_machines_endpoint(self, id):
        endpoint_url = self.host_url + "/api/alerts/" + id + "/machine"
        return endpoint_url

    def setup_get_files_endpoint(self, id):
        endpoint_url = self.host_url + "/api/alerts/" + id + "/files"
        return endpoint_url

    def setup_machine_isolate_endpoint(self, id):
        endpoint_url = self.host_url + "/api/machines/" + id + "/isolate"
        return endpoint_url

    def setup_machine_unisolate_endpoint(self, id):
        endpoint_url = self.host_url + "/api/machines/" + id + "/unisolate"
        return endpoint_url

    def setup_alerts_endpoint(self):
        endpoint_url = self.host_url + \
                       self.api_version + \
                       self.alert_endpoint

        return endpoint_url

    def update_time_from(self):
        self.start_from_payload = {"sinceTimeUtc": self.current_time.rfc3339()}
        self.current_time = maya.now()
        self.session.params = self.start_from_payload

    def test(self):
        self.update_access_token()
        self.update_time_from()
        endpoint_formatted = self.setup_alerts_endpoint()
        response = self.session.get(endpoint_formatted)
        return self.raise_exception_on_error(response)

    def raise_exception_on_error(self, response):
        if response.status_code == 200:
            return True
        elif response.status_code == 401:
            raise ConnectionTestException(cause="Unable to authorize against ATP metrics server.",
                                          assistance="The application may not be authorized to connect "
                                                     "to the ATP metrics server. Please contact your Azure or ATP administrator.")
        elif response.status_code == 404:
            raise ConnectionTestException(cause="Unable to reach ATP host server at: %s." % self.host_url + ".",
                                          assistance="Verify the ATP metrics server at the URL configured in your plugin "
                                                     "connection is correct.")
        else:
            self.logger.error(ConnectionTestException(cause="Unhandled error occurred: %s" % response.content))

    def raise_exception_on_token_error(self, response):
        if response.status_code == 200:
            return True
        elif response.status_code == 401:
            raise ConnectionTestException(cause="Unable to authorize against ATP authorization server.",
                                          assistance="The application may not be authorized to connect "
                                                     "to the ATP authorization server. Please contact your Azure or ATP administrator.")
        elif response.status_code == 404:
            raise ConnectionTestException(
                cause="Unable to reach ATP authorization server at: %s." % self.auth_url + ".",
                assistance="Verify the ATP authorization server is correctly configured.")
        else:
            self.logger.error(ConnectionTestException(cause="Unhandled error occurred: %s" % response.content))

    # Create a fake payload, convert it to json, and return
    def fake_alert(self):
        fake_payload = """
        [{
          "AlertTime": "2018-11-09T03:43:11.7194799Z",
          "ComputerDnsName": "w10-for-atp",
          "AlertTitle": "Sensitive information lookup",
          "Category": "LateralMovement",
          "Severity": "Medium",
          "AlertId": "636772341913498370_1532439962",
          "Actor": "",
          "LinkToWDATP": "https://securitycenter.windows.com/alert/636772341913498370_1532439962",
          "IocName": "",
          "IocValue": "",
          "CreatorIocName": "",
          "CreatorIocValue": "",
          "Sha1": "04ce0b79ea20332cc4ff4679883b18bfe4341fbd",
          "FileName": "reg.exe",
          "FilePath": "C:\\\\Windows\\\\System32",
          "IpAddress": "",
          "Url": "",
          "IoaDefinitionId": "4a89c39f-47b5-4ad6-8b48-7d1b0afd9493",
          "UserName": "",
          "AlertPart": 0,
          "FullId": "636772341913498370_1532439962:b1agHW5IpUdZpf6_KstT3dNo0dffOAx_5Sbs4tN4CUU=",
          "LastProcessedTimeUtc": "2018-11-12T16:32:51.0700622Z",
          "ThreatCategory": "",
          "ThreatFamily": "",
          "ThreatName": "",
          "RemediationAction": "",
          "RemediationIsSuccess": null,
          "Source": "EDR",
          "Md5": "e3dacf0b31841fa02064b4457d44b357",
          "Sha256": "928693d84d652dc15b3fcdc6576d790053755c5181ce6708b1110de12adae4a1",
          "WasExecutingWhileDetected": null,
          "UserDomain": "",
          "LogOnUsers": "W10-FOR-ATP\\\\Administrator",
          "MachineDomain": "",
          "MachineName": "w10-for-atp",
          "InternalIPv4List": "10.4.18.162;127.0.0.1",
          "InternalIPv6List": "2001:db8:123:2:5406:2223:9f79:e2ac;2001:db8:123:2:10eb:5adc:f27a:d6b3;fe80::5406:2223:9f79:e2ac;::1",
          "FileHash": "04ce0b79ea20332cc4ff4679883b18bfe4341fbd",
          "DeviceID": "xxxxxxxx",
          "MachineGroup": "",
          "Description": "Unusual behavior of sensitive information lookup",
          "BuiltInMachineTags": "",
          "UserDefinedMachineTags": "",
          "CommandLine": "",
          "ExternalId": "0D8219073DC9243ECADD537ECA9C2B414143594E",
          "IocUniqueId": "b1agHW5IpUdZpf6_KstT3dNo0dffOAx_5Sbs4tN4CUU="
        }]"""

        fake_payload_json = json.loads(fake_payload, strict=False)
        return komand.helper.clean(fake_payload_json)

    def fake_machine_info(self):
        fake_payload = """
        {
           "@odata.context":"https://api.securitycenter.windows.com/api/$metadata#Machines/$entity",
           "id":"c6944fa14970633adeecbabc104167ef12557a6f",
           "computerDnsName":"w10-for-atp",
           "firstSeen":"2018-11-07T17:59:46.4708884Z",
           "lastSeen":"2018-11-28T07:29:48.8372663Z",
           "osPlatform":"Windows10",
           "lastIpAddress":"10.4.18.162",
           "lastExternalIpAddress":"128.177.65.3",
           "agentVersion":"10.4850.17134.191",
           "osBuild":17134,
           "healthStatus":"Active",
           "rbacGroupId":0,
           "riskScore":"Medium",
           "isAadJoined":false,
           "machineTags":[]
        }
        """

        fake_payload_json = json.loads(fake_payload, strict=False)
        return komand.helper.clean(fake_payload_json)

    def fake_isolation_response(self):
        fake_payload = """
        {
            "@odata.context": "https://graph.microsoft.com/testwdatppreview/$metadata#MachineActions/$entity",
            "id": "b89eb834-4578-496c-8be0-03f004061435",
            "type": "Isolate",
            "requestor": "Analyst@contoso.com ",
            "requestorComment": "Isolate machine due to alert 1234",
            "status": "InProgress",
            "error": "None",
            "machineId": "f46b9bb259ed4a7fb9981b73510e3cc7aa81ec1f",
            "creationDateTimeUtc": "2017-12-04T12:12:18.9725659Z",
            "lastUpdateTimeUtc": "2017-12-04T12:12:18.9725659Z"
        }
        """

        fake_payload_json = json.loads(fake_payload, strict=False)
        return komand.helper.clean(fake_payload_json)

    def fake_file_info(self):
        fake_payload = """
        {
            "@odata.context": "https://api.securitycenter.windows.com/api/$metadata#Files",
            "value": [
                {
                    "sha1": "654f19c41d9662cf86be21bf0af5a88c38c56a9d",
                    "sha256": "2f905feec2798cee6f63da2c26758d86bfeaab954c01e20ac7085bf55fedde87",
                    "md5": "82849dc81d94056224445ea73dc6153a",
                    "globalPrevalence": 33,
                    "globalFirstObserved": "2018-07-17T18:17:27.5909748Z",
                    "globalLastObserved": "2018-08-06T16:07:12.9414137Z",
                    "windowsDefenderAVThreatName": null,
                    "size": 801112,
                    "fileType": "PortableExecutable",
                    "isPeFile": true,
                    "filePublisher": null,
                    "fileProductName": null,
                    "signer": "Microsoft Windows",
                    "issuer": "Microsoft Development PCA 2014",
                    "signerHash": "9e284231a4d1c53fc8d4492b09f65116bf97447f",
                    "isValidCertificate": true
                }
            ]
        }
        """

        fake_payload_json = json.loads(fake_payload, strict=False)
        return komand.helper.clean(fake_payload_json)
