from unittest import TestCase
from icon_storage.util.cache_help import CacheHelp
from icon_storage.actions.store import Store
from icon_storage.actions.retrieve import Retrieve


class TestStoreAction(TestCase):
    def test_store(self):
        store = Store()
        retrieve = Retrieve()
        params = {
            "variable_name": "foobar",
            "variable_value": "barfoo"
        }
        store.run(params)
        actual = retrieve.run(params)

        expected = {'value': 'barfoo'}
        self.assertEqual(expected, actual)

        cache_help = CacheHelp()
        cache_help._delete_dict_file()
