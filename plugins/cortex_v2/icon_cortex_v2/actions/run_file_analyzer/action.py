import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import RunFileAnalyzerInput, RunFileAnalyzerOutput, Input, Output, Component

# Custom imports below
from icon_cortex_v2.util.util import filter_job, filter_job_artifacts
from os.path import basename, join
from json import dumps as dict_to_string
from base64 import b64decode as base64_decode
from tempfile import TemporaryDirectory
from magic import Magic as IdentifyMimeType


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
        file_content = base64_decode(params.get(Input.FILE))
        tlp_num = params.get(Input.ATTRIBUTES).get("tlp")
        filename = params.get(Input.ATTRIBUTES).get("filename", "Not_Available")

        with TemporaryDirectory() as temp_dir:
            filename = basename(filename)
            file_path = join(temp_dir, filename)
            with open(file_path, "w+b") as temp_file_w:
                temp_file_w.write(file_content)
            mime_type = IdentifyMimeType(mime=True).from_file(file_path)
            analyzer = api.get_analyzer_by_name(analyzer_name)
            analyzer_id = analyzer.get("id")
            if not analyzer_id:
                raise PluginException(f"Analyzer {analyzer_name} not found")
            with open(file_path, "rb") as temp_file_r:
                file_obj = (filename, temp_file_r, mime_type)
                data = dict_to_string({"dataType": "file", "tlp": tlp_num})
                job = filter_job(api.run_analyzer(analyzer_id=analyzer_id,
                                                  data={"_json": data},
                                                  files={"data": file_obj}))
                if not job or not isinstance(job, dict) or "id" not in job:
                    raise PluginException(f"Failed to receive job from analyzer {analyzer_name}")
                job["artifacts"] = filter_job_artifacts(api.get_job_artifacts(job["id"]))
                return {Output.JOB: job}
