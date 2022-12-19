from .schema import RevokeSecurityGroupEgressInput, RevokeSecurityGroupEgressOutput, Component

# Custom imports below
from insightconnect_plugin_runtime.clients.aws_client import AWSAction


class RevokeSecurityGroupEgress(AWSAction):
    def __init__(self):
        super().__init__(
            name="revoke_security_group_egress",
            description=Component.DESCRIPTION,
            input_=RevokeSecurityGroupEgressInput(),
            output=RevokeSecurityGroupEgressOutput(),
            aws_service="ec2",
            aws_command="revoke_security_group_egress",
            pagination_helper=None,
        )
