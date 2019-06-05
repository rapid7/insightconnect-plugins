import komand
from .schema import GetAllDomainUsersInput, GetAllDomainUsersOutput, Input
# Custom imports below


class GetAllDomainUsers(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_all_domain_users',
                description='Get all domain users',
                input=GetAllDomainUsersInput(),
                output=GetAllDomainUsersOutput())

    def run(self, params={}):
        domain = params.get(Input.DOMAIN)
        service = self.connection.service

        # Call the Admin SDK Directory API
        self.logger.info("Fetching users...")
        request = service.users().list(domain=domain, orderBy="email")

        # Get all users
        users = []
        while request is not None:
            result = request.execute()
            users += result.get('users') or []
            request = service.users().list_next(request, result)

        if len(users) == 0:
            return {"users": []}

        # Format output
        formatted_users = []
        for user in users:
            email = user.get("primaryEmail", "")
            if "name" in user:
                name = user["name"].get("fullName", "")
            else:
                name = ""

            formatted_users.append({
                "email": email,
                "name": name
            })

        return {"users": formatted_users}
