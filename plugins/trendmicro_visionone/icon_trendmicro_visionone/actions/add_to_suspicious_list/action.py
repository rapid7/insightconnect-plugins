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
    OBJECT_TYPE_MAPPING = {
        "domain": pytmv1.ObjectType.DOMAIN,
        "ip": pytmv1.ObjectType.IP,
        "filesha1": pytmv1.ObjectType.FILE_SHA1,
        "filesha256": pytmv1.ObjectType.FILE_SHA256,
        "sendermailaddress": pytmv1.ObjectType.SENDER_MAIL_ADDRESS,
        "url": pytmv1.ObjectType.URL,
    }

    SCAN_ACTION_MAPPING = {
        "block": pytmv1.ScanAction.BLOCK,
        "log": pytmv1.ScanAction.LOG,
    }

    RISK_LEVEL_MAPPING = {
        "high": pytmv1.RiskLevel.HIGH,
        "medium": pytmv1.RiskLevel.MEDIUM,
        "low": pytmv1.RiskLevel.LOW,
    }

    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_to_suspicious_list",
            description=Component.DESCRIPTION,
            input=AddToSuspiciousListInput(),
            output=AddToSuspiciousListOutput(),
        )

    def run(self, params={}):
        # Get Connection Client
        client = self.connection.client
        # Get Action Parameters
        block_objects = params.get(Input.SUSPICIOUS_BLOCK_OBJECTS)
        # Choose enum
        for block_object in block_objects:
            block_object["object_type"] = self.OBJECT_TYPE_MAPPING.get(
                block_object["object_type"].lower()
            )
            block_object["scan_action"] = self.SCAN_ACTION_MAPPING.get(
                block_object["scan_action"].lower()
            )
            block_object["risk_level"] = self.RISK_LEVEL_MAPPING.get(
                block_object["risk_level"].lower()
            )
            if not block_object["object_type"]:
                raise PluginException(
                    cause="Invalid object type.",
                    assistance="Please check the provided object type and object value.",
                )
        # Make Action API Call
        self.logger.info("Making API Call...")
        multi_resp = []
        for block_object in block_objects:
            response = client.add_to_suspicious_list(
                pytmv1.SuspiciousObjectTask(
                    objectType=block_object["object_type"],
                    objectValue=block_object["object_value"],
                    scan_action=block_object.get("scan_action", "block"),
                    risk_level=block_object.get("risk_level", "medium"),
                    days_to_expiration=block_object.get("expiry_days", 30),
                )
            )
            if "error" in response.result_code.lower():
                raise PluginException(
                    cause="An error occurred while adding to the suspicious list.",
                    assistance="Please check the input parameters and try again.",
                    data=response.errors,
                )
            items = response.response.dict().get("items")[0]
            items["task_id"] = (
                "None" if items.get("task_id") is None else items["task_id"]
            )
            multi_resp.append(items)
        # Return results
        self.logger.info("Returning Results...")
        return {Output.MULTI_RESPONSE: multi_resp}
