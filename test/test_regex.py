import unittest
import yaml
import os
from data_url import DataURL

class TestDataURLRegex(unittest.TestCase):
    def setUp(self):
        # Load test cases from YAML file
        test_file = os.path.join(os.path.dirname(__file__), 'data_url_test_cases.yaml')
        with open(test_file, 'r') as f:
            self.test_cases = yaml.safe_load(f)['test_cases']

    def test_data_url_regex(self):
        for case in self.test_cases:
            url = case['url']
            expected_valid = case['valid']

            data_url = DataURL.from_url(url)
            actual_valid = data_url is not None
            with self.subTest(url=url, description=case['description']):
                self.assertEqual(actual_valid, expected_valid, f"URL: {url}\nDescription: {case['description']}")