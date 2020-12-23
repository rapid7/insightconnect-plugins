class Apps:

    @staticmethod
    def get_apps(console_url: str):
        """
        URI for all App operations
        :param console_url: URL to the InsightAppSec console
        :return: pre-populated ias/v1/apps/
        """
        return f'{console_url}ias/v1/apps/'

    @staticmethod
    def create_app(console_url: str):
        """
        URI for all App operations
        :param console_url: URL to the InsightAppSec console
        :return: pre-populated ias/v1/apps/
        """
        return f'{console_url}ias/v1/apps/'

    @staticmethod
    def get_app(console_url: str, app_id: str):
        """
        URI for all App operations
        :param console_url: URL to the InsightAppSec console
        :return: pre-populated ias/v1/apps/UUID/
        """
        return f'{console_url}ias/vi/apps/{app_id}/'

    @staticmethod
    def update_app(console_url: str, app_id: str):
        """
        URI for all App operations
        :param console_url: URL to the InsightAppSec console
        :return: pre-populated ias/v1/apps/UUID/
        """
        return f'{console_url}ias/v1/apps/{app_id}/'

    @staticmethod
    def delete_app(console_url: str, app_id: str):
        """
        URI for all App operations
        :param console_url: URL to the InsightAppSec console
        :return: pre-populated ias/v1/apps/UUID/
        """
        return f'{console_url}ias/vi/apps/{app_id}/'

    @staticmethod
    def get_app_users(console_url: str, app_id: str):
        """
        URI for all App operations
        :param console_url: URL to the InsightAppSec console
        :return: pre-populated ias/v1/apps/UUID/users/
        """
        return f'{console_url}ias/vi/apps/{app_id}/users/'

    @staticmethod
    def add_app_user(console_url: str, app_id: str):
        """
        URI for all App operations
        :param console_url: URL to the InsightAppSec console
        :return: pre-populated ias/v1/apps/UID/users/
        """
        return f'{console_url}ias/vi/apps/{app_id}/users/'

    @staticmethod
    def remove_app_user(console_url: str, app_id: str, user_id: str):
        """
        URI for all App operations
        :param console_url: URL to the InsightAppSec console
        :return: pre-populated ias/v1/apps/UUID/users/UUID/
        """
        return f'{console_url}ias/vi/apps/{app_id}/users/{user_id}/'


class AttackTemplates:
    def get_attack_templates(console_url: str):
        """
        URI for all attack template operations
        :param console_url: URL to the InsightAppSec console
        :return: pre-populated ias/v1/attack-templates/
        """
        return f'{console_url}ias/vi/attack-templates/'

    def get_attack_template(console_url: str, attack_template_id: str):
        """
        URI for all attack template operations
        :param console_url: URL to the InsightAppSec console
        :return: pre-populated ias/v1/attack-templates/UUID/
        """
        return f'{console_url}ias/vi/attack-templates/{attack_template_id}/'

class Blackouts:
    def get_blackouts(console_url: str):
        """
        URI for all blackout operations
        :param console_url: URL to the InsightAppSec console
        :return: pre-populated ias/v1/blackouts/
        """
        return f'{console_url}ias/vi/blackouts/'

    def create_blackout(console_url: str):
        """
        URI for all blackout operations
        :param console_url: URL to the InsightAppSec console
        :return: pre-populated ias/v1/blackouts/
        """
        return f'{console_url}ias/vi/blackouts/'

    def get_blackout(console_url: str, blackout_id: str):
        """
        URI for all blackout operations
        :param console_url: URL to the InsightAppSec console
        :return: pre-populated ias/v1/blackouts/UUID/
        """
        return f'{console_url}ias/vi/blackouts/{blackout_id}/'

    def update_blackout(concole_url: str, blackout_id: str):
        """
        URI for all blackout operations
        :param console_url: URL to the InsightAppSec console
        :return: pre-populated ias/v1/blackouts/UUID/
        """
        return f'{console_url}ias/vi/blackouts/{blackout_id}/'

    def delete_blackout(concole_url: str, blackout_id: str):
        """
        URI for all blackout operations
        :param console_url: URL to the InsightAppSec console
        :return: pre-populated ias/v1/blackouts/UUID/
        """
        return f'{console_url}ias/vi/blackouts/{blackout_id}/'


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
