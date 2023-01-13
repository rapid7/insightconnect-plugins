import insightconnect_plugin_runtime
from .schema import UpdateSharedCredentialInput, UpdateSharedCredentialOutput, Input, Output, Component
# Custom imports below


class UpdateSharedCredential(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='update_shared_credential',
                description=Component.DESCRIPTION,
                input=UpdateSharedCredentialInput(),
                output=UpdateSharedCredentialOutput())

    def run(self, params={}):
        account = params.get("account")
        description = params.get("description", "")
        host_restriction = params.get("host_restriction", None)
        id = params.get("id", None)
        name = params.get("name")
        port_restriction = params.get("port_restriction", None)
        site_assignment = params.get("site_assignment")
        sites = params.get("sites", None)

        # service = account.get("service")
        # switch = {0: "as400", 1: "cifs", 2: "cifshash", 3: "cvs", 4: "db2"}
        # which_service = switch.get(service)
        # I want to make a switch case thing here to check what service the user chose, so we only collect the necessary
        # inputs
        # try calling a function and pass through the service to a switch case that calls a specific function to get our
        # specific inputs depending on which service it is. dunno if this is possible tho
        # if your just back from holiday and thinking that you forgot how to code, dw you never knew in the first place :D
        return {}
