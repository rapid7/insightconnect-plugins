from .base import ViperBase


class Tag(ViperBase):
    pathName = 'project/{project_name}/tag/'

    def __init__(self, config, project_name, **data):
        super().__init__(config)
        self.project_name = project_name
        self.id = data.get('id')
        self.tag = data.get('tag')

    def __str__(self):
        return self.tag

    def save(self):
        data = {'tag': self.tag}
        url = self.pathName.format(project_name=self.project_name) + str(self.id) + "/"
        super()._put(self.config, url, data)

    def delete(self):
        url = self.pathName.format(project_name=self.project_name) + str(self.id) + "/"
        super()._delete(self.config, url)

    def dump(self):
        return {
            "project_name": self.project_name,
            "id": self.id,
            "tag": self.tag
        }
