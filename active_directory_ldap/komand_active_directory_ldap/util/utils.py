import re

from komand.exceptions import PluginException


class ADUtils:

    @staticmethod
    def dn_normalize(dn):
        dn_params = ["cn=", "ou=", "dc="]
        for params in dn_params:
            if params in dn:
                dn = dn.replace(params, params.upper())
        return dn

    @staticmethod
    def dn_escape_and_split(dn):
        temp_list = re.split(r',..=', dn)
        attribute = re.findall(r',..=', dn)

        # Ensure that special characters are escaped
        character_list = ['\\', ',', '#', '+', '<', '>', ';', '"', '/']
        for idx, value in enumerate(temp_list):
            for escaped_char in character_list:
                if f'\{escaped_char}' not in value:
                    temp_list[idx] = temp_list[idx].replace(escaped_char, f'\{escaped_char}')

        # Re add the removed ,..= to temp  list strings then remove the unneeded comma
        try:
            for idx, value in enumerate(attribute):
                temp_list[idx + 1] = f'{value}{temp_list[idx+1]}'[1:]
        except PluginException as e:
            raise PluginException(cause='The input DN was invalid. ',
                                  assistance='Please double check input. Input was:{dn}') from e
        return temp_list

    @staticmethod
    def find_parentheses_pairs(query_string):
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
