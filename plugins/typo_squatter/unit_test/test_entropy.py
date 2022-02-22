from unittest import TestCase
from komand_typo_squatter.util.utils import entropy


class TestEntropy(TestCase):
    def test_entropy(self):
        result = entropy("test.example.com")
        self.assertEqual(3.327819531114783, result)

    def test_entropy2(self):
        result = entropy("login.test.example_domain.com")
        self.assertEqual(3.8573068568981284, result)
