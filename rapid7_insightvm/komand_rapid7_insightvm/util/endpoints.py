class Asset:

    @staticmethod
    def assets(console_url, asset_id=None):
        """
        Gets assets by site
        :param console_url: URL to the InsightVM console
        :param asset_id: ID of the asset with which to interact
        :return: pre-populated /api/3/assets
        """
        if asset_id:
            return f"{console_url}/api/3/assets/{asset_id}"
        else:
            return f"{console_url}/api/3/assets"

    @staticmethod
    def search(console_url):
        """
        Gets assets by site
        :param console_url: URL to the InsightVM console
        :return: pre-populated /api/3/assets/search
        """
        return f"{console_url}/api/3/assets/search"

    @staticmethod
    def asset_tags(console_url, asset_id, tag_id=None):
        """
        Gets asset tags
        :param console_url: URL to the InsightVM console
        :param asset_id: ID of the asset with which to interact
        :param tag_id: ID of the tag with which to interact
        :return: pre-populated /api/3/assets/{id}/tags
        """
        if tag_id:
            return f"{console_url}/api/3/assets/{asset_id}/tags/{tag_id}"
        else:
            return f"{console_url}/api/3/assets/{asset_id}/tags"

    @staticmethod
    def asset_software(console_url, asset_id):
        """
        Gets assets by site
        :param console_url: URL to the InsightVM console
        :param asset_id: ID of the asset with which to interact
        :return: pre-populated /api/3/assets/{id}/software
        """
        return f"{console_url}/api/3/assets/{asset_id}/software"


class AssetGroup:

    @staticmethod
    def asset_groups(console_url, asset_group_id=None):
        """
        Gets assets by site
        :param console_url: URL to the InsightVM console
        :param asset_group_id: ID of the site to get assets for
        :return: pre-populated GET /api/3/asset_groups
        """
        if asset_group_id:
            return f"{console_url}/api/3/asset_groups/{asset_group_id}"
        else:
            return f"{console_url}/api/3/asset_groups"

    @staticmethod
    def asset_group_assets(console_url, asset_group_id=None):
        """
        Gets assets by site
        :param console_url: URL to the InsightVM console
        :param asset_group_id: ID of the site to get assets for
        :return: pre-populated GET /api/3/asset_groups/{id}/assets
        """
        return f"{console_url}/api/3/asset_groups/{asset_group_id}/assets"

    @staticmethod
    def asset_group_search_criteria(console_url, asset_group_id):
        """
        Gets assets by site
        :param console_url: URL to the InsightVM console
        :param asset_group_id: ID of the asset group with which to interact
        :return: pre-populated /api/3/asset_groups/{id}/search_criteria
        """
        return f"{console_url}/api/3/asset_groups/{asset_group_id}/search_criteria"

    @staticmethod
    def asset_group_tags(console_url, asset_group_id, tag_id=None):
        """
        Gets assets by site
        :param console_url: URL to the InsightVM console
        :param asset_group_id: ID of the asset group with which to interact
        :param tag_id: ID of the tag with which to interact
        :return: pre-populated /api/3/asset_groups/{id}/tags
        """
        if tag_id:
            return f"{console_url}/api/3/asset_groups/{asset_group_id}/tags/{tag_id}"
        else:
            return f"{console_url}/api/3/asset_groups/{asset_group_id}/tags"


class Scan:

    @staticmethod
    def site_scans(console_url, site_id):
        """
        Site scans endpoint operations
        :param console_url: URL to the InsightVM console
        :param site_id: ID of the site to scan
        :return: pre-populated /api/3/sites/{id}/scans
        """
        return f"{console_url}/api/3/sites/{site_id}/scans"

    @staticmethod
    def scans(console_url, scan_id=None):
        """
        Scans endpoint operations
        :param console_url: URL to the InsightVM console
        :param scan_id: ID of the scan to obtain
        :return: pre-populated /api/3/scans
        """
        if scan_id:
            return f"{console_url}/api/3/scans/{scan_id}"
        else:
            return f"{console_url}/api/3/scans"

    @staticmethod
    def scan_status(console_url, scan_id, status):
        """
        Set the status of a scan
        :param console_url: URL to the InsightVM console
        :param scan_id: ID of the scan to update
        :param status: status to which the scan should be set
        :return: pre-populated /api/3/scans
        """
        return f"{console_url}/api/3/scans/{scan_id}/{status}"


