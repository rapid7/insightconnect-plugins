import insightconnect_plugin_runtime

# Custom imports below
from .schema import AddUserInput, AddUserOutput, Output, Input


class AddUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_user",
            description="Adds the AD User specified",
            input=AddUserInput(),
            output=AddUserOutput(),
        )

    def run(self, params={}):
        use_ssl = self.connection.use_ssl
        domain_name = params.get(Input.DOMAIN_NAME)
        first_name = params.get(Input.FIRST_NAME)
        last_name = params.get(Input.LAST_NAME)
        logon_name = params.get(Input.LOGON_NAME)
        user_ou = params.get(Input.USER_OU)
        account_disabled = params.get(Input.ACCOUNT_DISABLED)
        password = params.get(Input.PASSWORD)
        additional_parameters = params.get(Input.ADDITIONAL_PARAMETERS)
        user_principal_name = params.get(Input.USER_PRINCIPAL_NAME)

        if account_disabled or not use_ssl:
            user_account_control = 514
        else:
            user_account_control = 512

        full_name = first_name + " " + last_name
        domain_dn = domain_name.replace(".", ",DC=")
        if user_ou == "Users":
            user_ou = user_ou.replace(",", ",CN=")
        else:
            user_ou = user_ou.replace(",", ",OU=")
        if user_ou == "Users":
            dn = f"CN={full_name},CN={user_ou},DC={domain_dn}"
        else:
            dn = f"CN={full_name},OU={user_ou},DC={domain_dn}"

        self.logger.info("User DN=" + dn)

        parameters = {
            "givenName": first_name,
            "sn": last_name,
            "sAMAccountName": logon_name,
            "userPassword": password,
            "userPrincipalName": user_principal_name,
        }

        if additional_parameters:
            parameters.update(additional_parameters)
        log_parameters = parameters
        log_parameters.pop("userPassword")
        self.logger.info(log_parameters)
        return {
            Output.SUCCESS: self.connection.client.add_user(dn, user_account_control, use_ssl, password, parameters)
        }
