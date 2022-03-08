import insightconnect_plugin_runtime
from .schema import RunFileAnalyzerInput, RunFileAnalyzerOutput

# Custom imports below
import os
import base64
import shutil
import tempfile
from icon_cortex_v2.util.convert import job_to_dict
from cortex4py.exceptions import ServiceUnavailableError, AuthenticationError, CortexException
from insightconnect_plugin_runtime.exceptions import ConnectionTestException


class RunFileAnalyzer(insightconnect_plugin_runtime.Action):
    tlp = {"WHITE": 0, "GREEN": 1, "AMBER": 2, "RED": 3}

    def __init__(self):
        super(self.__class__, self).__init__(
            name="run_file_analyzer",
            description="Run analyzers on a file",
            input=RunFileAnalyzerInput(),
            output=RunFileAnalyzerOutput(),
        )

    def run(self, params={}):
        api = self.connection.api

        analyzer_name = params.get("analyzer_id")
        file_content = base64.b64decode(params.get("file"))
        tlp_num = params.get("attributes").get("tlp")
        filename = params.get("attributes").get("filename") or "Not_Available"

        try:
            temp_dir = tempfile.mkdtemp()
            filename = os.path.basename(filename)
            file_path = os.path.join(temp_dir, filename)

            with open(file_path, "w+b") as f:
                f.write(file_content)

            job = api.analyzers.run_by_name(
                analyzer_name, {"data": file_path, "dataType": "file", "tlp": tlp_num}, force=1
            )
            job = job_to_dict(job, api)

            shutil.rmtree(temp_dir)
        except AuthenticationError as e:
            self.logger.error(e)
            raise ConnectionTestException(preset=ConnectionTestException.Preset.API_KEY)
        except ServiceUnavailableError as e:
            self.logger.error(e)
            raise ConnectionTestException(preset=ConnectionTestException.Preset.SERVICE_UNAVAILABLE)
        except CortexException as e:
            raise ConnectionTestException(cause="Failed to run analyzer.", assistance="{}.".format(e))

        return {"job": job}
