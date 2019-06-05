import komand
from .schema import CreateUserpolicyInput, CreateUserpolicyOutput
# Custom imports below
import requests
import xml.etree.ElementTree as ET


class CreateUserpolicy(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_userpolicy',
                description='Creates a user firewall policy',
                input=CreateUserpolicyInput(),
                output=CreateUserpolicyOutput())

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

        userpolicy = params["policy"]
        url = "https://{}/webconsole/APIController?".format(host + ":" + str(port))
        # Authentication
        auth = "<Request><Login><Username>{}</Username><Password>{}</Password></Login>".format(
            username,
            password
        )

        # Start of the operation to add a firewall policy
        start = "<Set operation=\"add\"><SecurityPolicy><Name>{}</Name>".format(userpolicy["SecurityPolicy"]["Name"])

        base_xml = "<Description>{}</Description><Status>{}</Status><IPFamily>{}</IPFamily>".format(
            userpolicy["SecurityPolicy"]["Description"],
            userpolicy["SecurityPolicy"]["Status"],
            userpolicy["SecurityPolicy"]["IPFamily"],
        )
        # Sets position xml
        if userpolicy["SecurityPolicy"]["Position"] == "after" or userpolicy["SecurityPolicy"]["Position"] == "before":
            position = "<{}>{}</{}>".format(
                userpolicy["SecurityPolicy"]["Position"],
                userpolicy["SecurityPolicy"]["PositionPolicyName"],
                userpolicy["SecurityPolicy"]["Position"]
            )
        else:
            position = userpolicy["SecurityPolicy"]["Position"]

        position_xml = "<Position>{}</Position>".format(position)

        policy_type = "<PolicyType>User</PolicyType>"

        # End of common config
        policy = ""
        # Start of Policy string
        policy += "<UserPolicy>"
        # Source Zones
        source_zones = userpolicy["SourceZones"]
        policy += buildnest_xml("SourceZones", source_zones, "Zones")
        # Source Networks
        source_networks = userpolicy["SourceNetworks"]
        policy += buildnest_xml("SourceNetworks", source_networks, "Network")
        # Services
        services = userpolicy["Services"]
        policy += buildnest_xml("Services", services, "Service")
        # Schedule
        schedule = userpolicy["Schedule"]
        policy += "<Schedule>{}</Schedule>".format(schedule)
        # Scan FTP
        scan_ftp = userpolicy["ScanFTP"]
        policy += "<ScanFTP>{}</ScanFTP>".format(scan_ftp)
        # Scan HTTP
        scan_http = userpolicy["ScanHTTP"]
        policy += "<ScanHTTP>{}</ScanHTTP>".format(scan_http)
        # Scan HTTPS
        scan_https = userpolicy["ScanHTTPS"]
        policy += "<ScanHTTPS>{}</ScanHTTPS>".format(scan_https)
        # Desrination Zones
        destination_zones = userpolicy["DestinationZones"]
        policy += buildnest_xml("DestinationZones", destination_zones, "Zone")
        # Destination Networks
        destination_networks = userpolicy["DestinationNetworks"]
        policy += buildnest_xml("DestinationNetworks", destination_networks, "Network")
        # Identity
        identity = userpolicy["Identity"]
        if identity:
            policy += buildnest_xml("Identity", identity, "Member")
        # Data Accounting
        data_accounting = userpolicy["DataAccounting"]
        policy += "<DataAccounting>{}</DataAccounting>".format(data_accounting)
        # Rewrite Source Address
        rwsource_address = userpolicy["RewriteSourceAddress"]
        policy += "<RewriteSourceAddress>{}</RewriteSourceAddress>".format(rwsource_address)
        # Outbound Address
        outbound_address = userpolicy["OutboundAddress"]
        policy += "<OutboundAddress>{}</OutboundAddress>".format(outbound_address)
        # Primary Gateway
        primary_gateway = userpolicy["PrimaryGateway"]
        policy += "<PrimaryGateway>{}</PrimaryGateway>".format(primary_gateway)
        # Backup Gateway
        backup_gateway = userpolicy["BackupGateway"]
        policy += "<BackupGateway>{}</BackupGateway>".format(backup_gateway)
        # DSCP Marking
        dscp_marking = userpolicy["DSCPMarking"]
        if dscp_marking:
            policy += "<DSCPMarking>{}</DSCPMarking>".format(dscp_marking)
        # Application Control
        app_contol = userpolicy["ApplicationControl"]
        policy += "<ApplicationControl>{}</ApplicationControl>".format(app_contol)
        # Application Base QoS Policy
        app_qos = userpolicy["ApplicationBaseQoSPolicy"]
        policy += "<ApplicationBaseQoSPolicy>{}</ApplicationBaseQoSPolicy>".format(app_qos)
        # Application Base QoS Policy
        web_filter = userpolicy["WebFilter"]
        policy += "<WebFilter>{}</WebFilter>".format(web_filter)
        # Web Category QoS
        web_cat_qos = userpolicy["WebCategoryBaseQoSPolicy"]
        policy += "<WebCategoryBaseQoSPolicy>{}</WebCategoryBaseQoSPolicy>".format(web_cat_qos)
        # Log Traffic
        log_traffic = userpolicy["LogTraffic"]
        policy += "<LogTraffic>{}</LogTraffic>".format(log_traffic)
        # End of User policy
        end_policy = "</UserPolicy>"
        # End of Policy String
        end = ""
        end += "<IntrusionPrevention>{}</IntrusionPrevention>".format(
            userpolicy["SecurityPolicy"]["IntrusionPrevention"])
        end += "<TrafficShapingPolicy>{}</TrafficShapingPolicy>".format(
            userpolicy["SecurityPolicy"]["TrafficShapingPolicy"])
        end += "<SourceSecurityHeartbeat>{}</SourceSecurityHeartbeat>".format(
            userpolicy["SecurityPolicy"]["SourceSecurityHeartbeat"])
        end += "<MinimumSourceHBPermitted />"
        end += "<DestSecurityHeartbeat>{}</DestSecurityHeartbeat>".format(
            userpolicy["SecurityPolicy"]["DestSecurityHeartbeat"])
        end += "<MinimumDestinationHBPermitted /></SecurityPolicy></Set></Request>"

        # Build request url
        request_string = "{}{}{}{}{}{}{}{}".format(auth, start, position_xml, base_xml, policy_type, policy, end_policy, end)

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
            self.logger.error("An error has occurred while adding a User policy: ", e)
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
