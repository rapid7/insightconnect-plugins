import re
from typing import List, Optional
from ldap3.core.exceptions import LDAPInvalidDnError, LDAPOperationsErrorResult
from ldap3 import MODIFY_REPLACE
from insightconnect_plugin_runtime.exceptions import PluginException
from logging import Logger


class ADUtils:
    @staticmethod
    def escape_non_ascii_characters(input_string: str) -> str:
        non_ascii_list = {
            "á": "\\E1",
            "é": "\\E9",
            "í": "\\ED",
            "ó": "\\F3",
            "ú": "\\FA",
            "ñ": "\\F1",
        }

        for non_ascii, escaped_character in non_ascii_list.items():
            input_string = input_string.replace(non_ascii, escaped_character)
        return input_string

    @staticmethod
    def dn_normalize(dn: str) -> str:
        """
        This method normalizes dn keys so that inputs are not case-sensitive
        :param dn: A dn
        :return: A normalized dn
        """
        dn_params = ["cn=", "ou=", "dc="]
        for params in dn_params:
            if params in dn:
                dn = dn.replace(params, params.upper())
        return dn

    @staticmethod
    def dn_escape_and_split(dn: str) -> list:
        """
        This method will split a dn into it's component peaces and then escape the needed characters
        :param dn:
        :return: Will return a list of the dn component peaces
        """

        dn_list = re.split(r",..=", dn)
        attribute = re.findall(r",..=", dn)

        # Ensure that special characters and non ascii characters are escaped
        character_list = [",", "#", "+", "<", ">", ";", '"']

        # non_ascii_list = {
        #     "á": "\\E1",
        #     "é": "\\E9",
        #     "í": "\\ED",
        #     "ó": "\\F3",
        #     "ú": "\\FA",
        #     "ñ": "\\F1",
        # }
        # These are legal characters that sometimes need to be escaped and sometimes do not
        # We make the use escape them correctly in their inputs if they want to use them
        manual_escape = ["*", "="]

        for idx, value in enumerate(dn_list):
            # Escape special characters
            for escaped_char in character_list:
                if f"\\{escaped_char}" not in value:
                    dn_list[idx] = dn_list[idx].replace(
                        escaped_char, f"\\{escaped_char}"
                    )
        # escape \\ as needed
        for idx, value in enumerate(dn_list):
            location = value.find("\\")
            if (
                not value[location + 1] in character_list
                and location != -1
                and not value[location + 1] in manual_escape
                and not value[location + 1] == "\\"
            ):
                dn_list[idx] = (
                    dn_list[idx][:location] + "\\\\" + dn_list[idx][location + 1 :]
                )

        # Re add the removed ,..= to dn_list strings then remove the unneeded comma
        try:
            for idx, value in enumerate(attribute):
                dn_list[idx + 1] = f"{value}{dn_list[idx + 1]}"[1:]
        except PluginException as error:
            raise PluginException(
                cause="The input DN was invalid. ",
                assistance="Please double check input. Input was:{dn}",
            ) from error
        return dn_list

    @staticmethod
    def find_search_base(dn_list: list) -> str:
        """
        This method will find a search base from a dn_list
        :param dn_list:
        :return: Will return a properly formatted search base
        """
        dc_list = [s for s in dn_list if "DC" in s]
        search_base = ",".join(dc_list)
        return search_base

    @staticmethod
    def format_dn(dn: str) -> (str, str):
        """
        This method takes a dn and preforms all needed operations to make it ready for use with ldap
        :param dn: A dn
        :return: Will return a properly formatted dn and search base as a tuple
        """
        dn = ADUtils.dn_normalize(dn)
        dn_list = ADUtils.dn_escape_and_split(dn)
        search_base = ADUtils.find_search_base(dn_list)
        formatted_dn = ",".join(dn_list)
        return formatted_dn, search_base

    @staticmethod
    def unescape_asterisk(dn: str) -> str:
        """
        This method takes a dn with escaped asterisks and unescapes them
        :param dn: A dn
        :return: returns the unescaped dn
        """
        dn = dn.replace("\\*", "*")
        return dn

    @staticmethod
    def find_parentheses_pairs(query_string: str) -> dict:
        """
        This method will find and return the indexes for parentheses pairs
        :param query_string: The string to evaluate
        :return: A dictionary where the key/value pairs are the start and end to parentheses pairs
        """
        pairs = {}
        temp_stack = []

        for idx, char in enumerate(query_string):
            if char == "(":
                temp_stack.append(idx)
            elif char == ")":
                if len(temp_stack) == 0:
                    raise PluginException(
                        cause="No matching closing parentheses at: " + str(idx)
                    )
                pairs[temp_stack.pop()] = idx

        if len(temp_stack) > 0:
            raise PluginException(
                cause="No matching opening parentheses at: " + str(temp_stack.pop())
            )

        return pairs

    @staticmethod
    def find_characters_in_string(
        input_list_of_characters: List[str],
        input_string: str,
        start_index: Optional[int] = None,
        end_index: Optional[int] = None,
    ) -> bool:
        """
        This method will check if input_string contains any characters from a input_list_of_characters
        :param input_list_of_characters: List of characters to search for
        :param input_string: The string to evaluate
        :param start_index: Start index of input_string to begin searching characters for
        :param end_index: End index of input_string to begin searching characters for
        :return: Bool value indicates whether input_string contains any of characters (True) or not (False)
        """
        for character in input_list_of_characters:
            if input_string.find(character, start_index, end_index) >= 0:
                return True
        return False

    @staticmethod
    def escape_brackets_for_query(query: str) -> str:
        """
        This method will properly escape a query
        :param query: The string to evaluate
        :return: An escaped query
        """
        change = True
        while change:
            change = False
            pairs = ADUtils.find_parentheses_pairs(query)
            for key, value in pairs.items():
                if not ADUtils.find_characters_in_string(
                    ["=", ">", "<"], query, key, value
                ):
                    query = query[:value] + "\\29" + query[value + 1 :]
                    query = query[:key] + "\\28" + query[key + 1 :]
                    change = True
                    break
        return query

    @staticmethod
    def escape_user_dn(user_dn: str) -> str:
        return ADUtils.escape_brackets_for_query(user_dn)

    @staticmethod
    def check_user_dn_is_valid(conn, user_dn: str, search_base: str) -> bool:
        try:
            conn.search(
                search_base=search_base,
                search_filter=f"(distinguishedName={ADUtils.escape_user_dn(user_dn)})",
                attributes=["userAccountControl"],
            )
        except LDAPInvalidDnError as error:
            raise PluginException(
                cause="The DN was not found.",
                assistance=f"The DN {user_dn} was not found.",
                data=error,
            )
        except LDAPOperationsErrorResult as error:
            raise PluginException(
                preset=PluginException.Preset.SERVER_ERROR, data=error
            )
        return len([d["dn"] for d in conn.response if "dn" in d]) > 0

    @staticmethod
    def change_account_status(conn, dn: str, status: bool, logger: Logger) -> bool:
        dn, search_base = ADUtils.format_dn(dn)
        logger.info(f"Escaped DN {dn}")

        if not ADUtils.check_user_dn_is_valid(conn, dn, search_base):
            logger.error(f"The DN {dn} was not found")
            raise PluginException(
                cause=f"The DN {dn} was not found.",
                assistance="Please provide a valid DN and try again.",
            )
        user_list = [d["attributes"] for d in conn.response if "attributes" in d]
        user_control = user_list[0]
        try:
            account_status = user_control["userAccountControl"]
        except Exception as ex:
            logger.error("The DN " + dn + " is not a user")
            raise PluginException(
                cause=f"The DN {dn} is not a user object therefore it cannot be enabled or disabled.",
                assistance="Please provide a valid user object and try again.",
            ) from ex
        user_account_flag = 2
        if status:
            account_status = account_status & ~user_account_flag
        else:
            account_status = account_status | user_account_flag

        conn.modify(dn, {"userAccountControl": [(MODIFY_REPLACE, [account_status])]})
        if conn.result["result"] == 0:
            return True

        output = conn.result["description"]
        logger.error(f"failed: error message {output}")
        return False

    @staticmethod
    def change_useraccountcontrol_property(
        conn,
        dn: str,
        clear_flag_switch: bool,
        flags: int,
        logger: Logger,
    ) -> bool:
        # https://docs.microsoft.com/en-us/troubleshoot/windows-server/identity/useraccountcontrol-manipulate-account-properties
        # for list of flags
        dn, search_base = ADUtils.format_dn(dn)
        logger.info(f"Escaped DN {dn}")

        if not ADUtils.check_user_dn_is_valid(conn, dn, search_base):
            logger.error(f"The DN {dn} was not found")
            raise PluginException(
                cause=f"The DN {dn} was not found.",
                assistance="Please provide a valid DN and try again.",
            )
        user_list = [d["attributes"] for d in conn.response if "attributes" in d]

        if len(user_list) > 0:
            user_control = user_list[0]
        else:
            logger.error(f"The DN '{dn}' has no attributes")
            raise PluginException(
                cause=f"The DN '{dn}' is likely not a user object therefore it cannot be unlocked.",
                assistance="Please provide a valid user object and try again.",
            )

        try:
            account_status = user_control["userAccountControl"]
        except Exception as ex:
            logger.error(f"The DN '{dn}' is not a user")
            raise PluginException(
                cause=f"The DN '{dn}' is not a user object therefore the account status cannot be changed.",
                assistance="Please provide a valid user object and try again.",
            ) from ex

        if clear_flag_switch:
            account_status = account_status & ~flags
        else:
            account_status = account_status | flags

        conn.modify(dn, {"userAccountControl": [(MODIFY_REPLACE, [account_status])]})
        if conn.result["result"] == 0:
            return True

        output = conn.result["description"]
        logger.error(f"failed: error message {output}")
        return False


class UserAccountFlags:
    # Enum-Like Reference for different account flags in AD/LDAP
    SCRIPT = 1
    ACCOUNTDISABLE = 2
    HOMEDIR_REQUIRED = 8
    LOCKOUT = 16
    PASSWD_NOTREQD = 32
    PASSWD_CANT_CHANGE = 64  # can't be set as easy as the others
    ENCRYPTED_TEXT_PWD_ALLOWED = 128
    TEMP_DUPLICATE_ACCOUNT = 256
    NORMAL_ACCOUNT = 512
    INTERDOMAIN_TRUST_ACCOUNT = 2048
    WORKSTATION_TRUST_ACCOUNT = 4096
    SERVER_TRUST_ACCOUNT = 8192
    DONT_EXPIRE_PASSWORD = 65536
    MSN_LOGON_ACCOUNT = 131072
    PASSWORD_EXPIRED = 8388608
