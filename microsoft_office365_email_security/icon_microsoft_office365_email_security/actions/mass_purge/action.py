import komand
from komand.exceptions import PluginException
from .schema import MassPurgeInput, MassPurgeOutput, Input, Output, Component
# Custom imports below
import subprocess
import os


class MassPurge(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='mass_purge',
                description=Component.DESCRIPTION,
                input=MassPurgeInput(),
                output=MassPurgeOutput())

    def run(self, params={}):
        compliance_search_name = params.get(Input.COMPLIANCE_SEARCH_NAME)
        timeout = params.get(Input.QUERY_TIMEOUT, 60)

        self.logger.info(f"Attempting to delete results of compliance search: {compliance_search_name}")

        powershell = subprocess.Popen(['pwsh',
                                       '-ExecutionPolicy',
                                       'Unrestricted',
                                       '-File',
                                       '/powershell/Destroy.ps1',
                                       '-Username',
                                       self.connection.username,
                                       '-Password',
                                       self.connection.password,
                                       '-ComplianceSearchName',
                                       compliance_search_name,
                                       '-TimeoutInMinutes',
                                       str(timeout),
                                       '-Office365URI',
                                       self.connection.o365_uri],
                                      cwd=os.getcwd(),
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE)

        out, err = powershell.communicate()
        if err:
            self.logger.error(err)
            if out:
                self.logger.error(out)

            # This is a generic error message as there's a lot that can go wrong here.
            # Hopefully the above logs give us enough information to diagnose the problem
            raise PluginException(
                cause="Powershell returned an error.",
                assistance="Please see the plugin logs for more information."
            )

        return {Output.SUCCESS: True}
        