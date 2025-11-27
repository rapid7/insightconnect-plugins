import insightconnect_plugin_runtime
from .schema import RunAnalysisInput, RunAnalysisOutput, Input, Output, Component

# Custom imports below
import base64
from insightconnect_plugin_runtime.exceptions import PluginException


class RunAnalysis(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="run_analysis",
            description=Component.DESCRIPTION,
            input=RunAnalysisInput(),
            output=RunAnalysisOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        object_type = params.get(Input.OBJ_TYPE, "file")
        provided_file = params.get(Input.FILE, {})
        provided_url = params.get(Input.OBJ_URL, "")
        # END INPUT BINDING - DO NOT REMOVE

        files = None
        filename = None
        file_content = None

        # If a file is provided, extract filename and content
        if provided_file:
            filename = provided_file.get("filename")
            file_content = provided_file.get("content")

        # Validation checks
        if object_type != "file" and file_content:
            raise PluginException(
                cause=f"The content of the file was provided, but the object type '{object_type}' was selected.",
                assistance="To analyze a file, change the object type to 'file'.",
            )

        if object_type == "file" and provided_url:
            raise PluginException(
                cause="Invalid input.",
                assistance="File submission from URL only possible with type 'url' or 'download'.",
            )

        if object_type == "file" and (not filename or not file_content):
            raise PluginException(
                cause="Missing filename or content.",
                assistance="Complete the file input with filename and base64 file content.",
            )

        if object_type in ["url", "download"] and not provided_url:
            raise PluginException(
                cause=f"Object type '{object_type}' was selected, but no URL was provided.",
                assistance="Please provide a URL and try again.",
            )

        if object_type != "url" and params.get(Input.OBJ_EXT_BROWSER):
            raise PluginException(cause="Invalid input.", assistance="Browser name only possible with type 'url'.")

        if object_type not in ["download", "url"] and (
            params.get(Input.OBJ_EXT_USERAGENT) or params.get(Input.OPT_PRIVACY_HIDESOURCE)
        ):
            raise PluginException(
                cause="Invalid input.",
                assistance="User agent only possible with type 'download' or 'url'.",
            )

        if object_type == "file" and filename and file_content:
            files = {
                "file": (
                    filename,
                    base64.decodebytes(file_content.encode("ascii")),
                )
            }

        # Clean up parameters by removing empty strings
        new_params = {key: value for key, value in params.items() if value != ""}

        # Remove file parameter if a file is provided separately
        if provided_file:
            new_params.pop(Input.FILE, None)

        # Get the analysis task result
        task_result = self.connection.any_run_api.run_analysis(json_data=new_params, files=files)
        return {Output.UUID: task_result.get("data", {}).get("taskid", None)}
