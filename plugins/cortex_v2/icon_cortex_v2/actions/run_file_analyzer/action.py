import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import RunFileAnalyzerInput, RunFileAnalyzerOutput, Input, Output, Component

# Custom imports below
import os
import base64
import shutil
import tempfile


class RunFileAnalyzer(insightconnect_plugin_runtime.Action):
    tlp = {"WHITE": 0, "GREEN": 1, "AMBER": 2, "RED": 3}

    def __init__(self):
        super(self.__class__, self).__init__(
            name="run_file_analyzer",
            description=Component.DESCRIPTION,
            input=RunFileAnalyzerInput(),
            output=RunFileAnalyzerOutput(),
        )

    def run(self, params={}):
        api = self.connection.API

        analyzer_name = params.get(Input.ANALYZER_ID)
        file_content = base64.b64decode(params.get(Input.FILE))
        tlp_num = params.get(Input.ATTRIBUTES).get("tlp")
        filename = params.get(Input.ATTRIBUTES).get("filename") or "Not_Available"

        try:
            temp_dir = tempfile.mkdtemp()
            filename = os.path.basename(filename)
            file_path = os.path.join(temp_dir, filename)

            with open(file_path, "w+b") as f:
                f.write(file_content)

            job = None  # api.analyzers.run_by_name(
            #     analyzer_name, {"data": file_path, "dataType": "file", "tlp": tlp_num}, force=1
            # )
            # job = job_to_dict(job, api)

            shutil.rmtree(temp_dir)
        except Exception as e:
            raise PluginException(e)
        return {Output.JOB: job}
