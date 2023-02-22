import insightconnect_plugin_runtime
from .schema import DeleteDomainByIdInput, DeleteDomainByIdOutput, Input, Output

# Custom imports below


class DeleteDomainById(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_domain_by_id",
            description="Delete domain from user domain list by ID",
            input=DeleteDomainByIdInput(),
            output=DeleteDomainByIdOutput(),
        )

    def run(self, params={}):
        ID = params.get(Input.ID)

        result = self.connection.client.delete_event(domain_id=ID)

        if result == "":
            return {Output.SUCCESS: True}
