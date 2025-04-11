import insightconnect_plugin_runtime
from .schema import GetSubmittedInfoInput, GetSubmittedInfoOutput, Input, Output, Component


# Custom imports below


class GetSubmittedInfo(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_submitted_info",
            description=Component.DESCRIPTION,
            input=GetSubmittedInfoInput(),
            output=GetSubmittedInfoOutput(),
        )

    def run(self, params={}):
        submission_id = params.get(Input.SUBMISSION_ID)
        self.logger.info(f"Submission ID: {submission_id}")

        submission_info = self.connection.api.submission_info(submission_id=submission_id)
        self.logger.info(f"Submission info: {submission_info}")

        most_relevant_analysis = submission_info.get("most_relevant_analysis")

        # Added this in as output is expecting string array and if scan is running it will return "None" instead
        if most_relevant_analysis is None:
            most_relevant_analysis_result = {"webid": "running", "detection": "running", "score": "running"}
            submission_info["most_relevant_analysis"] = most_relevant_analysis_result
            self.logger.info(f"No most_relevant_analysis: {submission_info}")

        return {Output.SUBMISSION_INFO: submission_info}
