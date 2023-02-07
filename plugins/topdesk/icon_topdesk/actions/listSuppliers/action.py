import insightconnect_plugin_runtime
from .schema import ListSuppliersInput, ListSuppliersOutput, Input, Output, Component

# Custom imports below
from icon_topdesk.util.helpers import clean


class ListSuppliers(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="listSuppliers",
            description=Component.DESCRIPTION,
            input=ListSuppliersInput(),
            output=ListSuppliersOutput(),
        )

    def run(self, params: dict) -> dict:
        self.logger.info(f"Getting suppliers with parameters: {params}.\n")
        parameters = {
            "start": params.get(Input.START),
            "page_size": params.get(Input.PAGESIZE),
            "query": params.get(Input.QUERY),
        }
        return {Output.SUPPLIERS: self.connection.api_client.get_suppliers(clean(parameters))}
