import re
from komand.exceptions import PluginException


class ADUtils:

    @staticmethod
    def dn_normalize(dn: str) -> str:
        """
        This method normalizes dn keys so that inputs are not case sensitive
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
        if dn[0] == ' ':
            dn = dn[:0] + '\\ ' + dn[1:]
        length = len(dn)-1
        if dn[length] == ' ':
            dn = dn[:length] + '\\ '

        dn_list = re.split(r',..=', dn)
        attribute = re.findall(r',..=', dn)

        # Ensure that special characters and non ascii characters are escaped
        character_list = [',', '#', '+', '<', '>', ';', '"']
        non_ascii_list = {'á': '\\E1', 'é': '\\E9', 'í': '\\ED', 'ó': '\\F3', 'ú': '\\FA', 'ñ': '\\F1'}

        # These are legal characters that some times need to be escaped and sometimes do not
        # We make the use escape them correctly in their inputs if they want to use them
        manual_escape = ['*', '=']

        for idx, value in enumerate(dn_list):
            # Escape special characters
            if value[0] == ' ':
                value = value[:0] + '\\ ' + value[1:]
            length = len(value) - 1
            if value[length] == ' ':
                value = value[:length] + '\\ '

            for escaped_char in character_list:
                if f'\\{escaped_char}' not in value:
                    dn_list[idx] = dn_list[idx].replace(escaped_char, f'\\{escaped_char}')
            # Escape non ascii characters
            for non_ascii_char, escaped_char in non_ascii_list.items():
                dn_list[idx] = dn_list[idx].replace(non_ascii_char, escaped_char)
        # escape \\ as needed
        for idx, value in enumerate(dn_list):
            location = value.find('\\')
            if not value[location + 1] in character_list and location != -1 and not value[location + 1] in manual_escape and not value[location + 1] == '\\':
                dn_list[idx] = dn_list[idx][:location] + "\\\\" + dn_list[idx][location + 1:]

        # Re add the removed ,..= to dn_list strings then remove the unneeded comma
        try:
            for idx, value in enumerate(attribute):
                dn_list[idx + 1] = f'{value}{dn_list[idx+1]}'[1:]
        except PluginException as e:
            raise PluginException(cause='The input DN was invalid. ',
                                  assistance='Please double check input. Input was:{dn}') from e
        return dn_list

    @staticmethod
    def find_search_base(dn_list: list) -> str:
        """
        This method will find a search base from a dn_list
        :param dn_list:
        :return: Will return a properly formatted search base
        """
        dc_list = [s for s in dn_list if 'DC' in s]
        search_base = ','.join(dc_list)
        return search_base

    def format_dn(self, dn: str) -> tuple:
        """
        This method takes a dn and preforms all needed operations to make it ready for use with ldap
        :param dn: A dn
        :return: Will return a properly formatted dn and search base as a tuple
        """
        dn = self.dn_normalize(dn)
        dn_list = self.dn_escape_and_split(dn)
        search_base = self.find_search_base(dn_list)
        formatted_dn = ','.join(dn_list)
        return formatted_dn, search_base

    @staticmethod
    def unescape_asterisk(dn: str) -> str:
        """
        This method takes a dn with escaped asterisks and unescapes them
        :param dn: A dn
        :return: returns the unescaped dn
        """
        dn = dn.replace('\\*', '*')
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
            if char == '(':
                temp_stack.append(idx)
            elif char == ')':
                if len(temp_stack) == 0:
                    raise PluginException(cause="No matching closing parentheses at: " + str(idx))
                pairs[temp_stack.pop()] = idx

        if len(temp_stack) > 0:
            raise PluginException(cause="No matching opening parentheses at: " + str(temp_stack.pop()))

        return pairs

    @staticmethod
    def escape_brackets_for_query(query: str, pairs: dict) -> str:
        """
        This method will properly escape a query
        :param query: The string to evaluate
        :param pairs: indexes of the start and end of brackets
        :return: An escaped query
        """
        for key, value in pairs.items():
            temp_string = query
            if temp_string.find('\\=', key, value) == -1:
                query = query[:value] + '\\29' + query[value + 1:]
                query = query[:key] + '\\28' + query[key + 1:]
        return query
