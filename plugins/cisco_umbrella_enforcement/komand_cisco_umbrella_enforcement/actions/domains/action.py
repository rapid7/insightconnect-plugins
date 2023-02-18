import insightconnect_plugin_runtime
from .schema import DomainsInput, DomainsOutput, Input, Output

# Custom imports below


class Domains(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="domains",
            description="To gather the lists of domains already added to the shared customer’s domain list, run a GET request against the domains endpoint of the API",
            input=DomainsInput(),
            output=DomainsOutput(),
        )

    def run(self, params={}):
        request_domains = self.connection.client.get_domains()

        datas = request_domains.get("data")
        meta = request_domains.get("meta")
        domains = {"meta": {}, "data": []}

        domains["meta"]["limit"] = meta.get("limit")
        domains["meta"]["page"] = meta.get("page")

        if not meta.get("next"):
            meta["next"] = "false"

        if not meta.get("prev"):
            meta["prev"] = "false"

        domains["meta"] = meta

        for data in datas:
            domains["data"].append(
                {
                    "ID": data.get("id"),
                    "name": data.get("name"),
                    "lastSeenAt": data.get("lastSeenAt"),
                }
            )

        return {Output.DOMAINS: domains}
