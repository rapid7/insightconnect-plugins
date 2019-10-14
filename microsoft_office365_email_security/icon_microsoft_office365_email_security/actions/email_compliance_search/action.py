import komand
from komand.exceptions import PluginException
from .schema import EmailComplianceSearchInput, EmailComplianceSearchOutput, Input, Output, Component
# Custom imports below
import subprocess
import os
import json


class EmailComplianceSearch(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='email_compliance_search',
            description=Component.DESCRIPTION,
            input=EmailComplianceSearchInput(),
            output=EmailComplianceSearchOutput())

    def run(self, params={}):
        compliance_search_name = params.get(Input.COMPLIANCE_SEARCH_NAME)
        content_match_query = params.get(Input.CONTENT_MATCH_QUERY)
        timeout = params.get(Input.QUERY_TIMEOUT, 60)

        self.logger.info(f"Searching mailboxes with query of: {content_match_query}")

        args = ['pwsh',
                '-ExecutionPolicy',
                'Unrestricted',
                '-File',
                '/powershell/Search.ps1',
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
                self.connection.o365_uri]
        powershell = subprocess.Popen(args,
                                      cwd=os.getcwd(),
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE,
                                      universal_newlines=True)

        out, err = powershell.communicate()
        sources = self.extract_search_statistics(out)
        user_count = 0
        email_count = 0
        affected_users = []
        for item in sources:
            email_count += item['ContentItems']
            if item['ContentItems'] > 0:
                affected_users.append(item['Name'])
            if item['ContentItems'] > 0:
                user_count += 1
        if err:
            if out:
                self.logger.error(out)

            # This is a generic error message as there's a lot that can go wrong here.
            # Hopefully the above logs give us enough information to diagnose the problem
            raise PluginException(
                cause="PowerShell returned an error.",
                assistance="Please see the plugin logs for more information.",
                data=err
            )

        return {Output.AFFECTED_USERS: user_count, Output.EMAILS_FOUND: email_count, Output.USERS: affected_users}

    def extract_search_statistics(self, out):
        if 'SearchStatistics' not in out:
            raise PluginException(
                cause="PowerShell returned an unexpected response.",
                assistance="Please ensure all of your parameters are correct.",
                data=out
            )
        try:
            out_split = ('{"SearchStatistics":' + str(out).split('@{SearchStatistics=')[1])
            x = out_split.split('\n')[0]
        except IndexError:
            raise PluginException(
                cause="Could not find SearchStatistics in compliance search results.",
                assistance="Please ensure all of your parameters are correct.",
                data=out
            )
        try:
            out = json.loads(x)
        except json.decoder.JSONDecodeError:
            raise PluginException(
                preset=PluginException.Preset.INVALID_JSON,
                data=x
            )
        try:
            return_val = out['SearchStatistics']['ExchangeBinding']['Sources']
        except KeyError:
            raise PluginException(
                cause="PowerShell returned an unexpected response.",
                assistance="Please ensure all of your parameters are correct.",
                data=out
            )
        return return_val
