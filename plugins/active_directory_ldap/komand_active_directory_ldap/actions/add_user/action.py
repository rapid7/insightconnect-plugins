import komand
from .schema import AddUserInput, AddUserOutput
from komand.exceptions import PluginException

# Custom imports below
from ldap3 import extend
from ldap3 import MODIFY_REPLACE
from ldap3.core.exceptions import LDAPException


class AddUser(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_user",
            description="Adds the AD User specified",
            input=AddUserInput(),
            output=AddUserOutput(),
        )

    def run(self, params={}):
        conn = self.connection.conn
        ssl = self.connection.ssl
        domain_name = params.get("domain_name")
        first_name = params.get("first_name")
        last_name = params.get("last_name")
        logon_name = params.get("logon_name")
        user_ou = params.get("user_ou")
        account_disabled = params.get("account_disabled")
        password = params.get("password")
        additional_parameters = params.get("additional_parameters")
        user_principal_name = params.get("user_principal_name")

        if account_disabled or not ssl:
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
            dn = "CN={},CN={},DC={}".format(full_name, user_ou, domain_dn)
        else:
            dn = "CN={},OU={},DC={}".format(full_name, user_ou, domain_dn)

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
            conn.raise_exceptions = True
            conn.add(dn, ["person", "user"], parameters)
        except LDAPException as e:
            raise PluginException(
                cause="LDAP returned an error message.",
                assistance="Creating new user failed, error returned by LDAP.",
                data=e,
            )
        success = True

        if ssl:
            try:
                extend.ad_modify_password(conn, dn, password, None)
            except LDAPException:
                self.logger.error("User account created successfully, but unable to update the password.")
                success = False
        else:
            self.logger.info("Warning SSL is not enabled. User password can not be set. User account will be disabled")

        change_uac_attribute = {"userAccountControl": (MODIFY_REPLACE, [user_account_control])}
        conn.modify(dn, change_uac_attribute)
        self.logger.info(conn.result)

        return {"success": success}
