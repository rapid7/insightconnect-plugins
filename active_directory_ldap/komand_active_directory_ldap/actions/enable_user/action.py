import komand
from .schema import EnableUserInput, EnableUserOutput

# Custom imports below
from komand.exceptions import PluginException
from komand_active_directory_ldap.util.utils import ADUtils
from ldap3 import MODIFY_REPLACE


class EnableUser(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="enable_user",
            description="Enable a account",
            input=EnableUserInput(),
            output=EnableUserOutput(),
        )

    def run(self, params={}):
        formatter = ADUtils()
        conn = self.connection.conn
        dn = params.get("distinguished_name")
        dn, search_base = formatter.format_dn(dn)
        self.logger.info(f"Escaped DN {dn}")

        pairs = formatter.find_parentheses_pairs(dn)
        # replace ( and ) when they are part of a name rather than a search parameter
        if pairs:
            dn = formatter.escape_brackets_for_query(dn, pairs)

        self.logger.info(f"Search DN {dn}")

        conn.search(
            search_base=search_base,
            search_filter=f"(distinguishedName={dn})",
            attributes=["userAccountControl"],
        )
        results = conn.response
        dn_test = [d["dn"] for d in results if "dn" in d]
        try:
            dn_test[0]
        except Exception as ex:
            self.logger.error("The DN " + dn + " was not found")
            raise PluginException(cause="The DN was not found", assistance="The DN " + dn + " was not found") from ex
        user_list = [d["attributes"] for d in results if "attributes" in d]
        user_control = user_list[0]
        try:
            account_status = user_control["userAccountControl"]
        except Exception as ex:
            self.logger.error("The DN " + dn + " is not a user")
            raise PluginException(cause="The DN is not a user", assistance="The DN " + dn + " is not a user") from ex
        user_account_flag = 2
        account_status = account_status & ~user_account_flag

        conn.modify(dn, {"userAccountControl": [(MODIFY_REPLACE, [account_status])]})
        result = conn.result
        output = result["description"]

        if result["result"] == 0:
            return {"success": True}

        self.logger.error("failed: error message %s" % output)
        return {"success": False}
