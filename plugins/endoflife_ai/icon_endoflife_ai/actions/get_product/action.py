import insightconnect_plugin_runtime
from .schema import GetProductInput, GetProductOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from icon_endoflife_ai.util import helper

# Fields kept on each version row, without the product-level ones repeated per row.
VERSION_FIELDS = (
    tuple(f for f in helper.SCORE_FIELDS if f not in ("product", "product_url")) + helper.VERSION_EXTRA_FIELDS
)


class GetProduct(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_product",
            description=Component.DESCRIPTION,
            input=GetProductInput(),
            output=GetProductOutput(),
        )

    def run(self, params={}):
        product = helper.path_segment(params.get(Input.PRODUCT), lowercase=True)
        if not product:
            raise PluginException(
                cause="Product is required.",
                assistance="Provide a product slug such as nodejs, windows-server or postgresql.",
            )

        self.logger.info(f"Listing versions of {product}")
        status_code, json_ = helper.request_json(self.connection, "GET", f"/v1/product/{product}")

        if status_code == 404:
            return {Output.FOUND: False, Output.MESSAGE: helper.error_message(json_)}

        versions = []
        for obj in json_.get("versions") or []:
            row = helper.score_to_output(obj, helper.VERSION_EXTRA_FIELDS)
            versions.append({field: row.get(field) for field in VERSION_FIELDS + ("cisa_kev_exposure",)})

        out = {
            Output.FOUND: True,
            Output.PRODUCT: json_.get("product"),
            Output.VERSION_COUNT: json_.get("version_count", len(versions)),
            Output.VERSIONS: versions,
            Output.PRODUCT_URL: json_.get("product_url"),
        }
        return insightconnect_plugin_runtime.helper.clean(out)
