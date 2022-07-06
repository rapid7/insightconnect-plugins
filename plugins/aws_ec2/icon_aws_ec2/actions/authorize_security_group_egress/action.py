from .schema import AuthorizeSecurityGroupEgressInput, AuthorizeSecurityGroupEgressOutput, Component

# Custom imports below
from icon_aws_ec2.util.common import AWSAction


class AuthorizeSecurityGroupEgress(AWSAction):
    def __init__(self):
        super().__init__(
            name="authorize_security_group_egress",
            description=Component.DESCRIPTION,
            input_=AuthorizeSecurityGroupEgressInput(),
            output=AuthorizeSecurityGroupEgressOutput(),
            aws_service="ec2",
            aws_command="authorize_security_group_egress",
            pagination_helper=None,
        )
