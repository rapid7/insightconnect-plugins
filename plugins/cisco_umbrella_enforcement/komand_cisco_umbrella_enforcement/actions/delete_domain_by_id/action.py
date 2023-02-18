import insightconnect_plugin_runtime
from .schema import DeleteDomainByIdInput, DeleteDomainByIdOutput, Input, Output
from insightconnect_plugin_runtime.helper import clean

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
        result = clean(result)

        return {Output.STATUS: result}
