import komand
from .schema import DomainsInput, DomainsOutput
# Custom imports below


class Domains(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='domains',
                description='To gather the lists of domains already added to the shared customer’s domain list, run a GET request against the domains endpoint of the API',
                input=DomainsInput(),
                output=DomainsOutput())

    def run(self, params={}):
        try:
            requestDomains = self.connection.api.get_domains()
        except Exception:
            self.logger.error("Domains: run: Problem with request")
            raise Exception("Domains: run: Problem with request")
        datas = requestDomains.get("data")
        meta = requestDomains.get("meta")
        domains = {"meta": {}, "data": []}

        domains["meta"]["limit"] = meta.get("limit")
        domains["meta"]["page"] = meta.get("page")

        if meta.get("next") == False:
            meta["next"] = "false"

        if meta.get("prev") == False:
            meta["prev"] = "false"

        domains["meta"] = meta

        for data in datas:
            domains["data"].append({
                "ID": data.get("id"),
                "name": data.get("name"),
                "lastSeenAt": data.get("lastSeenAt")
            })

        return domains

    def test(self):
        return {"meta": {"next": "", "prev": "", "limit": 0, "page": 0}, "data": []}
