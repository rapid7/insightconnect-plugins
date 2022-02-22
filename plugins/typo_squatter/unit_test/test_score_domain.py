from unittest import TestCase
from komand_typo_squatter.actions.score_domain import ScoreDomain
from komand_typo_squatter.actions.score_domain.schema import Input, Output
from parameterized import parameterized


class TestScoreDomain(TestCase):
    @parameterized.expand(
        [
            ["example.com", "example.com", 28],
            ["login.test.com", "login.test.com", 56],
            ["www.example.domain.com", "www.example.domain.com", 35],
        ]
    )
    def test_score_domain(self, name, domain, score):
        action = ScoreDomain()
        actual = action.run({Input.DOMAIN: domain})
        expected = {Output.SCORE: score}
        self.assertEqual(actual, expected)
