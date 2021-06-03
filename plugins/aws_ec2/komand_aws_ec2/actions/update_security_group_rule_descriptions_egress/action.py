import komand
from .schema import UpdateSecurityGroupRuleDescriptionsEgressInput, UpdateSecurityGroupRuleDescriptionsEgressOutput

# Custom imports below
from komand_aws_ec2.util.common import AWSAction


class UpdateSecurityGroupRuleDescriptionsEgress(AWSAction):
    def __init__(self):
        super().__init__(
            name="update_security_group_rule_descriptions_egress",
            description="[EC2-VPC only] Updates the description of an egress (outbound) security group rule",
            input=UpdateSecurityGroupRuleDescriptionsEgressInput(),
            output=UpdateSecurityGroupRuleDescriptionsEgressOutput(),
            aws_service="ec2",
            aws_command="update_security_group_rule_descriptions_egress",
            pagination_helper=None,
        )