class ScanEngine:

    @staticmethod
    def scan_engines(console_url, engine_id=None):
        """
        Engine endpoint operation
        :param console_url: URL to the InsightVM console
        :param engine_id: ID of an engine
        :return: pre-populated /api/3/engines/{id}
        """
        if engine_id:
            return f"{console_url}/api/3/scan_engines/{engine_id}"
        else:
            return f"{console_url}/api/3/scan_engines"

    @staticmethod
    def scan_engine_pools(console_url, engine_id):
        """
        Engine endpoint operation
        :param console_url: URL to the InsightVM console
        :param engine_id: ID of an engine
        :return: pre-populated /api/3/engines/{id}
        """
        return f"{console_url}/api/3/scan_engines/{engine_id}/scan_engine_pools"


class ScanEnginePool:

    @staticmethod
    def scan_engine_pools(console_url, engine_pool_id=None):
        """
        Engine pool endpoint operation
        :param console_url: URL to the InsightVM console
        :param engine_pool_id: ID of a scan engine pool
        :return: pre-populated /api/3/engines/{id}
        """
        if engine_pool_id:
            return f"{console_url}/api/3/scan_engine_pools/{engine_pool_id}"
        else:
            return f"{console_url}/api/3/scan_engine_pools"

    @staticmethod
    def scan_engine_pool_engines(console_url, engine_pool_id, engine_id=None):
        """
        Engine pool engine endpoint operation
        :param console_url: URL to the InsightVM console
        :param engine_pool_id: ID of a scan engine pool
        :param engine_id: ID of a scan engine
        :return: pre-populated /api/3/engines/{id}
        """
        if engine_id:
            return f"{console_url}/api/3/scan_engine_pools/{engine_pool_id}/engines/{engine_id}"
        else:
            return f"{console_url}/api/3/scan_engine_pools/{engine_pool_id}/engines"


class SharedSecret:

    @staticmethod
    def generate_shared_secret(console_url, time_to_live):
        """
        Generate a shared secret for scan engine pairing
        :param console_url: URL to the InsightVM console
        :param time_to_live: Time to live of the generated secret in seconds
        :return: pre-populated /data/admin/global/shared-secret?time-to-live=#{time_to_live}
        """
        return f"{console_url}/data/admin/global/shared-secret?time-to-live={time_to_live}"


