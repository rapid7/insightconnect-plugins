import komand
from .schema import UpdateInput, UpdateOutput
# Custom imports below


class Update(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='update',
                description='Update value by key',
                input=UpdateInput(),
                output=UpdateOutput())

    def run(self, params={}):
        update_key = params.get('key')
        update_value = params.get('value')

        if len(params.get('object')) > 0:
            _json = params.get('object')
            self.logger.info("User supplied an object to update")

        if len(params.get('array')) > 0:
            _json = params.get('array')
            self.logger.info("User supplied an array of objects to update")

        self.logger.info('Object Input: %s', _json)

        if isinstance(_json, dict):
            self.logger.info('Attempting object update')
            newdict = dict(_json)
            for k in _json.keys():
              # Find key user wants to update
              if k == update_key:
                 self.logger.info('Key found, updating its value')
                 # New assignment for key
                 newdict[k] = update_value
            return { "json": [newdict] }

        if isinstance(_json, list):
            self.logger.info('Attempting an array of objects update')
            l = []
            for d in _json:
                newdict = dict(d)
                for k in d.keys():
                    if k == update_key:
                        newdict[k] = update_value
                l.append(newdict)
            return { "json": l }

        self.logger.info('Something went wrong, could not update')
        return { "json": [{}] }

    def test(self):
        return { "json": [{ "Test": "Example" }] }
