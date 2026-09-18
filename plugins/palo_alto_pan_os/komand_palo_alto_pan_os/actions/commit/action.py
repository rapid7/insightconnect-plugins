import insightconnect_plugin_runtime
from .schema import CommitInput, CommitOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
from typing import Optional


class Commit(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="commit",
            description=Component.DESCRIPTION,
            input=CommitInput(),
            output=CommitOutput(),
        )

    def run(self, params={}):
        cmd = params.get(Input.CMD) or "<commit></commit>"
        action = self.get_commit_action(params.get(Input.ACTION), cmd)

        output = self.connection.request.commit(action, cmd)

        try:
            return {"response": output["response"]}
        except KeyError:
            raise PluginException(
                cause="The output did not contain expected keys.",
                assistance="Contact support for help.",
                data=output,
            )

    def get_commit_action(self, action: str, cmd: str) -> Optional[str]:
        """
        Works out the commit action that goes with the command given.

        'all' is a Panorama commit-all, which pushes shared policy out to managed firewalls, and it
        only applies to a command rooted at <commit-all>. A firewall has nothing to push, so sending
        it there fails every time. The action used to default to 'all', which means published
        workflows hold that value whether or not they meant to, and it has to be dropped here rather
        than only in the schema.

        The other direction is deliberately left alone: a Panorama commit-all is only sent as one when
        the action says so, so giving a <commit-all> command does not silently change the action given.
        :param action: The commit action given to the action
        :param cmd: The command being committed
        :return The commit action to send, or None for a plain commit
        """

        if action == "all" and not cmd.lstrip().startswith("<commit-all"):
            self.logger.info(
                "The 'all' commit action only applies to a Panorama commit-all command, so this commit is sent as a"
                " normal commit of the candidate configuration. To push shared policy out to managed firewalls, give a"
                " command rooted at <commit-all> with the 'all' action."
            )
            return None

        return action
