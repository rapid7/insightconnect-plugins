import insightconnect_plugin_runtime
from .schema import UpdateSharedCredentialInput, UpdateSharedCredentialOutput, Input, Output, Component
from ...util import endpoints
from ...util.resource_requests import ResourceRequests
from ...util.update_shared_credential_util import *
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
        endpoint = endpoints.SharedCredential.update_shared_credential(self.connection.console_url,
                                                                       params.get(Input.ID))
        account = params.get("account")
        description = params.get("description", "")
        host_restriction = params.get("host_restriction", "")
        id_ = check_not_null(params, "id")
        name = check_not_null(params, "name")
        port_restriction = params.get("port_restriction", "")
        site_assignment = check_not_null(params, "site_assignment")
        check_in_enum(site_assignment, "site_assignment", ["all-sites", "specific-sites"])
        if site_assignment == "all-sites":
            sites = None
        else:
            sites = check_not_null(params, "sites")

        service = check_not_null(account, "service")
        service_dict = {"as400": as400_cifs_cvs, "cifs": as400_cifs_cvs, "cvs": as400_cifs_cvs, "cifshash": cifshash,
                        "ftp": ftp_pop_remote_exec_telnet, "pop": ftp_pop_remote_exec_telnet, "oracle": oracle,
                        "db2": db2_mysql_postgresql, "mysql": db2_mysql_postgresql, "postgresql": db2_mysql_postgresql,
                        "remote-exec": ftp_pop_remote_exec_telnet, "telnet": ftp_pop_remote_exec_telnet, "snmp": snmp,
                        "http": http, "ms-sql": ms_sql_sybase, "sybase": ms_sql_sybase, "notes": notes,
                        "snmpv3": snmpv3, "ssh": ssh, "ssh-key": ssh_key}

        account_input = service_dict[service](account, service)
        payload = make_payload(account_input, description, host_restriction, id_, name, port_restriction,
                               site_assignment, sites)
        response = resource_helper.resource_request(endpoint=endpoint, method="put", payload=payload)

        return {"links": response["links"]}
