from .base import ViperBase
from komand.exceptions import PluginException


class Analysis(ViperBase):
    pathName = 'project/{project_name}/malware/{malware_sha256}/analysis/'

    def __init__(self, config, project_name, malware_sha256, **data):
        super().__init__(config)
        self.project_name = project_name
        self.malware_sha256 = malware_sha256
        self.id = data.get('id')
        self.cmd_line = data.get('cmd_line')
        self.stored_at = data.get('stored_at')
        self.results = data.get('results')

    def __str__(self):
        return str(self.id)

    def delete(self):
        if self.malware_sha256 is None:
            raise PluginException(cause="Error: ", assistance="Deleting an Analysis is not supported in this context.")

        url = self.pathName.format(
            project_name=self.project_name, malware_sha256=self.malware_sha256) + str(self.id) + "/"
        super()._delete(self.config, url)

    def dump(self):
        return {
            "id": self.id,
            "project_name": self.project_name,
            "malware_sha256": self.malware_sha256,
            "cmd_line": self.cmd_line,
            "stored_at": self.stored_at,
            "results": self.results
        }
