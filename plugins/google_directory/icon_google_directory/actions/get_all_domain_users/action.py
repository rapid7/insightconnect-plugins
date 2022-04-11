import insightconnect_plugin_runtime
from .schema import GetAllDomainUsersInput, GetAllDomainUsersOutput, Input, Output, Component

# Custom imports below


class GetAllDomainUsers(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_all_domain_users",
            description=Component.DESCRIPTION,
            input=GetAllDomainUsersInput(),
            output=GetAllDomainUsersOutput(),
        )

    def run(self, params={}):
        service = self.connection.service
        self.logger.info("Fetching users...")
        request = service.users().list(domain=params.get(Input.DOMAIN), orderBy="email")

        users = []
        while request:
            result = request.execute()
            users += result.get("users", [])
            request = service.users().list_next(request, result)

        if users:
            formatted_users = []
            for user in users:
                formatted_users.append(
                    {"email": user.get("primaryEmail", ""), "name": user.get("name", {}).get("fullName", "")}
                )
            return {Output.USERS: formatted_users}
        return {Output.USERS: users}
