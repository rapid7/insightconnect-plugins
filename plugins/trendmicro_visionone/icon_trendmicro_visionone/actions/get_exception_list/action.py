import insightconnect_plugin_runtime
from .schema import (
    GetExceptionListInput,
    GetExceptionListOutput,
    Input,
    Output,
    Component,
)
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import json


class GetExceptionList(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_exception_list",
            description=Component.DESCRIPTION,
            input=GetExceptionListInput(),
            output=GetExceptionListOutput(),
        )

    def run(self, params={}):  # pylint: disable=unused-argument
        # Get Connection Client
        client = self.connection.client
        new_exceptions = []
        # Make Action API Call
        self.logger.info("Making API Call...")
        response = client.object.consume_exception(lambda exception: new_exceptions.append(exception.model_dump()))
        if "error" in response.result_code.lower():
            raise PluginException(
                cause="Consume Exception List failed with following exception.",
                assistance="Please check your connection details and try again.",
                data=response.error,
            )
        # Load json objects to list
        exception_objects = []
        for new_exception in new_exceptions:
            new_exception["description"] = "" if not new_exception["description"] else new_exception["description"]
            new_exception = json.dumps(new_exception)
            exception_objects.append(json.loads(new_exception))
        # Return results
        self.logger.info("Returning Results...")
        return {Output.EXCEPTION_OBJECTS: exception_objects}
