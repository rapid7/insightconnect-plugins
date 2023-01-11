from .schema import DescribeSecurityGroupsInput, DescribeSecurityGroupsOutput, Component

# Custom imports below
from insightconnect_plugin_runtime.clients.aws_client import AWSAction, PaginationHelper


class DescribeSecurityGroups(AWSAction):
    def __init__(self):
        super().__init__(
            name="describe_security_groups",
            description=Component.DESCRIPTION,
            input_=DescribeSecurityGroupsInput(),
            output=DescribeSecurityGroupsOutput(),
            aws_service="ec2",
            aws_command="describe_security_groups",
            pagination_helper=PaginationHelper(
                input_token=["next_token"],
                output_token=["next_token"],
                result_key=["SecurityGroups"],
                limit_key="max_results",
            ),
        )
