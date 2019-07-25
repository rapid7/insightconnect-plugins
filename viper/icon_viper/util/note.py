from .base import ViperBase
from komand.exceptions import PluginException


class Note(ViperBase):
    pathName = 'project/{project_name}/malware/{malware_sha256}/note/'

    def __init__(self, config, project_name, malware_sha256, **data):
        super().__init__(config)
        self.project_name = project_name
        self.malware_sha256 = malware_sha256
        self.id = data.get('id')
        self.title = data.get('title')
        self.body = data.get('body')

    def __str__(self):
        return self.title

    def save(self):
        if self.malware_sha256 is None:
            raise PluginException(cause='Error: ', assistance='Updating a Note is not supported in this context.')

        data = {'title': self.title, 'body': self.body}

        url = self.pathName.format(project_name=self.project_name, malware_sha256=self.malware_sha256) + str(self.id) + "/"
        super()._put(self.config, url, data)

    def add(self):
        if self.malware_sha256 is None:
            raise PluginException(cause='Error: ', assistance='Updating a Note is not supported in this context.')

        data = {'title': self.title, 'body': self.body}

        url = self.pathName.format(project_name=self.project_name, malware_sha256=self.malware_sha256)
        note = super()._post(self.config, url, data)

        if note.get("data") and note.get("data").get("id"):
            self.id = note.get("data").get("id")

    def delete(self):
        if self.malware_sha256 is None:
            raise PluginException(cause='Error: ', assistance='Deleting a Note is not supported in this context.')

        url = self.pathName.format(project_name=self.project_name, malware_sha256=self.malware_sha256) + str(self.id) + "/"
        super()._delete(self.config, url)

    def dump(self):
        return {
            "id": self.id,
            "project_name": self.project_name,
            "malware_sha256": self.malware_sha256,
            "title": self.title,
            "body": self.body,
        }
