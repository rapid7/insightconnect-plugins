import dicttoxml
from komand_palo_alto_pan_os.util.log_helper import LogHelper


class SecurityPolicy:
    def __init__(self, logger=None):
        if logger:
            self.logger = logger
        else:
            self.logger = LogHelper().logger

    def extract_from_security_policy(self, policy: dict) -> dict:
        """
        Removes extraneous xml data from a current security policy so that it can be edited.
        :param policy: A PAN-OS security policy
        :return A new cleaner dictionary containing the polices current config.
        """
        key_list = ['source', 'destination', 'service',
                    'application', 'source-user', 'to',
                    'from', 'category', 'hip-profiles']
        output = {}
        for i in key_list:
            try:
                output[i] = policy['response']['result']['entry'][i]['member']
            except KeyError:
                self.logger.info('Current policy has no policy config: {}. Setting to any'.format(policy))
                output[i] = 'any'
        try:
            output['action'] = policy['response']['result']['entry']['action']
        except KeyError:
            self.logger.error('policy config: {}'.format(policy))
            raise Exception('Current policy config missing an action key.')

        for i in output:
            if isinstance(output[i], list):
                if isinstance(output[i][0], dict):
                    for k, val in enumerate(output[i]):
                        output[i][k] = val['#text']
            if isinstance(output[i], dict):
                if isinstance(output[i], dict) and '#text' in output[i]:
                    output[i] = output[i]['#text']

        return output

    def add_to_key(self, key, add: str):
        # Key can be a str or list
        """
        Adds new items to a current security policy key
        :param key: The key to add to. it may be a string list or a special string 'any'
        :param add: The string to add to the key, or in the case of the key being 'any' replace with
        :return The updated policy key
        """
        if add not in key:
            if isinstance(key, list):
                key.append(add)
            elif key and key != 'any':
                key = [key, add]
            else:
                key = add
        return key

    def remove_from_key(self, key, remove: str):
        # Key can be a str or list
        """
        Removes existing items to a current security policy key
        :param key: The key to remove from. it may be a string of a list or a special string 'any'
        :param remove: The string to remove from the key, or in the case of the key being 'any' to replace with
        :return The updated policy key
        """
        if remove in key:
            # If a list is reduced to len 1 it must be cast as a str. for 2 or more leave as list
            if isinstance(key, list) and len(key) > 3:
                key.remove(remove)
            elif isinstance(key, list):
                key.remove(remove)
                key = key[0]
            else:
                key = 'any'
            return key
        self.logger.error("{remove} was not found in {key}."
                          " {remove} will not be removed from policy.".format(remove=remove,
                                                                              key=key))
        return key

    def element_for_policy_update(self, rule_name, to, from_, source, destination,
                                  service, application, category, hip_profiles, source_user,
                                  fire_wall_action) -> str:
        """
        Builds the update policy dictionary into a xml string
        :param rule_name: Used to pass the name of the policy to be updated
        :param to: The new to list/str
        :param from_: The new from list/str
        :param source: The new source list/str
        :param destination: The new destination list/str
        :param service: The new service list/str
        :param application: The new application list/str
        :param category: The new category list/str
        :param hip_profiles: The new hip-profiles list/str
        :param source_user: The new source-user list/str
        :param fire_wall_action: The new fire_wall_action list/str
        :return A properly formatted xml file for the security policy
        """
        # Build dic for xml
        element = {'to': to, 'from': from_, 'source': source, 'destination': destination,
                   'service': service, 'application': application, 'category': category,
                   'hip-profiles': hip_profiles, 'source-user': source_user,
                   'action': fire_wall_action}

        for value in element:
            if not value == 'action' and isinstance(element[value], str):
                temp = element[value]
                element[value] = {'member': temp}

        element = dicttoxml.dicttoxml(element, attr_type=False, root=False)
        element = element.decode()
        element = element.replace('<item>', '<member>')
        element = element.replace('</item>', '</member>')
        element = '<entry name="{name}">{data}</entry>'.format(name=rule_name, data=element)
        self.logger.info('XML :{}'.format(element))
        return element


class ExternalList:
    def __init__(self, logger=None):
        if logger:
            self.logger = logger
        else:
            self.logger = LogHelper().logger

    def element_for_create_external_list(self, list_type: str, description: str,
                                         source: str, repeat: str, time: str, day: str) -> str:
        """
        Builds the update policy dictionary into a xml string
        :param list_type:
        :param description:
        :param source:
        :param certificate_profile:
        :param repeat:
        :param time:
        :param day:
        :return: A properly formatted xml file for the security policy
        """

        if repeat == 'daily':
            if not time:
                raise Exception('Time of day not defined')
            element = '<type><{list_type}>' \
                      '<recurring><daily><at>{time}</at></daily></recurring>' \
                      '<description>{description}</description>' \
                      '<url>{source}</url>' \
                      '</{list_type}></type>'.format(list_type=list_type,
                                                     time=time,
                                                     description=description,
                                                     source=source)
        elif repeat == 'weekly':
            if not time:
                raise Exception('Time of day not defined')
            if not day:
                raise Exception('Day of week not defined')
            element = '<type><{list_type}>' \
                      '<recurring><weekly><day-of-week>{day}</day-of-week>' \
                      '<at>{time}</at></weekly></recurring>' \
                      '<description>{description}</description>' \
                      '<url>{source}</url>' \
                      '</{list_type}></type>'.format(list_type=list_type,
                                                     day=day,
                                                     time=time,
                                                     description=description,
                                                     source=source)
        else:
            element = '<type><{list_type}>' \
                      '<recurring><{repeat}/></recurring>' \
                      '<description>{description}</description>' \
                      '<url>{source}</url>' \
                      '</{list_type}></type>'.format(list_type=list_type,
                                                     repeat=repeat,
                                                     description=description,
                                                     source=source)
        self.logger.info('XML :{}'.format(element))
        return element
