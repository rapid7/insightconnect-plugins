import komand
from .schema import DomainTagsInput, DomainTagsOutput
# Custom imports below


class DomainTags(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='domain_tags',
                description='Returns the date range when the domain being queried was a part of the Umbrella block list',
                input=DomainTagsInput(),
                output=DomainTagsOutput())

    def run(self, params={}):
        domain = params.get('domain')
        try:
            domain_tags = self.connection.investigate.domain_tags(domain)
        except Exception as e:
            self.logger.error("DomainTags: Run: Problem with request")
            raise e

        if not domain_tags:
            self.logger.info("DomainTags: Run: No results")
            return []

        domains = []
        for tag in domain_tags:
            url = ""
            if tag.get("url"):
                url = tag.get("url")
            domains.append({"begin": tag.get("period").get('begin'), "end": tag.get("period").get('end'), "category": tag.get("category"), "url": url })
        return {"domain_tags": domains}

    def test(self):
        return {"domain_tags": []}
