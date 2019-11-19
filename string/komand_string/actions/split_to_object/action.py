import komand
from .schema import SplitToObjectInput, SplitToObjectOutput
# Custom imports below
from komand.exceptions import PluginException


class SplitToObject(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='split_to_object',
                description='Converts a string to an object containing key:value strings',
                input=SplitToObjectInput(),
                output=SplitToObjectOutput())

    def run(self, params={}):
        block_split = False
        string = params.get('string')
        sd = params.get('string_delimiter')
        bd = params.get('block_delimiter')

        if not sd:
            self.logger.info('User did not supply a string delimiter. '
                             'Defaulting to a space character.')
            sd = ' '

        if not string:
            raise PluginException(cause='Action failed! Missing required user input.',
                                  assistance='Please provide the input string.')

        if bd:
            block_split = True
            self.logger.info('Block delimiter received, performing block split first')

        d = {}

        if block_split:
            # Split a block of text before applying user's string split delimiter
            for line in string.split(bd):
                pair = line.split(sd)
                c = len(pair)
                if c == 2:
                    # Assign 1st element as key, 2nd as value to dict
                    d[pair[0].strip('"')] = pair[1].strip('"')
                else:
                    self.logger.info('Skipping {count} element split: {pair}'.format(count=c, pair=pair))
            return {'object': d}

        # Single key:value pair split e.g. USER=bob
        try:
            list_ = string.split(sd)
            self.logger.info('User input to split: %s -> %s', string, list_)
            d[list_[0]] = list_[1]
        except (ValueError, IndexError):
            self.logger.error('It looks like the input contained more than a single key:value split.')
            raise PluginException(cause='Action failed! Unable to split string cleanly.',
                                  assistance='Please try specifying the block delimiter for more multi-key:value input.')

        return {'object': d}
