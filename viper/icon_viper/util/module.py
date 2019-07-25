from .base import ViperBase


class Module(ViperBase):
    pathName = 'module/'

    def __init__(self, config, **data):
        super().__init__(config)
        self.name = data.get('name')
        self.description = data.get('description')

    def __str__(self):
        return self.name

    @classmethod
    def all(cls, config):
        results = super(Module, cls)._get_results(config, cls.pathName)
        modules = []
        for result in results:
            modules.append(Module(config, **result).dump())
        return modules

    def dump(self):
        return {
            "name": self.name,
            "description": self.description
        }
