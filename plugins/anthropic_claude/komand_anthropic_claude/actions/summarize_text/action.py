import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import SummarizeTextInput, SummarizeTextOutput, Input, Output, Component

SUMMARIZE_SYSTEM_PROMPT = """You are a security analyst tasked with summarizing security-related content. Produce clear, concise summaries that highlight actionable information. Use bullet points for key findings. Keep the summary focused and avoid unnecessary repetition."""


class SummarizeText(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="summarize_text",
            description=Component.DESCRIPTION,
            input=SummarizeTextInput(),
            output=SummarizeTextOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        focus = params.get(Input.FOCUS, "")
        max_tokens = params.get(Input.MAX_TOKENS, 2048)
        text = params.get(Input.TEXT)
        # END INPUT BINDING - DO NOT REMOVE

        prompt = self._build_prompt(text, focus)

        response = self.connection.client.create_message(
            prompt=prompt,
            system_prompt=SUMMARIZE_SYSTEM_PROMPT,
            max_tokens=max_tokens,
        )

        summary_text = self._extract_text(response)

        return {
            Output.SUMMARY: summary_text,
            Output.MODEL: response.get("model", ""),
            Output.USAGE: response.get("usage", {}),
        }

    @staticmethod
    def _build_prompt(text: str, focus: str) -> str:
        """Build the summarization prompt."""
        prompt = f"Summarize the following security content:\n\n{text}"
        if focus:
            prompt += f"\n\nFocus the summary on: {focus}"
        return prompt

    @staticmethod
    def _extract_text(response: dict) -> str:
        """Extract text content from the Claude API response."""
        content_blocks = response.get("content", [])
        text_parts = []
        for block in content_blocks:
            if block.get("type") == "text":
                text_parts.append(block.get("text", ""))
        return "\n".join(text_parts)
