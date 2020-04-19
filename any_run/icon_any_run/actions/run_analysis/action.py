import insightconnect_plugin_runtime
from .schema import RunAnalysisInput, RunAnalysisOutput, Input, Output, Component
# Custom imports below
import base64
from insightconnect_plugin_runtime.exceptions import PluginException


class RunAnalysis(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='run_analysis',
            description=Component.DESCRIPTION,
            input=RunAnalysisInput(),
            output=RunAnalysisOutput())

    def run(self, params={}):
        files = None
        if params.get(Input.OBJ_TYPE) and \
                params.get(Input.OBJ_TYPE) != 'file' and \
                Input.FILE in params and params.get(Input.FILE).get('content'):
            raise PluginException(cause='Invalid input', assistance='Send file only possible with type "file"')
        if params.get(Input.OBJ_TYPE) == 'file' and Input.OBJ_URL in params:
            raise PluginException(cause='Invalid input',
                                  assistance='Send file from url only possible with type "url" or "download"')
        if params.get(Input.OBJ_TYPE) != 'url' and Input.OBJ_EXT_BROWSER in params:
            raise PluginException(cause='Invalid input',
                                  assistance='Browser name only possible with type "url"')
        if params.get(Input.OBJ_TYPE) != 'download' and (
                Input.OBJ_EXT_USERAGENT in params or Input.OPT_PRIVACY_HIDESOURCE in params):
            raise PluginException(cause='Invalid input',
                                  assistance='User agent only possible with type "download"')

        if params.get(Input.OBJ_TYPE) == 'file' and Input.FILE in params and params.get(Input.FILE).get('content'):
            file = params.get(Input.FILE)
            files = {'file': (file.get('filename'), base64.decodebytes(file.get('content').encode('ascii')))}

        if params.get(Input.FILE):
            params.pop(Input.FILE)
        task_result = self.connection.any_run_api.run_analysis(params, files)
        return {
            Output.UUID: task_result.get("data", {}).get('taskid', None)
        }
