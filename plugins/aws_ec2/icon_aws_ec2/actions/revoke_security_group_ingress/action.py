from .schema import RevokeSecurityGroupIngressInput, RevokeSecurityGroupIngressOutput, Component

# Custom imports below
from insightconnect_plugin_runtime.clients.aws_client import AWSAction


class RevokeSecurityGroupIngress(AWSAction):
    def __init__(self):
        super().__init__(
            name="revoke_security_group_ingress",
            description=Component.DESCRIPTION,
            input_=RevokeSecurityGroupIngressInput(),
            output=RevokeSecurityGroupIngressOutput(),
            aws_service="ec2",
            aws_command="revoke_security_group_ingress",
            pagination_helper=None,
        )
