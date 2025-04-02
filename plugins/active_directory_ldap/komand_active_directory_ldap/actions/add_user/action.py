import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
from .schema import AddUserInput, AddUserOutput, Output, Input
from komand_active_directory_ldap.util.utils import ADUtils


class AddUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_user",
            description="Adds the AD User specified",
            input=AddUserInput(),
            output=AddUserOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        domain_name = params.get(Input.DOMAIN_NAME)
        first_name = params.get(Input.FIRST_NAME)
        last_name = params.get(Input.LAST_NAME)
        logon_name = params.get(Input.LOGON_NAME)
        user_ou = params.get(Input.USER_OU)
        account_disabled = params.get(Input.ACCOUNT_DISABLED)
        password = params.get(Input.PASSWORD)
        additional_parameters = params.get(Input.ADDITIONAL_PARAMETERS)
        user_principal_name = params.get(Input.USER_PRINCIPAL_NAME)
        # END INPUT BINDING - DO NOT REMOVE

        if account_disabled or not self.connection.use_ssl:
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

        try:
            return {
                Output.SUCCESS: self.connection.client.add_user(
                    dn,
                    user_account_control,
                    self.connection.use_ssl,
                    password,
                    parameters,
                )
            }
        except PluginException:
            self.logger.info("Escaping non-ascii characters...")
            return {
                Output.SUCCESS: self.connection.client.add_user(
                    ADUtils.escape_non_ascii_characters(dn),
                    user_account_control,
                    self.connection.use_ssl,
                    password,
                    parameters,
                )
            }