class Site:

    @staticmethod
    def get_site_assets(console_url, site_id):
        """
        Gets assets by site
        :param console_url: URL to the InsightVM console
        :param site_id: ID of the site to get assets for
        :return: pre-populated GET /api/3/sites/{id}/assets
        """
        return f"{console_url}/api/3/sites/{site_id}/assets"

    @staticmethod
    def sites(console_url, site_id=None):
        """
        Gets assets by site
        :param console_url: URL to the InsightVM console
        :param site_id: ID of the site with which to interact
        :return: pre-populated /api/3/sites
        """
        if site_id:
            return f"{console_url}/api/3/sites/{site_id}"
        else:
            return f"{console_url}/api/3/sites"

    @staticmethod
    def site_tags(console_url, site_id, tag_id=None):
        """
        Gets assets by site
        :param console_url: URL to the InsightVM console
        :param site_id: ID of the site with which to interact
        :param tag_id: ID of the tag with which to interact
        :return: pre-populated /api/3/sites/{id}/tags
        """
        if tag_id:
            return f"{console_url}/api/3/sites/{site_id}/tags/{tag_id}"
        else:
            return f"{console_url}/api/3/sites/{site_id}/tags"

    @staticmethod
    def site_engine(console_url, site_id):
        """
        Gets assets by site
        :param console_url: URL to the InsightVM console
        :param site_id: ID of the site with which to interact
        :return: pre-populated /api/3/sites/{id}/scan_engine
        """
        return f"{console_url}/api/3/sites/{site_id}/scan_engine"

    @staticmethod
    def site_included_targets(console_url, site_id):
        """
        Updates included scan targets by site
        :param console_url: URL to the InsightVM console
        :param site_id: ID of the site with which to interact
        :return: pre-populated /api/3/sites/{id}/included_targets
        """
        return f"{console_url}/api/3/sites/{site_id}/included_targets"

    @staticmethod
    def site_excluded_targets(console_url, site_id):
        """
        Updates excluded scan targets by site
        :param console_url: URL to the InsightVM console
        :param site_id: ID of the site with which to interact
        :return: pre-populated /api/3/sites/{id}/excluded_targets
        """
        return f"{console_url}/api/3/sites/{site_id}/excluded_targets"

    @staticmethod
    def site_included_asset_groups(console_url, site_id):
        """
        Updates included scan asset groups by site
        :param console_url: URL to the InsightVM console
        :param site_id: ID of the site with which to interact
        :return: pre-populated /api/3/sites/{id}/included_targets
        """
        return f"{console_url}/api/3/sites/{site_id}/included_asset_groups"

    @staticmethod
    def site_excluded_asset_groups(console_url, site_id):
        """
        Updates excluded scan asset groups by site
        :param console_url: URL to the InsightVM console
        :param site_id: ID of the site with which to interact
        :return: pre-populated /api/3/sites/{id}/excluded_targets
        """
        return f"{console_url}/api/3/sites/{site_id}/excluded_asset_groups"


class Tag:

    @staticmethod
    def tags(console_url, tag_id=None):
        """
        Interacts with base tags/specific tag endpoints
        :param console_url: URL to the InsightVM console
        :param tag_id: ID of the tag with which to interact
        :return: pre-populated /api/3/tags endpoint
        """
        if tag_id:
            return f"{console_url}/api/3/tags/{tag_id}"
        else:
            return f"{console_url}/api/3/tags"

    @staticmethod
    def tag_assets(console_url, tag_id, asset_id=None):
        """
        Interacts with tag assets endpoint
        :param console_url: URL to the InsightVM console
        :param tag_id: ID of the tag with which to interact
        :param asset_id: ID of the asset with which to interact
        :return: pre-populated /api/3/tags{id}/assets endpoint
        """
        if asset_id:
            return f"{console_url}/api/3/tags/{tag_id}/assets/{asset_id}"
        else:
            return f"{console_url}/api/3/tags/{tag_id}/assets"

    @staticmethod
    def tag_asset_groups(console_url, tag_id, asset_group_id=None):
        """
        Interacts with tag asset groups endpoint
        :param console_url: URL to the InsightVM console
        :param tag_id: ID of the tag to retrieve
        :param asset_group_id: ID of the asset group with which to interact
        :return: pre-populated /api/3/tags{id}/asset_groups endpoint
        """
        if asset_group_id:
            return f"{console_url}/api/3/tags/{tag_id}/asset_groups/{asset_group_id}"
        else:
            return f"{console_url}/api/3/tags/{tag_id}/asset_groups"

    @staticmethod
    def tag_sites(console_url, tag_id, site_id=None):
        """
        Interacts with tag sites endpoint
        :param console_url: URL to the InsightVM console
        :param tag_id: ID of the tag to retrieve
        :param site_id: ID of the site with which to interact
        :return: pre-populated /api/3/tags{id}/sites endpoint
        """
        if site_id:
            return f"{console_url}/api/3/tags/{tag_id}/sites/{site_id}"
        else:
            return f"{console_url}/api/3/tags/{tag_id}/sites"

    @staticmethod
    def tag_search_criteria(console_url, tag_id):
        """
        Interacts with tag search criteria endpoint
        :param console_url: URL to the InsightVM console
        :param tag_id: ID of the tag with which to interact
        :return: pre-populated /api/3/tags{id}/search_criteria endpoint
        """
        return f"{console_url}/api/3/tags/{tag_id}/search_criteria"


