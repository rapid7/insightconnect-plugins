import komand
from .schema import InsertInput, InsertOutput, Input, Output, Component
# Custom imports below


class Insert(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='insert',
                description=Component.DESCRIPTION,
                input=InsertInput(),
                output=InsertOutput())

    def run(self, params={}):
        """Run insert action"""
        index_name = params.get(Input.INDEX)
        event = params.get(Input.EVENT).encode("utf-8")

        try:
            index = self.connection.client.indexes[index_name]
        except (KeyError, IndexError):
            index = self.connection.client.indexes.create(index_name)

        kwargs = {}
        if params.get(Input.HOST):
            kwargs["host"] = params.get(Input.HOST)
        if params.get(Input.SOURCE):
            kwargs["source"] = params.get(Input.SOURCE)
        if params.get(Input.SOURCETYPE):
            kwargs["sourcetype"] = params.get(Input.SOURCETYPE)

        index.submit(event, **kwargs)
        return {}
