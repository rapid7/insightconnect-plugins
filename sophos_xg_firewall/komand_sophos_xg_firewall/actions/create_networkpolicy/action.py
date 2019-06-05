import komand
from .schema import CreateNetworkpolicyInput, CreateNetworkpolicyOutput
# Custom imports below
import requests
import xml.etree.ElementTree as ET


class CreateNetworkpolicy(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_networkpolicy',
                description='Creates a network firewall policy',
                input=CreateNetworkpolicyInput(),
                output=CreateNetworkpolicyOutput())

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

        networkpolicy = params["policy"]
        url = "https://{}/webconsole/APIController?".format(host + ":" + str(port))
        # Authentication
        auth = "<Request><Login><Username>{}</Username><Password>{}</Password></Login>".format(
            username,
            password
        )

        # Start of the operation to add a firewall policy
        start = "<Set operation=\"add\"><SecurityPolicy><Name>{}</Name>".format(networkpolicy["SecurityPolicy"]["Name"])

        base_xml = "<Description>{}</Description><Status>{}</Status><IPFamily>{}</IPFamily>".format(
            networkpolicy["SecurityPolicy"]["Description"],
            networkpolicy["SecurityPolicy"]["Status"],
            networkpolicy["SecurityPolicy"]["IPFamily"],
        )
        # Sets position xml
        if networkpolicy["SecurityPolicy"]["Position"] == "after" or networkpolicy["SecurityPolicy"]["Position"] == "before":
            position = "<{}>{}</{}>".format(
                networkpolicy["SecurityPolicy"]["Position"],
                networkpolicy["SecurityPolicy"]["PositionPolicyName"],
                networkpolicy["SecurityPolicy"]["Position"]
            )
        else:
            position = networkpolicy["SecurityPolicy"]["Position"]

        position_xml = "<Position>{}</Position>".format(position)

        policy_type = "<PolicyType>Network</PolicyType>"

        # End of common config
        # Start of Policy string
        policy = ""
        # Start of Network Policy
        policy += "<NetworkPolicy>"
        # Source Zones
        source_zones = networkpolicy["SourceZones"]
        policy += buildnest_xml("SourceZones", source_zones, "Zone")
        # Source Networks
        source_networks = networkpolicy["SourceNetworks"]
        if source_networks:
            policy += buildnest_xml("SourceNetworks", source_networks, "Network")
        # Services
        services = networkpolicy["Services"]
        if services:
            policy += buildnest_xml("Services", services, "Service")
        # Schedule
        schedule = networkpolicy["Schedule"]
        if schedule:
            policy += "<Schedule>{}</Schedule>".format(schedule)
        # Destination Zones
        destination_zones = networkpolicy["DestinationZones"]
        policy += buildnest_xml("DestinationZones", destination_zones, "Zone")
        # Destination Networks
        destination_networks = networkpolicy["DestinationNetworks"]
        if destination_networks:
            policy += buildnest_xml("DestinationNetworks", destination_networks, "Network")
        # Action
        action = networkpolicy["Action"]
        if action:
            policy += "<Action>{}</Action>".format(action)
        # Match Identity
        match_id = networkpolicy["MatchIdentity"]
        if match_id:
            policy += "<MatchIdentity>{}</MatchIdentity>".format(match_id)
        # Identity
        identity = networkpolicy["Identity"]
        if identity:
            policy += buildnest_xml("Identity", identity, "Member")
        # Data Accounting
        data_accounting = networkpolicy["DataAccounting"]
        if data_accounting:
            policy += "<DataAccounting>{}</DataAccounting>".format(data_accounting)
        # Rewrite Source Address
        rwsource_address = networkpolicy["RewriteSourceAddress"]
        if rwsource_address:
            policy += "<RewriteSourceAddress>{}</RewriteSourceAddress>".format(rwsource_address)
        # Outbound Address
        outbound_address = networkpolicy["OutboundAddress"]
        if outbound_address:
            policy += "<OutboundAddress>{}</OutboundAddress>".format(outbound_address)
        # Primary Gateway
        primary_gateway = networkpolicy["PrimaryGateway"]
        if primary_gateway:
            policy += "<PrimaryGateway>{}</PrimaryGateway>".format(primary_gateway)
        # Backup Gateway
        backup_gateway = networkpolicy["BackupGateway"]
        if backup_gateway:
            policy += "<BackupGateway>{}</BackupGateway>".format(backup_gateway)
        # DSCP Marking
        dscp_marking = networkpolicy["DSCPMarking"]
        if dscp_marking:
            policy += "<DSCPMarking>{}</DSCPMarking>".format(dscp_marking)
        # Log Traffic
        log_traffic = networkpolicy["LogTraffic"]
        if log_traffic:
            policy += "<LogTraffic>{}</LogTraffic>".format(log_traffic)
        # End Network Policy
        end_policy = "</NetworkPolicy>"
        # End of Policy String
        end = ""
        end += "<IntrusionPrevention>{}</IntrusionPrevention>".format(
            networkpolicy["SecurityPolicy"]["IntrusionPrevention"])
        end += "<TrafficShapingPolicy>{}</TrafficShapingPolicy>".format(
            networkpolicy["SecurityPolicy"]["TrafficShapingPolicy"])
        end += "<SourceSecurityHeartbeat>{}</SourceSecurityHeartbeat>".format(
            networkpolicy["SecurityPolicy"]["SourceSecurityHeartbeat"])
        end += "<MinimumSourceHBPermitted />"
        end += "<DestSecurityHeartbeat>{}</DestSecurityHeartbeat>".format(
            networkpolicy["SecurityPolicy"]["DestSecurityHeartbeat"])
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
            self.logger.error("An error has occurred while adding a Network policy: ", e)
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
