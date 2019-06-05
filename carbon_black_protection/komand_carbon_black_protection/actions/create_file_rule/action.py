import komand
from .schema import CreateFileRuleInput, CreateFileRuleOutput, Input, Output, Component
from komand.exceptions import PluginException
# Custom imports below
import json
import requests


class CreateFileRule(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_file_rule',
                description=Component.DESCRIPTION,
                input=CreateFileRuleInput(),
                output=CreateFileRuleOutput())

    def run(self, params={}):
        file_catalog_id = params.get(Input.FILE_CATALOG_ID)
        name = params.get(Input.NAME)
        description = params.get(Input.DESCRIPTION)
        report_only = params.get(Input.REPORT_ONLY)
        reputation_approvals_enabled = params.get(Input.REPUTATION_APPROVALS_ENABLED)
        force_installer = params.get(Input.FORCE_INSTALLER)
        force_not_installer = params.get(Input.FORCE_NOT_INSTALLER)
        hash_ = params.get(Input.HASH)
        policy_ids = params.get(Input.POLICY_IDS)
        platform_flags = params.get(Input.PLATFORM_FLAGS)

        file_state = params.get(Input.FILE_STATE)
        file_state_switch = {
            "Unapproved": 1,
            "Approved": 2,
            "Banned": 3
        }
        file_state_int = file_state_switch.get(file_state, 1)

        self.logger.info(f"Creating file rule {name}")

        data = {
            'fileCatalogId': file_catalog_id,
            'name': name,
            'description': description,
            'fileState': file_state_int,
            'reportOnly': report_only,
            'reputationApprovalsEnabled': reputation_approvals_enabled,
            'forceInstaller': force_installer,
            'forceNotInstaller': force_not_installer,
            'policyIds': policy_ids,
            'hash': hash_,
            'platformFlags': platform_flags
        }

        url = self.connection.host + '/api/bit9platform/v1/fileRule'
        r = self.connection.session.post(url, json.dumps(data), verify=self.connection.verify)

        try:
            r.raise_for_status()
        except requests.exceptions.RequestException as e:
            self.logger.info(f"Call to Carbon Black raised exception: {e}")
            raise PluginException(cause="Call to Carbon Black failed",
                                  assistance=r.text)

        result = komand.helper.clean(r.json())

        return {Output.FILE_RULE: result}
