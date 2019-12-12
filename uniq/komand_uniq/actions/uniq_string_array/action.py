import komand
from .schema import UniqStringArrayInput, UniqStringArrayOutput
from komand.exceptions import PluginException
# Custom imports below
import json
from komand_uniq.util import util

class UniqStringArray(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='uniq_string_array',
                description='Remove duplicate items from an array of strings',
                input=UniqStringArrayInput(),
                output=UniqStringArrayOutput())

    def run(self, params={}):
        orig_ls = params.get('data')
        if not orig_ls:
            return { 'data': orig_ls, 'duplicate_count': 0 }
        new_ls = list(set(orig_ls))

        # Get total count of duplicates
        t_count = util.duplicate_count(orig_ls, new_ls)
        # Get individual element count
        e_count = util.element_count(orig_ls)

        return { 'result': new_ls, 'duplicate_count': t_count, 'element_count': e_count }

    def test(self):
        orig_ls = [ "a", "b", "c", "a", "c" ]
        new_ls = list(set(orig_ls))

        # Get total count of duplicates
        t_count = util.duplicate_count(orig_ls, new_ls)
        # Get individual element count
        e_count = util.element_count(orig_ls)

        if t_count == 2:
            return { 'result': new_ls, 'duplicate_count': t_count, 'element_count': e_count}
        self.logger.error('Count %s from %s is wrong', t_count, orig_ls)
        raise PluginException(cause='Test failed')
