import insightconnect_plugin_runtime
from .schema import AddToBlockListInput, AddToBlockListOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import pytmv1


class AddToBlockList(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_to_block_list",
            description=Component.DESCRIPTION,
            input=AddToBlockListInput(),
            output=AddToBlockListOutput(),
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
        multi_resp = {Output.MULTI_RESPONSE: []}
        for i in block_objects:
            response = client.add_to_block_list(
                pytmv1.ObjectTask(
                    objectType=i["object_type"],
                    objectValue=i["object_value"],
                    description=i.get("description", ""),
                )
            )
            if "error" in response.result_code.lower():
                raise PluginException(
                    cause="An error occurred while adding the object to the block list.",
                    assistance="Please check the provided object type and object value.",
                    data=response.errors,
                )
            else:
                multi_resp[Output.MULTI_RESPONSE].append(
                    response.response.dict().get("items")[0]
                )
        # Return results
        self.logger.info("Returning Results...")
        return multi_resp
