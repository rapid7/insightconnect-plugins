from .schema import (
    UpdateSecurityGroupRuleDescriptionsIngressInput,
    UpdateSecurityGroupRuleDescriptionsIngressOutput,
    Component,
)

# Custom imports below
from insightconnect_plugin_runtime.clients.aws_client import AWSAction


class UpdateSecurityGroupRuleDescriptionsIngress(AWSAction):
    def __init__(self):
        super().__init__(
            name="update_security_group_rule_descriptions_ingress",
            description=Component.DESCRIPTION,
            input_=UpdateSecurityGroupRuleDescriptionsIngressInput(),
            output=UpdateSecurityGroupRuleDescriptionsIngressOutput(),
            aws_service="ec2",
            aws_command="update_security_group_rule_descriptions_ingress",
            pagination_helper=None,
        )
