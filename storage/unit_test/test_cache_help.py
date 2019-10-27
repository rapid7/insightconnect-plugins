from unittest import TestCase
from icon_storage.util.cache_help import CacheHelp


class TestCacheHelp(TestCase):
    def setUp(self) -> None:
        self.cache_help = CacheHelp()
        self.cache_help._delete_dict_file()

    def tearDown(self) -> None:
        self.cache_help._delete_dict_file()

    def test_get_dict_from_store(self):
        actual = self.cache_help._get_dict_from_store()
        self.assertEqual(actual, {})

    def test_save_dict_to_store(self):
        test_dict = {"foo": "bar"}
        self.cache_help._save_dict_to_store(test_dict)
        acutal_dict = self.cache_help._get_dict_from_store()

        self.assertEqual(acutal_dict, test_dict)

    def test_store_variable(self):
        self.cache_help.store_variable("test_dict", {"foo": "bar"})
        actual = self.cache_help.retrieve_variable("test_dict")
        self.assertEqual(actual, {"foo": "bar"})

    def test_delete_variable(self):
        self.cache_help.store_variable("key1", "value1")
        self.cache_help.store_variable("key2", "value2")
        self.cache_help.store_variable("key3", "value3")

        self.cache_help.delete_variable("key2")

        actual = self.cache_help._get_dict_from_store()
        expected = {'key1': 'value1', 'key3': 'value3'}

        self.assertEqual(expected, actual)

    def test_check_for_variable(self):
        self.cache_help.store_variable("key1", "value1")
        self.cache_help.store_variable("key2", "value2")

        self.assertTrue(not self.cache_help.check_for_variable("don't find me"))
        self.assertTrue(self.cache_help.check_for_variable("key2"))
