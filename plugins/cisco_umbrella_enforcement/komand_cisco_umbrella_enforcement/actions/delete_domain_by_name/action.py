import insightconnect_plugin_runtime
from .schema import DeleteDomainByNameInput, DeleteDomainByNameOutput, Input, Output

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
        domain_name = params.get(Input.NAME)

        result = self.connection.client.delete_event(name=domain_name)

        if result == "":
            return {Output.SUCCESS: True}
