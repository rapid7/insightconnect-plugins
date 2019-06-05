import komand
from .schema import BlacklistByContentHashInput, BlacklistByContentHashOutput, Input, Output
# Custom imports below


class BlacklistByContentHash(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='blacklist_by_content_hash',
                description='Add hashed content to global blacklist',
                input=BlacklistByContentHashInput(),
                output=BlacklistByContentHashOutput())

    def run(self, params={}):
        hash_value = params.get(Input.HASH)
        result = self.connection.blacklist_by_content_hash(hash_value)
        result_data = result.get('data')
        new_result = {
            'blacklist_data': result_data
        }
        return {Output.RESULT: new_result}
