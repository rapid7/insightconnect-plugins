from unittest import TestCase
from icon_storage.util.cache_help import CacheHelp
from icon_storage.actions.store import Store
from icon_storage.actions.check_for_variable import CheckForVariable


class TestStoreAction(TestCase):
    def test_store(self):
        store = Store()
        var_check = CheckForVariable()
        params = {
            "variable_name": "foobar",
            "variable_value": "barfoo"
        }
        store.run(params)
        actual = var_check.run(params)

        expected = {'variable_found': True}
        self.assertEqual(expected, actual)

        cache_help = CacheHelp()
        cache_help.delete_variable("foobar")

        expected = {'variable_found': False}
        actual = var_check.run(params)
        self.assertEqual(expected, actual)

