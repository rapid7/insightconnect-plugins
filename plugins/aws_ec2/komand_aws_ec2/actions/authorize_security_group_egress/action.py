import komand
from .schema import AuthorizeSecurityGroupEgressInput, AuthorizeSecurityGroupEgressOutput

# Custom imports below
from komand_aws_ec2.util.common import AWSAction


class AuthorizeSecurityGroupEgress(AWSAction):
    def __init__(self):
        super().__init__(
            name="authorize_security_group_egress",
            description="[EC2-VPC only] Adds one or more egress rules to a security group for use with a VPC",
            input=AuthorizeSecurityGroupEgressInput(),
            output=AuthorizeSecurityGroupEgressOutput(),
            aws_service="ec2",
            aws_command="authorize_security_group_egress",
            pagination_helper=None,
        )
