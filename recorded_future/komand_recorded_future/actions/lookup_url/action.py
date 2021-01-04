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
            comment = params.get(Input.COMMENT)

            fields = [
                "analystNotes",
                "counts",
                "enterpriseLists",
                "entity",
                "metrics",
                "relatedEntities",
                "risk",
                "sightings",
                "timestamps"
            ]

            if not len(comment):
                comment = None

            url_report = self.connection.client.lookup_url(
                url=url, fields=fields, comment=comment
            )

            return komand.helper.clean(url_report["data"])

        except Exception as e:
            self.logger.error("Error: " + str(e))
            return {}