class VulnerabilityResult:

    @staticmethod
    def vulnerabilities_for_asset(console_url, asset_id):
        """
        Gets vulnerabilities found on an asset
        :param console_url: URL to the InsightVM console
        :param asset_id: ID of the asset to assess for vulnerabilities
        :return: pre-populated GET /api/3/assets/{id}/vulnerabilities
        """
        return f"{console_url}/api/3/assets/{asset_id}/vulnerabilities"


class Administration:

    @staticmethod
    def get_info(console_url):
        """
        Returns system details, including host and version information.
        :param console_url: URL to the InsightVM console
        :return: pre-populated GET /api/3/administration/info
        """
        return f"{console_url}/api/3/administration/info"


class Report:

    @staticmethod
    def create(console_url):
        return f"{console_url}/api/3/reports"

    @staticmethod
    def generate(console_url, report_id):
        return f"{console_url}/api/3/reports/{report_id}/generate"

    @staticmethod
    def status(console_url, report_id, instance_id):
        return f"{console_url}/api/3/reports/{report_id}/history/{instance_id}"

    @staticmethod
    def delete(console_url, report_id):
        return f"{console_url}/api/3/reports/{report_id}"

    @staticmethod
    def download(console_url, report_id, instance_id):
        """
        Returns the contents of a generated report. The report content is usually returned in a GZip compressed format.
        :param console_url: URL to the InsightVM console
        :param report_id: The identifier of the report
        :param instance_id: The identifier of the report instance
        :return: file
        """
        return f"{console_url}/api/3/reports/{report_id}/history/{instance_id}/output"

    @staticmethod
    def list_reports(console_url, page, size, sort):
        """
        Returns the contents of a generated report. The report content is usually returned in a GZip compressed format.
        :param console_url: URL to the InsightVM console
        :param name: The name of the report
        :param page: The index of the page (zero-based) to retrieve
        :param size: The number of records per page to retrieve
        :param sort: The criteria to sort the records by
        :return: array of report_id objects
        """
        # The criteria to sort the records by, in the format: property[,ASC|DESC]
        s = {"Ascending": "ASC", "Descending": "DESC"}
        return f"{console_url}/api/3/reports?page={page}&size={size}&sort={s[sort]}"


class Vulnerability:

    @staticmethod
    def vulnerability(console_url, vulnerability_id):
        """
        Gets assets affected by the vulnerability ID
        :param console_url: URL to the InsightVM console
        :param vulnerability_id: ID of the vulnerability to find assets for
        :return: pre-populated GET /api/3/vulnerabilities/{id}
        """
        return f"{console_url}/api/3/vulnerabilities/{vulnerability_id}"

    @staticmethod
    def solution(console_url, vulnerability_id):
        """
        Gets assets affected by the vulnerability ID
        :param console_url: URL to the InsightVM console
        :param vulnerability_id: ID of the vulnerability to find assets for
        :return: pre-populated GET /api/3/vulnerabilities/{id}
        """
        return f"{console_url}/api/3/solutions/{vulnerability_id}"
   
    @staticmethod
    def vuln_solution(console_url, vulnerability_id):
        """
        Gets assets affected by the vulnerability ID
        :param console_url: URL to the InsightVM console
        :param vulnerability_id: ID of the vulnerability to find assets for
        :return: pre-populated GET /api/3/vulnerabilities/{id}
        """
        return f"{console_url}/api/3/vulnerabilities/{vulnerability_id}/solutions"

    @staticmethod
    def vulnerability_affected_assets(console_url, vulnerability_id):
        """
        Gets assets affected by the vulnerability ID
        :param console_url: URL to the InsightVM console
        :param vulnerability_id: ID of the vulnerability to find assets for
        :return: pre-populated GET /api/3/vulnerabilities/{id}/assets
        """
        return f"{console_url}/api/3/vulnerabilities/{vulnerability_id}/assets"

    @staticmethod
    def vulnerability_checks(console_url):
        """
        Gets assets affected by the vulnerability ID
        :param console_url: URL to the InsightVM console
        :return: pre-populated GET /api/3/vulnerability_checks
        """
        return f"{console_url}/api/3/vulnerability_checks"


