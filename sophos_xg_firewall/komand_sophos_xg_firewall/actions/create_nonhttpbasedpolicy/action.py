import komand
from .schema import CreateNonhttpbasedpolicyInput, CreateNonhttpbasedpolicyOutput
# Custom imports below
import requests
import xml.etree.ElementTree as ET


class CreateNonhttpbasedpolicy(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_nonhttpbasedpolicy',
                description='Creates a NonHTTPBased policy',
                input=CreateNonhttpbasedpolicyInput(),
                output=CreateNonhttpbasedpolicyOutput())

    def run(self, params={}):
        username = self.connection.username
        password = self.connection.password
        host = self.connection.host
        port = self.connection.port

        def buildnest_xml(tlxml, values, nest_item):
            xml_string = ""
            xml_string += "<{}>".format(tlxml)
            for value in values:
                xml_string += "<{}>{}</{}>".format(nest_item, value, nest_item)
            xml_string += "</{}>".format(tlxml)
            return xml_string

        nonhttpbased = params["policy"]
        url = "https://{}/webconsole/APIController?".format(host + ":" + str(port))
        # Authentication
        auth = "<Request><Login><Username>{}</Username><Password>{}</Password></Login>".format(
            username,
            password
        )

        # Start of the operation to add a firewall policy
        start = "<Set operation=\"add\"><SecurityPolicy><Name>{}</Name>".format(nonhttpbased["SecurityPolicy"]["Name"])

        base_xml = "<Description>{}</Description><Status>{}</Status><IPFamily>{}</IPFamily>".format(
            nonhttpbased["SecurityPolicy"]["Description"],
            nonhttpbased["SecurityPolicy"]["Status"],
            nonhttpbased["SecurityPolicy"]["IPFamily"],
        )
        # Sets position xml
        if nonhttpbased["SecurityPolicy"]["Position"] == "after" or nonhttpbased["SecurityPolicy"]["Position"] == "before":
            position = "<{}>{}</{}>".format(
                nonhttpbased["SecurityPolicy"]["Position"],
                nonhttpbased["SecurityPolicy"]["PositionPolicyName"],
                nonhttpbased["SecurityPolicy"]["Position"]
            )
        else:
            position = nonhttpbased["SecurityPolicy"]["Position"]

        position_xml = "<Position>{}</Position>".format(position)

        policy_type = "<PolicyType>NonHTTPBased</PolicyType>"

        # End of common config
        # Start of Policy string
        policy = ""

        policy += "<NonHTTPBasedPolicy>"
        # Source Zones
        source_zones = nonhttpbased["SourceZones"]
        policy += buildnest_xml("SourceZones", source_zones, "Zones")
        # Source Networks
        source_networks = nonhttpbased["SourceNetworks"]
        policy += buildnest_xml("SourceNetworks", source_networks, "Network")
        # ExceptionNetworks
        exception_networks = nonhttpbased["ExceptionNetworks"]
        policy += buildnest_xml("ExceptionNetworks", exception_networks, "Network")
        # Host Address
        host_addr = nonhttpbased["HostedAddress"]
        policy += "<HostedAddress>{}</HostedAddress>".format(host_addr)
        # Scan SMTP
        scan_smtp = nonhttpbased["ScanSMTP"]
        policy += "<ScanSMTP>{}</ScanSMTP>".format(scan_smtp)
        # Scan IMAP
        scan_imap = nonhttpbased["ScanIMAP"]
        policy += "<ScanIMAP>{}</ScanIMAP>".format(scan_imap)
        # Scan POP3
        scan_pop = nonhttpbased["ScanPOP3"]
        policy += "<ScanPOP3>{}</ScanPOP3>".format(scan_pop)
        # SMTPS
        scan_smtps = nonhttpbased["ScanSMTPS"]
        policy += "<ScanSMTPS>{}</ScanSMTPS>".format(scan_smtps)
        # Scan POP3S
        scan_pops = nonhttpbased["ScanPOP3S"]
        policy += "<ScanPOP3S>{}</ScanPOP3S>".format(scan_pops)
        # Protected Zone
        protected_zone = nonhttpbased["ProtectedZone"]
        policy += "<ProtectedZone>{}</ProtectedZone>".format(protected_zone)
        # Protected Servers
        protected_server = nonhttpbased["ProtectedServer"]
        policy += "<ProtectedServer>{}</ProtectedServer>".format(protected_server)
        # Forward Ports
        policy += "<ForwardPorts>{}</ForwardPorts>".format(nonhttpbased["ForwardPorts"])
        # Protocol
        policy += "<Protocol>{}</Protocol>".format(nonhttpbased["Protocol"])
        # External Ports
        external_port = nonhttpbased["ExternalPort"]
        if external_port > 0:
            policy += "<ExternalPort>{}</ExternalPort>".format(nonhttpbased["ExternalPort"])
        # External Port Range
        policy += "<ExternalPortRange>"
        start_external_prange = nonhttpbased["ExternalPortRange"]
        if start_external_prange["start"] > 0 or start_external_prange["end"] > 0:
            policy += "<Start>{}</Start>".format(nonhttpbased["ExternalPortRange"]["start"])
            policy += "<End>{}</End>".format(nonhttpbased["ExternalPortRange"]["end"])
            policy += "</ExternalPortRange>"
        else:
            policy += "<Start>{}</Start>".format("")
            policy += "<End>{}</End>".format("")
            policy += "</ExternalPortRange>"
        # External Port list
        policy += "<ExternalPortList>"
        external_plist = nonhttpbased["ExternalPortList"]
        plist = ""
        for ports in external_plist:
            plist += str(ports) + ","
        policy += plist
        policy += "</ExternalPortList>"
        # Mapped Port
        policy += "<MappedPort>{}</MappedPort>".format(nonhttpbased["MappedPort"])
        # Mapped Port Range
        policy += "<MappedPortRange>"
        mapped_port_range = nonhttpbased["MappedPortRange"]
        if mapped_port_range["start"] > 0 or mapped_port_range["end"] > 0:
            policy += "<Start>{}</Start>".format(nonhttpbased["MappedPortRange"]["start"])
            policy += "<End>{}</End>".format(nonhttpbased["MappedPortRange"]["end"])
            policy += "</MappedPortRange>"
        else:
            policy += "<Start>{}</Start>".format("")
            policy += "<End>{}</End>".format("")
            policy += "</MappedPortRange>"
        # Mapped Port list
        policy += "<MappedPortList>"
        external_plist = nonhttpbased["MappedPortList"]
        mplist = ""
        for mports in external_plist:
            mplist += str(mports) + ","
        policy += mplist
        policy += "</MappedPortList>"
        # Rewrite Source Address
        policy += "<RewriteSourceAddress>{}</RewriteSourceAddress>".format(nonhttpbased["RewriteSourceAddress"])
        # Outbound Address
        policy += "<OutboundAddress>{}</OutboundAddress>".format(nonhttpbased["OutboundAddress"])
        # Match Identity
        policy += "<MatchIdentity>{}</MatchIdentity>".format(nonhttpbased["MatchIdentity"])
        # Identity
        identity = nonhttpbased["Identity"]
        policy += buildnest_xml("Identity", identity, "Member")
        # Data Accounting
        data_accounting = nonhttpbased["DataAccounting"]
        policy += "<DataAccounting>{}</DataAccounting>".format(data_accounting)
        # Reflexive Rule
        policy += "<ReflexiveRule>{}</ReflexiveRule>".format(nonhttpbased["ReflexiveRule"])
        # Log Traffic
        log_traffic = nonhttpbased["LogTraffic"]
        policy += "<LogTraffic>{}</LogTraffic>".format(log_traffic)
        # End of NonHTTP Based Policy
        end_policy = "</NonHTTPBasedPolicy>"
        # End of Policy String
        end = ""
        end += "<IntrusionPrevention>{}</IntrusionPrevention>".format(
            nonhttpbased["SecurityPolicy"]["IntrusionPrevention"])
        end += "<TrafficShapingPolicy>{}</TrafficShapingPolicy>".format(
            nonhttpbased["SecurityPolicy"]["TrafficShapingPolicy"])
        end += "<SourceSecurityHeartbeat>{}</SourceSecurityHeartbeat>".format(
            nonhttpbased["SecurityPolicy"]["SourceSecurityHeartbeat"])
        end += "<MinimumSourceHBPermitted />"
        end += "<DestSecurityHeartbeat>{}</DestSecurityHeartbeat>".format(
            nonhttpbased["SecurityPolicy"]["DestSecurityHeartbeat"])
        end += "<MinimumDestinationHBPermitted /></SecurityPolicy></Set></Request>"

        # Build request url
        request_string = "{}{}{}{}{}{}{}{}".format(auth, start, position_xml, base_xml, policy_type, policy, end_policy,
                                                   end)

        status_code = 00
        status_response = "default"
        invalid_params = ""
        try:
            r = requests.post(url, files={"reqxml": (None, request_string)}, verify=False)
            tree = ET.fromstring(r.content)
            resp_status = tree.find("SecurityPolicy/Status")
            error_status = tree.find("Status")
            inval_params = tree.findall("SecurityPolicy/InvalidParams/Params")
            try:
                status_code = resp_status.get("code")
                status_response = resp_status.text
            except:
                pass
            try:
                status_code = error_status.get("code")
                status_response = error_status.text
            except:
                pass
            try:
                for item in inval_params:
                    invalid_params += "{} ".format(item.text)
            except:
                pass
            if invalid_params == "":
                invalid_params = "None"
        except Exception as e:
            self.logger.error("An error has occurred while adding a NonHTTPBased policy: ", e)
            raise
        return {"response":{
            "status_code": status_code,
            "status_response": status_response,
            "invalid_params": invalid_params
            }
        }

    def test(self):
        username = self.connection.username
        password = self.connection.password
        host = self.connection.host
        port = self.connection.port
        request_string = "<Request><Login><Username>{}</Username><Password>{}</Password></Login><Get><User></User></Get></Request>".format(
            username, password)
        url = "https://{}/webconsole/APIController?".format(host + ":" + str(port))
        try:
            response = requests.get(url, files={"reqxml": (None, request_string)}, verify=False)
            if not response.status_code // 100 == 2:
                self.logger.error("Error: Unexpected response {}".format(response))
            else:
                return {"success": True}
        except requests.exceptions.RequestException as e:
            self.logger.error("Error: {}".format(e))
            raise
