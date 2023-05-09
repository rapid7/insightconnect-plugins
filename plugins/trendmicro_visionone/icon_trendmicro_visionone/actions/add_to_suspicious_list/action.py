import insightconnect_plugin_runtime
from .schema import (
    AddToSuspiciousListInput,
    AddToSuspiciousListOutput,
    Input,
    Output,
    Component,
)
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import pytmv1


class AddToSuspiciousList(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_to_suspicious_list",
            description=Component.DESCRIPTION,
            input=AddToSuspiciousListInput(),
            output=AddToSuspiciousListOutput(),
        )

    def run(self, params={}):
        # Get Connection Parameters
        url = self.connection.server
        token = self.connection.token_
        app = self.connection.app
        # Get Action Parameters
        block_objects = params.get(Input.SUSPICIOUS_BLOCK_OBJECT)
        # Choose enum
        for i in block_objects:
            if "domain" in i["object_type"].lower():
                i["object_type"] = pytmv1.ObjectType.DOMAIN
            elif "ip" in i["object_type"].lower():
                i["object_type"] = pytmv1.ObjectType.IP
            elif "filesha1" in i["object_type"].lower():
                i["object_type"] = pytmv1.ObjectType.FILE_SHA1
            elif "filesha256" in i["object_type"].lower():
                i["object_type"] = pytmv1.ObjectType.FILE_SHA256
            elif "sendermailaddress" in i["object_type"].lower():
                i["object_type"] = pytmv1.ObjectType.SENDER_MAIL_ADDRESS
            elif "url" in i["object_type"].lower():
                i["object_type"] = pytmv1.ObjectType.URL
            elif "block" in i["scan_action"].lower():
                i["scan_action"] = pytmv1.ScanAction.BLOCK
            elif "log" in i["scan_action"].lower():
                i["scan_action"] = pytmv1.ScanAction.LOG
            elif "high" in i["risk_level"].lower():
                i["risk_level"] = pytmv1.RiskLevel.HIGH
            elif "medium" in i["risk_level"].lower():
                i["risk_level"] = pytmv1.RiskLevel.MEDIUM
            elif "low" in i["risk_level"].lower():
                i["risk_level"] = pytmv1.RiskLevel.LOW
        # Initialize PYTMV1 Client
        self.logger.info("Initializing PYTMV1 Client...")
        client = pytmv1.client(app, token, url)
        # Make Action API Call
        self.logger.info("Making API Call...")
        multi_resp = {"multi_response": []}
        for i in block_objects:
            response = client.add_to_suspicious_list(
                pytmv1.SuspiciousObjectTask(
                    objectType=i["object_type"],
                    objectValue=i["object_value"],
                    scan_action=i.get("scan_action", "block"),
                    risk_level=i.get("risk_level", "medium"),
                    days_to_expiration=i.get("expiry_days", 30),
                )
            )
            if "error" in response.result_code.lower():
                raise PluginException(
                    cause="An error occurred while adding to the suspicious list.",
                    assistance="Please check the input parameters and try again.",
                    data=response.errors,
                )
            else:
                items = response.response.dict().get("items")[0]
                items["task_id"] = (
                    "None" if items.get("task_id") is None else items["task_id"]
                )
                multi_resp["multi_response"].append(items)
        # Return results
        self.logger.info("Returning Results...")
        return multi_resp
