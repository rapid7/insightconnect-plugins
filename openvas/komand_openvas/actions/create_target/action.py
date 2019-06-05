import komand
from .schema import CreateTargetInput, CreateTargetOutput
# Custom imports below
import sys
import ipaddress
from openvas_lib import VulnscanTargetError


class CreateTarget(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_target',
                description='Create a new target in the OpenVAS server',
                input=CreateTargetInput(),
                output=CreateTargetOutput())

    def validateIPAddressRange(self, host_range):
        if '::' in host_range:
            raise ValueError('Cannot parse ranges for IPv6 addresses.' + host_range)
        breakdown = host_range.split('.')
        for index,value in enumerate(breakdown):
            if index != (len(breakdown)-1) and '-' in value:
                raise ValueError('Error creating target: IP address range is not in correct format'
                                 ' (dash only allowed in the last octet).' + str(i))

        newbreakdown = host_range.split('-')
        if len(newbreakdown) != 2:
            raise ValueError("IP range should not have multiple dash characters." + host_range)
        firstIP = newbreakdown[0]
        lastIPLastOctet = newbreakdown[1]
        newbreakdown = firstIP.split('.')
        if len(newbreakdown) != 4:
            raise ValueError('IP address should have only 4 octets.' + host_range)
        firstIPLastOctet = newbreakdown[3]
        for j in range(int(firstIPLastOctet),(int(lastIPLastOctet) + 1)):
            IPtoTest = newbreakdown[0] + '.' + newbreakdown[1] + '.' + newbreakdown[2] + '.' + str(j)
            try:
                ipaddress.ip_address(IPtoTest)
            except ValueError:
                raise

    def validateIPList(self, host_list):
        for i in host_list:
            if '/' in i:
                try:
                    ipaddress.ip_network(i)
                except ValueError:
                    raise

            elif '-' in i and ',' in i:
                for j in i.split(','):
                    if '-' in j:
                        self.validateIPAddressRange(j)
                    else:
                        try:
                            ipaddress.ip_address(j)
                        except ValueError:
                            raise

            elif '-' in i and ',' not in i:
                self.validateIPAddressRange(i)

            elif '-' not in i and ',' in i:
                for j in i.split(','):
                    try:
                        ipaddress.ip_address(j)
                    except ValueError:
                        raise

            else:
                try:
                    ipaddress.ip_address(i)
                except ValueError:
                    raise

    def run(self, params={}):
        target_name = str(params.get('name'))
        host_list = list(params.get('host_list'))

        target_port_list_id = params.get('port_list_id')
        if target_port_list_id == None:
            target_port_list_id = "Default"
        else:
            target_port_list_id = str(target_port_list_id)

        try:
            self.validateIPList(host_list)
        except ValueError as err:
            self.logger.error('Error  trying to create target, IP not valid: ' + str(err))
            return{'target_id': '', 'success': False, 'message': 'Error  trying to create target, IP not valid: ' 
                                                                 + str(err)}

        try:
            target_id = self.connection.scanner.create_target(name=target_name, hosts=host_list, comment='',
                                                              port_list=target_port_list_id)
        except VulnscanTargetError as err:
            self.logger.error('Error creating target: ' + str(err))
            return{ 'target_id':'', 'success': False, 'message': 'Error creating target: ' + str(err) }
        except:
            self.logger.error('Error creating target: ' + ' | '.join([str(sys.exc_info()[0]),str(sys.exc_info()[1])]))
            return{'target_id': '', 'success': False,
                    'message': 'Error creating target: ' + ' | '.join([str(sys.exc_info()[0]),str(sys.exc_info()[1])])}

        return {'target_id': target_id, 'success': True, 'message': 'Successfully created target in the OpenVAS server'}

    def test(self):
        """TODO: Test action"""
        return {}
