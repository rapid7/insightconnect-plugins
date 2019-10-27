import komand
from .schema import LookupUrlInput, LookupUrlOutput, Input, Component

# Custom imports below


class LookupUrl(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="lookup_url",
            description=Component.DESCRIPTION,
            input=LookupUrlInput(),
            output=LookupUrlOutput(),
        )

    def run(self, params={}):
        try:
            url = params.get(Input.URL)
            fields = params.get(Input.FIELDS)
            comment = params.get(Input.COMMENT)
            if not len(fields):
                fields = None
            if not len(comment):
                comment = None

            url_report = self.connection.client.lookup_url(
                url=url, fields=fields, comment=comment
            )
            if url_report.get("warnings", False):
                self.logger.info(
                    'Option for fields are: ["sightings","threatLists","analystNotes","counts","entity","hashAlgorithm","intelCard","metrics", "relatedEntities" ,"risk" ,"timestamps"]'
                )

            return komand.helper.clean(url_report["data"])

        except Exception as e:
            self.logger.error("Error: " + str(e))
            return {}
