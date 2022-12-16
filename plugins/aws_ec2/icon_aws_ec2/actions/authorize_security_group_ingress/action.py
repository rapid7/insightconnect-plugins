from .schema import AuthorizeSecurityGroupIngressInput, AuthorizeSecurityGroupIngressOutput, Component

# Custom imports below
from insightconnect_plugin_runtime.clients.aws_client import AWSAction


class AuthorizeSecurityGroupIngress(AWSAction):
    def __init__(self):
        super().__init__(
            name="authorize_security_group_ingress",
            description=Component.DESCRIPTION,
            input_=AuthorizeSecurityGroupIngressInput(),
            output=AuthorizeSecurityGroupIngressOutput(),
            aws_service="ec2",
            aws_command="authorize_security_group_ingress",
            pagination_helper=None,
        )
