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
            hash_id = params.get(Input.HASH)
            comment = params.get(Input.COMMENT)

            fields = [
                "analystNotes",
                "counts",
                "enterpriseLists",
                "entity",
                "intelCard",
                "metrics",
                "relatedEntities",
                "risk",
                "sightings",
                "threatLists",
                "timestamps",
                "hashAlgorithm"
            ]

            if not comment:
                comment = None

            hash_report = self.connection.client.lookup_hash(hash_id, fields=fields, comment=comment)

            return komand.helper.clean(hash_report["data"])

        except Exception as e:
            self.logger.error("Error: " + str(e))
