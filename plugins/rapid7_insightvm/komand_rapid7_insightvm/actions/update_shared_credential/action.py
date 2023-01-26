import json
from json import JSONDecodeError

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import UpdateSharedCredentialInput, UpdateSharedCredentialOutput, Input, Output, Component
from ...util import endpoints
from ...util.resource_requests import ResourceRequests
from ...util.util import check_not_null, check_in_enum, make_payload


class UpdateSharedCredential(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='update_shared_credential',
            description=Component.DESCRIPTION,
            input=UpdateSharedCredentialInput(),
            output=UpdateSharedCredentialOutput())

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        endpoint = endpoints.Site.site_excluded_asset_groups(self.connection.console_url, params.get(Input.ID))

        account = params.get("account")
        # check that account is in a json format
        try:
            account = json.loads(account)
        except JSONDecodeError:
            print("Please confirm that the account input is in a correct json format")

        description = params.get("description", "")
        host_restriction = params.get("host_restriction", None)
        id = params.get("id", None)
        name = check_not_null(params.get("name"))
        port_restriction = params.get("port_restriction", None)
        site_assignment = params.get("site_assignment", "")
        check_in_enum(site_assignment, ["all-sites", "specific-sites"])

        if site_assignment is "all-sites":
            sites = None
        else:
            sites = check_not_null(params.get("sites"))

        account_input = {}
        service = check_not_null(account.get("service"))
        if service in ("as400", "cifs", "cvs"):
            domain = account.get("domain", "")
            username = check_not_null(account.get("username"))
            password = check_not_null(account.get("password"))
            account_input = {"domain": domain, "username": username, "password": password}
        elif service == "cifshash":
            domain = account.get("domain", "")
            username = check_not_null(account.get("username"))
            ntlm_hash = check_not_null(account.get("ntlm_hash"))
            account_input = {"domain": domain, "username": username, "ntlmHash": ntlm_hash}
        elif service in ("db2", "mysql", "postgresql"):
            database = account.get("database", "")
            username = check_not_null(account.get("username"))
            password = check_not_null(account.get("password"))
            account_input = {"database": database, "username": username, "password": password}
        elif service in ("ftp", "pop", "remote-exec", "telnet"):
            username = check_not_null(account.get("username"))
            password = check_not_null(account.get("password"))
            account_input = {"username": username, "password": password}
        elif service == "http":
            realm = account.get("realm", "")
            username = check_not_null(account.get("username"))
            password = check_not_null(account.get("password"))
            account_input = {"realm": realm, "username": username, "password": password}
        elif service in ("ms-sql", "sybase"):
            database = account.get("database", "")
            username = check_not_null(account.get("username"))
            password = check_not_null(account.get("password"))
            use_windows_authentication = account.get("use_windows_authentication", False)
            if use_windows_authentication is True:
                domain = check_not_null(account.get("domain"))
                account_input = {"database": database, "domain": domain, "username": username, "password": password}
            else:
                account_input = {"database": database, "username": username, "password": password}
        elif service == "notes":
            notes_id_password = check_not_null(account.get("notes_id_password"))
            account_input = {"notesIDPassword": notes_id_password}
        elif service == "oracle":
            sid = account.get("sid", "")
            username = check_not_null(account.get("username"))
            password = check_not_null(account.get("password"))
            enumerate_sids = account.get("enumerate_sids", False)
            oracle_listener_password = account.get("oracle_listener_password", "")
            account_input = {"sid": sid, "enumerateSids": enumerate_sids, "username": username, "password": password,
                             "oracleListenerPassword": oracle_listener_password}
        elif service == "snmp":
            community_name = check_not_null(account.get("community_name"))
            account_input = {"communityName": community_name}
        elif service == "snmpv3":
            authentication_type = check_not_null(account.get("authentication_type"))
            check_in_enum(authentication_type, ["no-authentication", "md5", "sha"])
            username = check_not_null(account.get("username"))
            password = check_not_null(account.get("password"))
            privacy_type = account.get("privacy_type", "")
            if privacy_type not in ("", None):
                check_in_enum(privacy_type,
                              ["no-privacy", "des", "aes-128", "aes-192", "aes-192-with-3-des-key-extension",
                               "aes-256", "aes-265-with-3-des-key-extension"])
            privacy_password = account.get("privacy_password", "")
            if authentication_type is "no-authentication" and privacy_type is "no-privacy" and privacy_password is "":
                raise PluginException(
                    cause="privacy_password is required when authentication_type is no-authentication and privacy_type is no-privacy",
                    assistance="enter privacy_password"
                )
            account_input = {"authenticationType": authentication_type, "privacyType": privacy_type,
                             "username": username, "password": password}
        elif service == "ssh":
            username = check_not_null(account.get("username"))
            password = check_not_null(account.get("password"))
            permission_elevation = account.get("permission_elevation", "none")
            check_in_enum(permission_elevation, ["none", "sudo", "sudosu", "su", "pbrun", "privileged-exec"])
            permission_elevation_username = account.get("permission_elevation_username")
            permission_elevation_password = account.get("permission_elevation_password")
            account_input = {"username": username, "password": password, "permissionElevation": permission_elevation,
                             "permissionElevationUsername": permission_elevation_username,
                             "permissionElevationPassword": permission_elevation_password}

        elif service == "ssh-key":
            username = check_not_null(account.get("username"))
            private_key_password = check_not_null(account.get("private_key_password"))
            pem_key = check_not_null(account.get("pem_key"))
            permission_elevation = account.get("permission_elevation", "none")
            check_in_enum(permission_elevation, ["none", "sudo", "sudosu", "su", "pbrun", "privileged-exec"])
            permission_elevation_username = account.get("permission_elevation_username")
            permission_elevation_password = account.get("permission_elevation_password")
            account_input = {"username": username, "privateKeyPassword": private_key_password, "pemKey": pem_key,
                             "permissionElevation": permission_elevation,
                             "permissionElevationUsername": permission_elevation_username,
                             "permissionElevationPassword": permission_elevation_password}

        payload = make_payload(account_input, description, host_restriction, id, name, port_restriction,
                               site_assignment, sites)
        response = resource_helper.resource_request(endpoint=endpoint, method="put", payload=payload)

        return {"links": response["links"]}
