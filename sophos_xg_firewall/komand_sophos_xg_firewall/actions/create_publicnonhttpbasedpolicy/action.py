import komand
from .schema import CreatePublicnonhttpbasedpolicyInput, CreatePublicnonhttpbasedpolicyOutput
# Custom imports below
import requests
import xml.etree.ElementTree as ET


class CreatePublicnonhttpbasedpolicy(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_publicnonhttpbasedpolicy',
                description='Creates a PublicHTTPBased policy',
                input=CreatePublicnonhttpbasedpolicyInput(),
                output=CreatePublicnonhttpbasedpolicyOutput())

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

        pubnonhttppolicy = params["policy"]
        url = "https://{}/webconsole/APIController?".format(host + ":" + str(port))
        # Authentication
        auth = "<Request><Login><Username>{}</Username><Password>{}</Password></Login>".format(
            username,
            password
        )

        # Start of the operation to add a firewall policy
        start = "<Set operation=\"add\"><SecurityPolicy><Name>{}</Name>".format(pubnonhttppolicy["SecurityPolicy"]["Name"])

        base_xml = "<Description>{}</Description><Status>{}</Status><IPFamily>{}</IPFamily>".format(
            pubnonhttppolicy["SecurityPolicy"]["Description"],
            pubnonhttppolicy["SecurityPolicy"]["Status"],
            pubnonhttppolicy["SecurityPolicy"]["IPFamily"],
        )
        # Sets position xml
        if pubnonhttppolicy["SecurityPolicy"]["Position"] == "after" or pubnonhttppolicy["SecurityPolicy"]["Position"] == "before":
            position = "<{}>{}</{}>".format(
                pubnonhttppolicy["SecurityPolicy"]["Position"],
                pubnonhttppolicy["SecurityPolicy"]["PositionPolicyName"],
                pubnonhttppolicy["SecurityPolicy"]["Position"]
            )
        else:
            position = pubnonhttppolicy["SecurityPolicy"]["Position"]

        position_xml = "<Position>{}</Position>".format(position)

        policy_type = "<PolicyType>PublicNonHTTPPolicy</PolicyType>"

        # End of common config
        # Start of Policy string
        policy = ""
        policy += "<PublicNonHTTPBasedPolicy>"
        # Source Zones
        source_zones = pubnonhttppolicy["SourceZones"]
        policy += buildnest_xml("SourceZones", source_zones, "Zones")
        # Hosted Address
        host_addr = pubnonhttppolicy["HostedAddress"]
        policy += "<HostedAddress>{}</HostedAddress>".format(host_addr)
        # Scan SMTP
        scan_smtp = pubnonhttppolicy["ScanSMTP"]
        policy += "<ScanSMTP>{}</ScanSMTP>".format(scan_smtp)
        # Scan IMAP
        scan_imap = pubnonhttppolicy["ScanIMAP"]
        policy += "<ScanIMAP>{}</ScanIMAP>".format(scan_imap)
        # Scan POP3
        scan_pop = pubnonhttppolicy["ScanPOP3"]
        policy += "<ScanPOP3>{}</ScanPOP3>".format(scan_pop)
        # SMTPS
        scan_smtps = pubnonhttppolicy["ScanSMTPS"]
        policy += "<ScanSMTPS>{}</ScanSMTPS>".format(scan_smtps)
        # Scan POP3S
        scan_pops = pubnonhttppolicy["ScanPOP3S"]
        policy += "<ScanPOP3S>{}</ScanPOP3S>".format(scan_pops)
        # Rewrite Source Address
        rwsource_address = pubnonhttppolicy["RewriteSourceAddress"]
        policy += "<RewriteSourceAddress>{}</RewriteSourceAddress>".format(rwsource_address)
        # Outbound Address
        outbound_address = pubnonhttppolicy["OutboundAddress"]
        policy += "<OutboundAddress>{}</OutboundAddress>".format(outbound_address)
        # Match Identity
        match_id = pubnonhttppolicy["MatchIdentity"]
        policy += "<MatchIdentity>{}</MatchIdentity>".format(match_id)
        # Identity
        identity = pubnonhttppolicy["Identity"]
        policy += buildnest_xml("Identity", identity, "Member")
        # Data Accounting
        data_accounting = pubnonhttppolicy["DataAccounting"]
        policy += "<DataAccounting>{}</DataAccounting>".format(data_accounting)
        # Log Traffic
        log_traffic = pubnonhttppolicy["LogTraffic"]
        policy += "<LogTraffic>{}</LogTraffic>".format(log_traffic)
        # End
        end_policy = "</PublicNonHTTPBasedPolicy>"
        # End of Policy String
        end = ""
        end += "<IntrusionPrevention>{}</IntrusionPrevention>".format(
            pubnonhttppolicy["SecurityPolicy"]["IntrusionPrevention"])
        end += "<TrafficShapingPolicy>{}</TrafficShapingPolicy>".format(
            pubnonhttppolicy["SecurityPolicy"]["TrafficShapingPolicy"])
        end += "<SourceSecurityHeartbeat>{}</SourceSecurityHeartbeat>".format(
            pubnonhttppolicy["SecurityPolicy"]["SourceSecurityHeartbeat"])
        end += "<MinimumSourceHBPermitted />"
        end += "<DestSecurityHeartbeat>{}</DestSecurityHeartbeat>".format(
            pubnonhttppolicy["SecurityPolicy"]["DestSecurityHeartbeat"])
        end += "<MinimumDestinationHBPermitted /></SecurityPolicy></Set></Request>"

        # Build request url
        request_string = "{}{}{}{}{}{}{}{}".format(auth, start, position_xml, base_xml, policy_type, policy, end_policy, end)

        status_code = 00
        status_response = "default"
        invalid_params = ""
        try:
            r = requests.post(url,files={"reqxml": (None, request_string)}, verify=False)
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
            self.logger.error("An error has occurred while adding a Public Non HTTP based policy: ", e)
            raise
        return {"response": {
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
