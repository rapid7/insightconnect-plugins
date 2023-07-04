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
    OBJECT_TYPES = {
        "domain": pytmv1.ObjectType.DOMAIN,
        "ip": pytmv1.ObjectType.IP,
        "filesha1": pytmv1.ObjectType.FILE_SHA1,
        "filesha256": pytmv1.ObjectType.FILE_SHA256,
        "sendermailaddress": pytmv1.ObjectType.SENDER_MAIL_ADDRESS,
        "url": pytmv1.ObjectType.URL,
    }

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
        block_objects = params.get(Input.BLOCK_OBJECTS)
        # Choose enum
        for block_object in block_objects:
            object_type = self.OBJECT_TYPES.get(block_object["object_type"].lower())
            if not object_type:
                raise PluginException(
                    cause="Invalid object type.",
                    assistance="Please check the provided object type and object value.",
                )
        # Make Action API Call
        self.logger.info("Making API Call...")
        multi_resp = []
        for block_object in block_objects:
            response = client.add_to_exception_list(
                pytmv1.ObjectTask(
                    objectType=block_object["object_type"],
                    objectValue=block_object["object_value"],
                    description=block_object.get("description", ""),
                )
            )
            if "error" in response.result_code.lower():
                raise PluginException(
                    cause="An error occurred while adding to exception list.",
                    assistance="Please check the object_value and object_type parameters.",
                    data=response.errors,
                )
            items = response.response.dict().get("items")[0]
            items["task_id"] = "None" if items.get("task_id") is None else items["task_id"]
            multi_resp.append(items)
        # Return results
        self.logger.info("Returning Results...")
        return {Output.MULTI_RESPONSE: multi_resp}
