from unittest import TestCase
from icon_storage.util.cache_help import CacheHelp
from icon_storage.actions.store import Store


class TestStoreAction(TestCase):
    def test_store(self):
        store = Store()
        params = {
            "variable_name": "foobar",
            "variable_value": "barfoo"
        }
        store.run(params)
        cache_help = CacheHelp()

        # This is cheaty, but it's a test
        actual = cache_help._get_dict_from_store()
        expected = {'foobar': 'barfoo'}

        self.assertEqual(expected, actual)
        cache_help._delete_dict_file()
