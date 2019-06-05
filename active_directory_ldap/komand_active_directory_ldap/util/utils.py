import re


class ADUtils():

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

        # Ensure that commas are escaped
        for idx, value in enumerate(temp_list):
            if '\,' not in value:
                temp_list[idx] = temp_list[idx].replace(',', '\,')

        # Re add the removed ,..= to temp  list strings then remove the unneeded comma
        try:
            for idx, value in enumerate(attribute):
                temp_list[idx + 1] = f'{value}{temp_list[idx+1]}'[1:]
        except IndexError:
            raise Exception(f'The input DN was invalid. Please double check input. Input was:{dn}')
        return temp_list
