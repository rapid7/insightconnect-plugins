import komand
from .schema import RevokeSecurityGroupEgressInput, RevokeSecurityGroupEgressOutput

# Custom imports below
from komand_aws_ec2.util.common import AWSAction


class RevokeSecurityGroupEgress(AWSAction):
    def __init__(self):
        super().__init__(
            name="revoke_security_group_egress",
            description="[EC2-VPC only] Removes one or more egress rules from a security group for EC2-VPC",
            input=RevokeSecurityGroupEgressInput(),
            output=RevokeSecurityGroupEgressOutput(),
            aws_service="ec2",
            aws_command="revoke_security_group_egress",
            pagination_helper=None,
        )
