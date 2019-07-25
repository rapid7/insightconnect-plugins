import base64
from .base import ViperBase
from .analysis import Analysis
from .note import Note
from .tag import Tag
from .malware import Malware
from komand.exceptions import PluginException


class Project(ViperBase):
    pathName = 'project/'

    def __init__(self, config, name):
        super().__init__(config)
        self.name = name

    def __str__(self):
        return self.name

    @classmethod
    def get(cls, config, name):
        response = super(Project, cls)._get(config, f'{cls.pathName}{name}')

        if 'data' not in response:
            raise PluginException(cause='Error: Received an unexpected response. Please verify your Viper server '
                            'status and try again. ', assistance='If the issue persists please contact support.')

        data = response['data']
        return Project(config, data['name']).dump()

    @classmethod
    def all(cls, config):
        response = super(Project, cls)._get(config, cls.pathName)
        results = response['results']
        projects = []
        for result in results:
            if 'data' not in result:
                break

            data = result['data']
            projects.append(Project(config, data['name']).dump())
        return projects

    @classmethod
    def create(cls, config, name):
        data = {'name': name}
        response = super(Project, cls)._post(config, cls.pathName, data)

        if 'data' not in response:
            raise PluginException(cause='Error: Received an unexpected response. Please verify your Viper server '
                            'status and try again. ', assistance='If the issue persists please contact support.')

        data = response['data']
        return Project(config, data.get('name')).dump()

    def list_analyses(self):
        results = self._get_results(self.config, self.pathName + self.name + '/analysis/')
        analyses = []
        for result in results:
            if 'data' not in result:
                break

            data = result['data']
            analyses.append(Analysis(self.config, self.name, None, **data).dump())
        return analyses

    def get_analysis(self, id):
        response = super()._get(self.config, self.pathName + self.name + '/analysis/' + str(id) + "/")

        if 'data' not in response:
            raise PluginException(cause='Error: Received an unexpected response. Please verify your Viper server '
                            'status and try again. ', assistance='If the issue persists please contact support.')

        data = response['data']
        return Analysis(self.config, self.name, None, **data).dump()

    def list_notes(self):
        results = self._get_results(self.config, self.pathName + self.name + '/note/')
        notes = []
        for result in results:
            if 'data' not in result:
                break

            data = result['data']
            notes.append(Note(self.config, self.name, None, **data).dump())
        return notes

    def get_note(self, id):
        response = super()._get(self.config, self.pathName + self.name + '/note/' + str(id) + "/")

        if 'data' not in response:
            raise PluginException(cause='Error: Received an unexpected response. Please verify your Viper server '
                            'status and try again. ', assistance='If the issue persists please contact support.')

        data = response['data']
        return Note(self.config, self.name, None, **data)

    def list_tags(self):
        results = self._get_results(self.config, self.pathName + self.name + '/tag/')
        tags = []
        for result in results:
            if 'data' not in result:
                break

            data = result['data']
            tags.append(Tag(self.config, self.name, **data).dump())
        return tags

    def get_tag(self, id):
        response = super()._get(self.config, self.pathName + self.name + '/tag/' + str(id) + "/")

        if 'data' not in response:
            raise PluginException(cause='Error: Received an unexpected response. Please verify your Viper server '
                            'status and try again. ', assistance='If the issue persists please contact support.')

        data = response['data']
        return Tag(self.config, self.name, **data)

    def list_malware(self):
        results = self._get_results(self.config, self.pathName + self.name + '/malware/')
        malware = []
        for result in results:
            if 'data' not in result:
                break

            data = result['data']
            malware.append(Malware(self.config, self.name, **data).dump())
        return malware

    def get_malware(self, sha256):
        response = super()._get(self.config, self.pathName + self.name + '/malware/' + sha256 + "/")

        if 'data' not in response:
            raise PluginException(cause='Error: Received an unexpected response. Please verify your Viper server '
                            'status and try again. ', assistance='If the issue persists please contact support.')

        data = response['data']
        return Malware(self.config, self.name, **data)

    def upload_malware(self, file, extractor=None, tag_list=None, archive_pass=None, store_archive=None,
                       note_title=None, note_body=None, file_name=None):
        files = {"file": "{}".format(file.get("filename"), base64.b64decode(file.get("content")))}
        data = {}

        if extractor:
            data['extractor'] = extractor
        if tag_list:
            data['tag_list'] = ' '.join(str(x) for x in tag_list)
        if archive_pass:
            data['archive_pass'] = archive_pass
        if store_archive:
            data['store_archive'] = store_archive
        if note_title:
            data['note_title'] = note_title
        if note_body:
            data['note_body'] = note_body
        if file_name:
            data['file_name'] = file_name

        url = self.pathName + self.name + '/malware/upload/'
        results = super()._post(self.config, url, data, files)

        malware = []
        for result in results:
            if 'data' not in result:
                break

            data = result['data']
            malware.append(Malware(self.config, self.name, **data).dump())
        return malware

    def dump(self):
        return {
            "name": self.name
        }
