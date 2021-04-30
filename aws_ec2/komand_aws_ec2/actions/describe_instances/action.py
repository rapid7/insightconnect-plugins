import komand
from .schema import DescribeInstancesInput, DescribeInstancesOutput

# Custom imports below
from komand_aws_ec2.util.common import AWSAction, PaginationHelper


class DescribeInstances(AWSAction):
    def __init__(self):
        super().__init__(
            name="describe_instances",
            description="Describes one or more of your instances",
            input=DescribeInstancesInput(),
            output=DescribeInstancesOutput(),
            aws_service="ec2",
            aws_command="describe_instances",
            pagination_helper=PaginationHelper(
                input_token=["next_token"],
                output_token=["next_token"],
                result_key=["Reservations"],
                limit_key="max_results",
            ),
        )
