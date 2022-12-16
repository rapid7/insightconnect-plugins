from .schema import (
    UpdateSecurityGroupRuleDescriptionsEgressInput,
    UpdateSecurityGroupRuleDescriptionsEgressOutput,
    Component,
)

# Custom imports below
from insightconnect_plugin_runtime.clients.aws_client import AWSAction


class UpdateSecurityGroupRuleDescriptionsEgress(AWSAction):
    def __init__(self):
        super().__init__(
            name="update_security_group_rule_descriptions_egress",
            description=Component.DESCRIPTION,
            input_=UpdateSecurityGroupRuleDescriptionsEgressInput(),
            output=UpdateSecurityGroupRuleDescriptionsEgressOutput(),
            aws_service="ec2",
            aws_command="update_security_group_rule_descriptions_egress",
            pagination_helper=None,
        )
