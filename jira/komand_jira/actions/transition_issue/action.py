import komand
from .schema import TransitionIssueInput, TransitionIssueOutput, Input, Output, Component

# Custom imports below
from jira.exceptions import JIRAError
from komand.exceptions import PluginException


class TransitionIssue(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='transition_issue',
            description=Component.DESCRIPTION,
            input=TransitionIssueInput(),
            output=TransitionIssueOutput())

    def run(self, params={}):
        """Transition Issue"""

        issue = self.connection.client.issue(id=params[Input.ID])

        if not issue:
            raise PluginException(cause=f"No issue found with ID: {params[Input.ID]}.",
                                  assistance='Please provide a valid issue ID.')

        try:
            result = self.connection.client.transition_issue(
                issue=issue,
                transition=params[Input.TRANSITION],
                comment=params.get(Input.COMMENT),
                fields=params.get(Input.FIELDS)
            )
        except JIRAError as e:
            raise PluginException(cause=e.text if e.text else "Invalid input.", data=e)

        self.logger.info('Result: %s', result)

        return {Output.SUCCESS: True}
