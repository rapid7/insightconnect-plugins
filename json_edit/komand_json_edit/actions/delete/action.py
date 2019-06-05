import komand
from .schema import DeleteInput, DeleteOutput
# Custom imports below


class Delete(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete',
                description='Delete a key by name',
                input=DeleteInput(),
                output=DeleteOutput())

    def run(self, params={}):
        update_key = params.get('key')

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
                 self.logger.info('Key found, deleting it')
                 # Delete key
                 del newdict[k]
            return { "json": [newdict] }

        if isinstance(_json, list):
            self.logger.info('Attempting an array of objects update')
            l = []
            for d in _json:
                newdict = dict(d)
                for k in d.keys():
                    if k == update_key:
                        self.logger.info('Key found, deleting it')
                        # Delete key
                        del newdict[k]
                l.append(newdict)
            return { "json": l }

        self.logger.info('Something went wrong, could not update')
        return { "json": [{}] }

    def test(self):
        return { "json": [{ "Test": "Example" }] }
