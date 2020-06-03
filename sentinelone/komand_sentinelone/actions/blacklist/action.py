import komand
from .schema import BlacklistInput, BlacklistOutput, Input, Output, Component
# Custom imports below


class Blacklist(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='blacklist',
                description=Component.DESCRIPTION,
                input=BlacklistInput(),
                output=BlacklistOutput())

    def run(self, params={}):
        blacklist_state = params.get(Input.BLACKLIST_STATE)
        if blacklist_state is True:
            errors = self.connection.create_blacklist_item(
                params.get(Input.HASH),
                params.get(Input.DESCRIPTION, "Hash Blacklisted from InsightConnect")
            )
            success_result = len(errors) == 0
        else:
            item_ids = self.connection.get_item_ids_by_hash(params.get(Input.HASH))
            result = self.connection.delete_blacklist_item_by_hash(item_ids)
            success_result = result.get("data", {}).get("affected") == len(item_ids)

        return {
            Output.SUCCESS: success_result
        }
