import komand
from komand.exceptions import PluginException
from .schema import MassSearchAndPurgeInput, MassSearchAndPurgeOutput, Input, Output, Component
# Custom imports below
import subprocess
import os


class MassSearchAndPurge(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='mass_search_and_purge',
                description=Component.DESCRIPTION,
                input=MassSearchAndPurgeInput(),
                output=MassSearchAndPurgeOutput())

    def run(self, params={}):
        compliance_search_name = params.get(Input.COMPLIANCE_SEARCH_NAME)
        content_match_query = params.get(Input.CONTENT_MATCH_QUERY)
        timeout = params.get(Input.QUERY_TIMEOUT, 60)
        delete_items = params.get(Input.DELETE_ITEMS, False)

        self.logger.info(f"Searching mailboxes with query of: {content_match_query}")

        args = ['pwsh',
                '-ExecutionPolicy',
                'Unrestricted',
                '-File',
                '/powershell/Search-And-Destroy.ps1',
                '-Username',
                self.connection.username,
                '-Password',
                self.connection.password,
                '-ComplianceSearchName',
                compliance_search_name,
                '-ContentMatchQuery',
                content_match_query,
                '-TimeoutInMinutes',
                str(timeout),
                '-Office365URI',
                self.connection.o365_uri,
                '-DeleteItems',
                str(delete_items)]

        powershell = subprocess.Popen(args,
                                      cwd=os.getcwd(),
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE,
                                      universal_newlines=True)

        out, err = powershell.communicate()
        if err:
            self.logger.error(err)
            if out:
                self.logger.error(out)

            # This is a generic error message as there's a lot that can go wrong here.
            # Hopefully the above logs give us enough information to diagnose the problem
            raise PluginException(
                cause="PowerShell returned an error.",
                assistance="Please see the plugin logs for more information."
            )

        return {Output.SUCCESS: True}
        