class VulnerabilityException:

    @staticmethod
    def vulnerability_exceptions(console_url):
        """
        Interacts with all vulnerability exceptions
        :param console_url: URL to the InsightVM console
        :return: pre-populated GET /api/3/vulnerability_exceptions
        """
        return f"{console_url}/api/3/vulnerability_exceptions"

    @staticmethod
    def vulnerability_exception(console_url, id):
        """
        Interacts with a single vulnerability exception
        :param console_url: URL to the InsightVM console
        :parm id: optional sort order for results
        :return: pre-populated GET /api/3/vulnerability_exceptions
        """
        return f"{console_url}/api/3/vulnerability_exceptions/{id}"

    @staticmethod
    def vulnerability_exception_expiration(console_url, id):
        """
        Interacts with vulnerability exception expiration
        :param console_url: URL to the InsightVM console
        :parm id: optional sort order for results
        :return: pre-populated GET /api/3/vulnerability_exceptions
        """
        return f"{console_url}/api/3/vulnerability_exceptions/{id}/expires"

    @staticmethod
    def vulnerability_exception_status(console_url, id, status):
        """
        Update vulnerability exception status
        :param console_url: URL to the InsightVM console
        :parm id: optional sort order for results
        :return: pre-populated POST /api/3/vulnerability_exceptions
        """
        return f"{console_url}/api/3/vulnerability_exceptions/{id}/{status}"


class User:

    @staticmethod
    def users(console_url, user_id=None):
        """
        Interacts with users endpoint
        :param console_url: URL to the InsightVM console
        :param user_id: ID of the user with which to interact
        :return: pre-populated /api/3/users endpoint
        """
        if user_id:
            return f"{console_url}/api/3/users/{user_id}"
        else:
            return f"{console_url}/api/3/users"

    @staticmethod
    def user_asset_groups(console_url, user_id, asset_group_id=None):
        """
        Interacts with users endpoint
        :param console_url: URL to the InsightVM console
        :param user_id: ID of the user with which to interact
        :param asset_group_id: ID of the asset group with which to interact
        :return: pre-populated /api/3/users/{user_id}/asset_groups endpoint
        """
        if asset_group_id:
            return f"{console_url}/api/3/users/{user_id}/asset_groups/{asset_group_id}"
        else:
            return f"{console_url}/api/3/users/{user_id}/asset_groups"

    @staticmethod
    def user_sites(console_url, user_id, site_id=None):
        """
        Interacts with users endpoint
        :param console_url: URL to the InsightVM console
        :param user_id: ID of the user with which to interact
        :param site_id: ID of the site with which to interact
        :return: pre-populated /api/3/users/{user_id}/asset_groups endpoint
        """
        if site_id:
            return f"{console_url}/api/3/users/{user_id}/sites/{site_id}"
        else:
            return f"{console_url}/api/3/users/{user_id}/sites"


class AuthenticationSource:

    @staticmethod
    def authentication_sources(console_url, authentication_source_id=None):
        """
        Interacts with users endpoint
        :param console_url: URL to the InsightVM console
        :param authentication_source_id: ID of the authentication source with which to interact
        :return: pre-populated /api/3/authentication_sources endpoint
        """
        if authentication_source_id:
            return f"{console_url}/api/3/authentication_sources/{authentication_source_id}"
        else:
            return f"{console_url}/api/3/authentication_sources"


class Role:

    @staticmethod
    def roles(console_url, role_id=None):
        """
        Interacts with users endpoint
        :param console_url: URL to the InsightVM console
        :param role_id: ID of the role with which to interact
        :return: pre-populated /api/3/roles endpoint
        """
        if role_id:
            return f"{console_url}/api/3/roles/{role_id}"
        else:
            return f"{console_url}/api/3/roles"
