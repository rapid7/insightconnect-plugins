import insightconnect_plugin_runtime
from .schema import DeleteDomainByNameInput, DeleteDomainByNameOutput

# Custom imports


class DeleteDomainByName(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_domain_by_name",
            description="Delete domain from user domain list",
            input=DeleteDomainByNameInput(),
            output=DeleteDomainByNameOutput(),
        )

    def run(self, params={}):
        domainName = params.get("domain")

        try:
            self.connection.client.delete_domains_by_name(domainName)
        except Exception:
            self.logger.error("DeleteDomainByName: run: Problem with request")
            raise Exception("DeleteDomainByName: run: Problem with request")

        return {"status": "success"}

    def test(self):
        return {"status": "success"}
