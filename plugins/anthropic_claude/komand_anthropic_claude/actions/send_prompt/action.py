import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import SendPromptInput, SendPromptOutput, Input, Output, Component


class SendPrompt(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="send_prompt", description=Component.DESCRIPTION, input=SendPromptInput(), output=SendPromptOutput()
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        max_tokens = params.get(Input.MAX_TOKENS, 4096)
        prompt = params.get(Input.PROMPT)
        system_prompt = params.get(Input.SYSTEM_PROMPT)
        # END INPUT BINDING - DO NOT REMOVE

        response = self.connection.client.create_message(
            prompt=prompt,
            system_prompt=system_prompt,
            max_tokens=max_tokens,
        )

        response_text = self._extract_text(response)

        return {
            Output.RESPONSE: response_text,
            Output.MODEL: response.get("model", ""),
            Output.USAGE: response.get("usage", {}),
        }

    @staticmethod
    def _extract_text(response: dict) -> str:
        """Extract text content from the Claude API response."""
        content_blocks = response.get("content", [])
        text_parts = []
        for block in content_blocks:
            if block.get("type") == "text":
                text_parts.append(block.get("text", ""))
        return "\n".join(text_parts)
