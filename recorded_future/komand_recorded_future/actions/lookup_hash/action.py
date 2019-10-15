import komand
from .schema import LookupHashInput, LookupHashOutput, Input


class LookupHash(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="lookup_hash",
            description="This action is used to retrieve information about a specified hash",
            input=LookupHashInput(),
            output=LookupHashOutput(),
        )

    def run(self, params={}):
        try:
            hash_ID = params.get(Input.HASH)
            fields = params.get(Input.FIELDS)
            comment = params.get(Input.COMMENT)
            if not len(fields):
                fields = None
            if not comment:
                comment = None
            hash_report = self.connection.client.lookup_hash(hash_ID, fields=fields, comment=comment)
            if hash_report.get("warnings", False):
                self.logger.info(
                    'Option for fields are: ["sightings","threatLists","analystNotes","counts","entity","hashAlgorithm","intelCard","metrics", "relatedEntities" ,"risk" ,"timestamps"]'
                )

            return komand.helper.clean(hash_report["data"])

        except Exception as e:
            self.logger.error("Error: " + str(e))
