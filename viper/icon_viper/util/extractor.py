from .base import ViperBase


class Extractor(ViperBase):
    pathName = 'extractor/'

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
        results = super(Extractor, cls)._get_results(config, cls.pathName)
        extractors = []
        for result in results:
            extractors.append(Extractor(config, **result).dump())
        return extractors

    def dump(self):
        return {
            "cls_name": self.cls_name,
            "title": self.title,
            "extensions": self.extensions,
            "password": self.password
        }
