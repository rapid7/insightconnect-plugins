import komand
from .schema import RevokeSecurityGroupIngressInput, RevokeSecurityGroupIngressOutput

# Custom imports below
from komand_aws_ec2.util.common import AWSAction


class RevokeSecurityGroupIngress(AWSAction):
    def __init__(self):
        super().__init__(
            name="revoke_security_group_ingress",
            description="Removes one or more ingress rules from a security group",
            input=RevokeSecurityGroupIngressInput(),
            output=RevokeSecurityGroupIngressOutput(),
            aws_service="ec2",
            aws_command="revoke_security_group_ingress",
            pagination_helper=None,
        )
