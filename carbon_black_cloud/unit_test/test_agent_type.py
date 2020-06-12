from unittest import TestCase
import icon_carbon_black_cloud.util.agent_typer as agent_typer

class TestAgentType(TestCase):
    def test_agent_type(self):
        input_ip = "192.168.1.1"
        input_ip_v6 = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
        input_hostname = "foo-bar_pc1"
        input_mac_address = "00:0a:95:9d:68:16"
        input_device_id = "3365550"

        self.assertEqual(agent_typer.get_agent_type(input_ip), agent_typer.IP_ADDRESS)
        self.assertEqual(agent_typer.get_agent_type(input_ip_v6), agent_typer.IP_ADDRESS)
        self.assertEqual(agent_typer.get_agent_type(input_hostname), agent_typer.HOSTNAME)
        self.assertEqual(agent_typer.get_agent_type(input_mac_address), agent_typer.MAC_ADDRESS)
        self.assertEqual(agent_typer.get_agent_type(input_device_id), agent_typer.DEVICE_ID)
