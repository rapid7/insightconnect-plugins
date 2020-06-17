from unittest import TestCase
import komand_cisco_firepower.util.read_csv as read_csv

class TestReadCSV(TestCase):
    def test_read_csv(self):
        file_name = "../examples/report.csv"
        with open(file_name) as f:
            csv_string = f.read()

        fields, csv_dict = read_csv.read_csv(csv_string)

        expected_fields = ['asset_id', 'host_name', 'ip_address', 'mac_address', 'last_assessed_for_vulnerabilities', 'asset_riskscore', 'vulnerability_description', 'vulnerability_title', 'vulnerability_severity', 'vulnerability_riskscore']
        expected_records = 1289

        self.assertEqual(fields, expected_fields)
        self.assertEqual(expected_records, len(csv_dict))





