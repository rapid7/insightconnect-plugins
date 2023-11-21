import insightconnect_plugin_runtime
from .schema import GetSubmittedInfoInput, GetSubmittedInfoOutput, Input, Output, Component

# Custom imports below


class GetSubmittedInfo(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name="get_submission_info",
                description=Component.DESCRIPTION,
                input=GetSubmittedInfoInput(),
                output=GetSubmittedInfoOutput())

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        # END INPUT BINDING - DO NOT REMOVE
        
        submission_id = params.get("submission_id")
        self.logger.info(f"Submission ID: {submission_id}")

        submission_info = self.connection.api.submission_info(submission_id = submission_id)
        self.logger.info(f"Submission info: {submission_info}")

        most_relevant_analysis = submission_info.get('most_relevant_analysis')

        # Added this in as output is expecting string array and if scan is running it will return "None" instead
        if most_relevant_analysis == None:
            most_relevant_analysis_result = {'webid': 'running', 'detection': 'running', 'score': 'running'}
            submission_info['most_relevant_analysis'] = most_relevant_analysis_result
            self.logger.info(f"No most_relevant_analysis: {submission_info}")

        return {'submission_info': submission_info}
