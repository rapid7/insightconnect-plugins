import insightconnect_plugin_runtime
from .schema import (
    RemoveFromSuspiciousListInput,
    RemoveFromSuspiciousListOutput,
    Input,
    Output,
    Component,
)
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import pytmv1


class RemoveFromSuspiciousList(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="remove_from_suspicious_list",
            description=Component.DESCRIPTION,
            input=RemoveFromSuspiciousListInput(),
            output=RemoveFromSuspiciousListOutput(),
        )

    def run(self, params={}):
        # Get Connection Client
        client = self.connection.client
        # Get Action Parameters
        block_objects = params.get(Input.BLOCK_OBJECTS)
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
        # Make Action API Call
        self.logger.info("Making API Call...")
        multi_resp = {Output.MULTI_RESPONSE: []}
        for i in block_objects:
            response = client.remove_from_suspicious_list(
                pytmv1.ObjectTask(
                    objectType=i["object_type"], objectValue=i["object_value"]
                )
            )
            if "error" in response.result_code.lower():
                raise PluginException(
                    cause="An error occurred when removing object from suspicious list.",
                    assistance="Check if the object type and value are correct.",
                    data=response.errors,
                )
            else:
                items = response.response.dict().get("items")[0]
                items["task_id"] = (
                    "None" if items.get("task_id") is None else items["task_id"]
                )
                multi_resp[Output.MULTI_RESPONSE].append(items)
        # Return results
        self.logger.info("Returning Results...")
        return multi_resp
