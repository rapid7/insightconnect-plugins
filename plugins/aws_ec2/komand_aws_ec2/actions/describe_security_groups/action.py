import komand
from .schema import DescribeSecurityGroupsInput, DescribeSecurityGroupsOutput

# Custom imports below
from komand_aws_ec2.util.common import AWSAction, PaginationHelper


class DescribeSecurityGroups(AWSAction):
    def __init__(self):
        super().__init__(
            name="describe_security_groups",
            description="Describes one or more of your security groups",
            input=DescribeSecurityGroupsInput(),
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
