import re
from komand.exceptions import PluginException


class ADUtils:

    @staticmethod
    def dn_normalize(dn):
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
    def dn_escape_and_split(dn):
        """
        This method will split a dn into it's component peaces and then escape the needed characters
        :param dn:
        :return: Will return a list of the dn component peaces
        """
        dn_list = re.split(r',..=', dn)
        attribute = re.findall(r',..=', dn)

        # Ensure that special characters are escaped
        character_list = ['\\', ',', '#', '+', '<', '>', ';', '"', '/']
        for idx, value in enumerate(dn_list):
            for escaped_char in character_list:
                if f'\{escaped_char}' not in value:
                    dn_list[idx] = dn_list[idx].replace(escaped_char, f'\{escaped_char}')

        # Re add the removed ,..= to temp  list strings then remove the unneeded comma
        try:
            for idx, value in enumerate(attribute):
                dn_list[idx + 1] = f'{value}{dn_list[idx+1]}'[1:]
        except PluginException as e:
            raise PluginException(cause='The input DN was invalid. ',
                                  assistance='Please double check input. Input was:{dn}') from e
        return dn_list

    @staticmethod
    def users_container_handling(dn_list: list):
        """
        This method handles the fact the default 'Users' container in AD is not infect a OU but a container which is called differently
        :param dn_list: A dn_list created by the 'dn_escape_and_split' method
        :return: A corrected dn_list for the User container
        """

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
