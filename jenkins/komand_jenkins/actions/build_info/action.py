import komand
from .schema import BuildInfoInput, BuildInfoOutput
# Custom imports below
import json


class BuildInfo(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='build_info',
                description='Returns detailed information on a build',
                input=BuildInfoInput(),
                output=BuildInfoOutput())

    def run(self, params={}):
        name = params.get('name')
        build_number = params.get('build number')

        output = self.connection.server.get_build_info(name, build_number)
        try:
            build_info = {'building': output['building'], 'full_display_name': output['fullDisplayName'],
                          'keep_log': output['keepLog'], 'number': output['number'], 'queue_id': output['queueId'],
                          'result': output['result'], 'timestamp': output['timestamp'], 'url': output['url'],
                          'built_on': output['builtOn'], 'items': output['changeSet']['items']}
        except KeyError as e:
            self.logger.error(e)
            self.logger.error("Raw build_info: " + json.dumps(output))
            raise Exception("An expected value in the build info return was not found."
                            " Check the error log for more information")

        return {'build_info': build_info}
