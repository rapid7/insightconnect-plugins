import komand
from .schema import AuthorizeSecurityGroupIngressInput, AuthorizeSecurityGroupIngressOutput

# Custom imports below
from komand_aws_ec2.util.common import AWSAction


class AuthorizeSecurityGroupIngress(AWSAction):
    def __init__(self):
        super().__init__(
            name="authorize_security_group_ingress",
            description="Adds one or more ingress rules to a security group",
            input=AuthorizeSecurityGroupIngressInput(),
            output=AuthorizeSecurityGroupIngressOutput(),
            aws_service="ec2",
            aws_command="authorize_security_group_ingress",
            pagination_helper=None,
        )
