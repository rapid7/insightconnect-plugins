import insightconnect_plugin_runtime
from .schema import (
    AddToExceptionListInput,
    AddToExceptionListOutput,
    Input,
    Output,
    Component,
)
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import pytmv1


class AddToExceptionList(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_to_exception_list",
            description=Component.DESCRIPTION,
            input=AddToExceptionListInput(),
            output=AddToExceptionListOutput(),
        )

    def run(self, params={}):
        # Get Connection Client
        client = self.connection.client
        # Get Action Parameters
        block_objects = params.get(Input.BLOCK_OBJECT)
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
        multi_resp = {"multi_response": []}
        for i in block_objects:
            response = client.add_to_exception_list(
                pytmv1.ObjectTask(
                    objectType=i["object_type"],
                    objectValue=i["object_value"],
                    description=i.get("description", ""),
                )
            )
            if "error" in response.result_code.lower():
                raise PluginException(
                    cause="An error occurred while adding to exception list.",
                    assistance="Please check the object_value and object_type parameters.",
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
