import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import AnalyzeIocsInput, AnalyzeIocsOutput, Input, Output, Component

IOC_SYSTEM_PROMPT = """You are a senior security analyst specializing in threat intelligence and indicator of compromise (IOC) analysis. When given IOCs, provide:

1. **Classification** — Identify the type of each indicator (IP, domain, hash, URL, email)
2. **Risk Assessment** — Rate each indicator's risk level (Critical, High, Medium, Low, Informational) with reasoning
3. **Context** — Provide known associations, threat actor groups, malware families, or campaigns if recognizable
4. **Recommendations** — Suggest specific containment and investigation actions
5. **Summary** — A brief executive summary of the overall threat picture

Be concise but thorough. If an indicator appears benign (e.g., private IP ranges, well-known legitimate domains), note that clearly."""


class AnalyzeIocs(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="analyze_iocs", description=Component.DESCRIPTION, input=AnalyzeIocsInput(), output=AnalyzeIocsOutput()
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        context = params.get(Input.CONTEXT, "")
        indicators = params.get(Input.INDICATORS)
        max_tokens = params.get(Input.MAX_TOKENS, 4096)
        # END INPUT BINDING - DO NOT REMOVE

        prompt = self._build_prompt(indicators, context)

        response = self.connection.client.create_message(
            prompt=prompt,
            system_prompt=IOC_SYSTEM_PROMPT,
            max_tokens=max_tokens,
        )

        analysis_text = self._extract_text(response)

        return {
            Output.ANALYSIS: analysis_text,
            Output.MODEL: response.get("model", ""),
            Output.USAGE: response.get("usage", {}),
        }

    @staticmethod
    def _build_prompt(indicators: list, context: str) -> str:
        """Build the analysis prompt from indicators and optional context."""
        indicator_list = "\n".join(f"- {indicator}" for indicator in indicators)
        prompt = f"Analyze the following indicators of compromise:\n\n{indicator_list}"
        if context:
            prompt += f"\n\nAdditional context: {context}"
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
