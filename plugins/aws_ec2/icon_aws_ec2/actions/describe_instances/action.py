from .schema import DescribeInstancesInput, DescribeInstancesOutput, Component

# Custom imports below
from insightconnect_plugin_runtime.clients.aws_client import AWSAction, PaginationHelper


class DescribeInstances(AWSAction):
    def __init__(self):
        super().__init__(
            name="describe_instances",
            description=Component.DESCRIPTION,
            input_=DescribeInstancesInput(),
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
