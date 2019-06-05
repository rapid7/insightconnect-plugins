import komand
import ipcalc
from .schema import CalculateInput, CalculateOutput


class Calculate(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='calculate',
                description='Returns Subnet Information for IP and Netmask',
                input=CalculateInput(),
                output=CalculateOutput())

    def run(self, params={}):
        cidr = params.get('cidr')

        # Test for correct input
        try:
            subnet = ipcalc.Network(cidr)
        except:
            raise ValueError("Invalid Input")

        # Extract first octet from input
        address = cidr.split('/', 1)
        separate = cidr.split('.', 1)
        octet = int(separate[0])

        # Test if IP is is within class A, B, or C
        if octet < 128:
            bits = 8
            ip_class = 'A'
        elif octet < 192:
            bits = 16
            ip_class = 'B'
        elif octet < 224:
            bits = 24
            ip_class = 'C'
        else:
            raise ValueError('IP Resides in Reserved Range')
        # Error if an invalid mask is provided for the network class
        if int(subnet.subnet()) < bits:
            raise ValueError("Invalid Mask for Network Class")

        # Find first and last host address in subnet
        first = str(subnet.host_first())
        last = str(subnet.host_last())
        
        # Create variables to generate dic
        hosts = int(subnet.size() - 2) 
        subnet_id = str(subnet.network())
        host_range = "%s - %s" %(first, last)
        broadcast = str(subnet.broadcast())
        ip = address[0]
        netmask_bin = subnet.netmask()
        binary_netmask = netmask_bin.bin()
        netmask = str(subnet.netmask())
        netmask_split = netmask.split('.', 4)
        cidr_notation = "/%s" % address[1]

        # Calculate wildcard mask
        wildcard = []
        for i in netmask_split:
            wildcard.append(str(255 - int(i)))
        wildcard = '.'.join(wildcard)

        # Calculate number of subnets
        borrowed = int(subnet.subnet()) - bits
        subnets = 2 ** borrowed
        
        # Subnets should never return zero
        if subnets == 0:
            subnets = 1

        # Generate dic to return
        dic = {'ip': ip,
          'netmask': netmask,
          'wildcard': wildcard,
          'cidr': cidr_notation,
          'binary_netmask': binary_netmask,
          'ip_class': ip_class,
          'subnets': subnets,
          'hosts': hosts,
          'subnet_id': subnet_id,
          'host_range': host_range,
          'broadcast': broadcast
          }

        return dic

    def test(self):
        """TODO: Test action"""
        return {}
