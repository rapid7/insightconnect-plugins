from .base import ViperBase


class Compressor(ViperBase):
    pathName = 'compressor/'

    def __init__(self, config, **data):
        super().__init__(config)
        self.cls_name = data.get('cls_name')
        self.title = data.get('title')
        self.extensions = data.get('extensions')
        self.password = data.get('password')

    def __str__(self):
        return self.title

    @classmethod
    def all(cls, config):
        results = super(Compressor, cls)._get_results(config, cls.pathName)
        compressors = []
        for result in results:
            compressors.append(Compressor(config, **result).dump())
        return compressors

    def dump(self):
        return {
            "cls_name": self.cls_name,
            "title": self.title,
            "extensions": self.extensions,
            "password": self.password
        }
