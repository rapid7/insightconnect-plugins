import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import DomainAvailabilityInput, DomainAvailabilityOutput, Input, Output, Component

# Custom imports below
from icon_whoisfreaks.util import constants, outputs, validators


class DomainAvailability(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="domain_availability",
            description=Component.DESCRIPTION,
            input=DomainAvailabilityInput(),
            output=DomainAvailabilityOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        domain = params.get(Input.DOMAIN)
        suggestion_count = params.get(Input.SUGGESTION_COUNT)
        suggestions = params.get(Input.SUGGESTIONS)
        # END INPUT BINDING - DO NOT REMOVE

        params = {"domain": validators.domain(domain), "sug": bool(suggestions)}
        if suggestions:
            params["count"] = validators.integer(suggestion_count, "Suggestion Count", 1, 100, default=5)
        result = self.connection.client.lookup("Domain Availability", "GET", constants.PATH_DOMAIN_AVAILABILITY, params)
        data = result.data_dict
        availability = data.get("availability")
        if isinstance(availability, bool):
            availability = "AVAILABLE" if availability else "UNAVAILABLE"
        availability = (outputs.to_str(availability) or "").upper() or None
        output = outputs.single(
            result,
            {
                Output.AVAILABILITY: availability,
                Output.AVAILABLE: {"AVAILABLE": True, "UNAVAILABLE": False}.get(availability),
                Output.SUGGESTIONS: outputs.to_object_list(data.get("domain_available_response")) or None,
            },
            include_response=False,
        )
        if result.found and outputs.to_str(data.get("message")):
            output[Output.MESSAGE] = outputs.to_str(data.get("message"))
        return output
