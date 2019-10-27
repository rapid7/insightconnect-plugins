from unittest import TestCase
from icon_storage.util.cache_help import CacheHelp
from icon_storage.actions.store import Store
from icon_storage.actions.delete_variable import DeleteVariable


class TestStoreAction(TestCase):
    def test_store(self):
        store = Store()
        delete_ = DeleteVariable()
        params = {
            "variable_name": "foobar",
            "variable_value": "barfoo"
        }
        store.run(params)
        actual = delete_.run(params)

        expected = {'success': True}
        self.assertEqual(expected, actual)

        cache_help = CacheHelp()
        actual_dict = cache_help._get_dict_from_store()
        self.assertEqual({}, actual_dict)

        cache_help._delete_dict_file()
