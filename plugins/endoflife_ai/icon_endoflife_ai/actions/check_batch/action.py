import insightconnect_plugin_runtime
from .schema import CheckBatchInput, CheckBatchOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from icon_endoflife_ai.util import helper


class CheckBatch(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="check_batch",
            description=Component.DESCRIPTION,
            input=CheckBatchInput(),
            output=CheckBatchOutput(),
        )

    @staticmethod
    def build_item(item: dict) -> dict:
        """One entry of the API batch body: {"slug": ..., "version": ...}."""
        slug = str(item.get("product") or "").strip().lower()
        version = str(item.get("version") or "").strip()
        body = {"slug": slug}
        if version:
            body["version"] = version
        return body

    @staticmethod
    def build_result(item: dict, api_result: dict) -> dict:
        """Map one API batch result onto the plugin's per-item output, keyed by the submitted pair."""
        submitted_product = str(item.get("product") or "").strip()
        submitted_version = str(item.get("version") or "").strip()
        if not isinstance(api_result, dict) or api_result.get("error"):
            message = helper.error_message(api_result) if isinstance(api_result, dict) else "No result returned"
            if isinstance(api_result, dict) and isinstance(api_result.get("candidates"), list):
                message = f"{message}. Candidates: {', '.join(str(c) for c in api_result['candidates'])}"
            out = {"product": submitted_product, "found": False, "message": message}
            if submitted_version:
                out["version"] = submitted_version
            return out
        out = helper.score_to_output(api_result)
        out["found"] = True
        # Keep the submitted spelling so a workflow can join results back to its own inventory.
        out["product"] = submitted_product or out.get("product")
        if submitted_version:
            out["version"] = submitted_version
        return out

    def run(self, params={}):
        items = params.get(Input.ITEMS) or []
        if not isinstance(items, list):
            raise PluginException(
                cause="Items must be a list of product and version pairs.",
                assistance='Provide items such as [{"product": "nodejs", "version": "20"}].',
            )
        for item in items:
            if not isinstance(item, dict) or not str(item.get("product") or "").strip():
                raise PluginException(
                    cause="Every item needs a product slug.",
                    assistance='Provide items such as [{"product": "nodejs", "version": "20"}].',
                    data=str(item),
                )

        results = []
        chunk_size = helper.BATCH_CHUNK_SIZE
        for start in range(0, len(items), chunk_size):
            chunk = items[start : start + chunk_size]
            body = {"products": [self.build_item(item) for item in chunk]}
            self.logger.info(f"Checking batch items {start + 1} to {start + len(chunk)} of {len(items)}")
            status_code, json_ = helper.request_json(self.connection, "POST", "/v1/batch", json_body=body)
            if status_code == 404:
                raise PluginException(preset=PluginException.Preset.NOT_FOUND, data=str(json_))
            api_results = json_.get("results") if isinstance(json_, dict) else None
            if not isinstance(api_results, list) or len(api_results) != len(chunk):
                raise PluginException(
                    cause="The batch response did not carry one result per item.",
                    assistance="Try again. If the issue persists, check the endoflife.ai API status.",
                    data=str(json_),
                )
            for item, api_result in zip(chunk, api_results):
                results.append(insightconnect_plugin_runtime.helper.clean(self.build_result(item, api_result)))

        found = [r for r in results if r.get("found")]
        return {
            Output.RESULTS: results,
            Output.COUNT: len(results),
            Output.FOUND_COUNT: len(found),
            Output.EOL_COUNT: sum(1 for r in found if r.get("status") == "eol"),
        }
