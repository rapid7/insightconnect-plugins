import insightconnect_plugin_runtime
from .schema import InsertInput, InsertOutput, Input, Output, Component

# Custom imports below


class Insert(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="insert",
            description=Component.DESCRIPTION,
            input=InsertInput(),
            output=InsertOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        index_name = params.get(Input.INDEX)
        event = params.get(Input.EVENT, "").encode("utf-8")
        host = params.get(Input.HOST)
        source = params.get(Input.SOURCE)
        source_type = params.get(Input.SOURCE_TYPE)
        # END INPUT BINDING - DO NOT REMOVE

        try:
            index = self.connection.client.indexes[index_name]
        except (KeyError, IndexError):
            index = self.connection.client.indexes.create(index_name)

        kwargs = {}
        if host:
            kwargs["host"] = host
        if source:
            kwargs["source"] = source
        if source_type:
            kwargs["sourcetype"] = source_type

        index.submit(event, **kwargs)
        return {Output.SUCCESS: True}
