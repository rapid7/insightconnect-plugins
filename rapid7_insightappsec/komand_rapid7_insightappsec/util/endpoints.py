class ScanConfig:

    @staticmethod
    def scan_config(console_url: str):
        """
        URI for all scan_config operations
        :param console_url: URL to the InsightAppSec console
        :return: pre-populated ias/v1/scan-configs/
        """
        return f'{console_url}ias/v1/scan-configs/'


class Scans:

    @staticmethod
    def scans(console_url: str):
        """
        URI for scans operations
        :param console_url: URL to the InsightAppSec console
        :return: pre-populated ias/v1/scans/
        """
        return f'{console_url}ias/v1/scans/'

    @staticmethod
    def scan_action(console_url: str, scan_id: str):
        """
        URI for scans action operations
        :param console_url: URL to the InsightAppSec console
        :param scan_id: The UUID of the scan
        :return: pre-populated ias/v1/scans/{scan_id}/action/
        """
        return f'{console_url}ias/v1/scans/{scan_id}/action/'

    @staticmethod
    def scan_engine_events(console_url: str, scan_id: str):
        """
        URI for scans action operations
        :param console_url: URL to the InsightAppSec console
        :param scan_id: The UUID of the scan
        :return: pre-populated ias/v1/scans/{scan_id}/engine-events/
        """
        return f'{console_url}ias/v1/scans/{scan_id}/engine-events/'

    @staticmethod
    def scan_execution_details(console_url: str, scan_id: str):
        """
        URI for scans action operations
        :param console_url: URL to the InsightAppSec console
        :param scan_id: The UUID of the scan
        :return: pre-populated ias/v1/scans/{scan_id}/execution-details/
        """
        return f'{console_url}ias/v1/scans/{scan_id}/execution-details/'

    @staticmethod
    def scan_platform_events(console_url: str, scan_id: str):
        """
        URI for scans action operations
        :param console_url: URL to the InsightAppSec console
        :param scan_id: The UUID of the scan
        :return: pre-populated ias/v1/scans/{scan_id}/platform-events/
        """
        return f'{console_url}ias/v1/scans/{scan_id}/platform-events/'

class Schedule:

    @staticmethod
    def get_schedules(console_url: str):
        """
        URI for a page of all Schedules
        :param console_url: URL to the InsightAppSec console
        :return: pre-populated ias/v1/schedules/
        """
        return f'{console_url}ias/v1/schedules/'

    @staticmethod
    def create_schedule(console_url: str):
        """
        URI to schedule the scan of a scan_config
        :param console_url: URL to the IAS console
        """
        return f'{console_url}ias/v1/schedules/'
