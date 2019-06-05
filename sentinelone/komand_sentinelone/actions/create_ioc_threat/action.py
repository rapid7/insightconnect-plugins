import komand
from .schema import CreateIocThreatInput, CreateIocThreatOutput, Input, Output
# Custom imports below


class CreateIocThreat(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_ioc_threat',
                description='Create an IOC threat',
                input=CreateIocThreatInput(),
                output=CreateIocThreatOutput())

    def run(self, params={}):
        hash_ = params.get(Input.HASH)
        group_id = params.get(Input.GROUP_ID)
        path = params.get(Input.PATH)
        agent_id = params.get(Input.AGENT_ID)
        annotation = params.get(Input.ANNOTATION)
        annotation_url = params.get(Input.ANNOTATION_URL)

        affected = self.connection.create_ioc_threat(
            hash_, group_id, path, agent_id, annotation, annotation_url
        )
        return {Output.AFFECTED: affected}
