"""Test slack command functionalities."""

import unittest
from unittest.mock import patch

import requests

import memeseeks


class ApiTest(unittest.TestCase):
    """Test the API endpoint."""

    def test_api_endpoints(self):
        """Test response 200 from API call."""
        moas_res = requests.get(memeseeks.ENDPOINT_MAP["mrmemeseeks"])
        frink_res = requests.get(memeseeks.ENDPOINT_MAP["frinkiac"])
        morbo_res = requests.get(memeseeks.ENDPOINT_MAP["morbotron"])
        self.assertEqual(moas_res.status_code, 200)
        self.assertEqual(frink_res.status_code, 200)
        self.assertEqual(morbo_res.status_code, 200)


class CheckArgsTests(unittest.TestCase):
    """Test check_args method from memeseeks.py."""

    @patch('memeseeks.ephemeral_response')
    def test_check_args_search_string_empty(self, mock):
        """Check ephemeral_response is called when no search_string is sent."""
        slack_text = ""
        memeseeks.check_args(slack_text, "second arg")
        self.assertTrue(mock.called)

    @patch('memeseeks.ephemeral_response')
    def test_check_args_search_string_exists(self, mock):
        """Test that a search_string was passed to the slack command."""
        slack_text = "argument"
        memeseeks.check_args(slack_text, "second arg")
        self.assertFalse(mock.called)

    @patch('memeseeks.ephemeral_response')
    def test_check_args_search_too_many_args(self, mock):
        """Check ephemeral_response is called when no search_string is sent."""
        slack_text = "testing; this is a test; extra arg"
        memeseeks.check_args(slack_text, "second arg")
        self.assertTrue(mock.called)

    def test_check_args_single_arg(self):
        """Test that query and meme_text get set correctly with a single arg."""
        slack_text = "testing"
        query, meme_text = memeseeks.check_args(slack_text, "second arg")
        self.assertEqual(query, "testing")
        self.assertEqual(meme_text, "")

    def test_check_args_two_args_space(self):
        """Test that query and meme_test get set corectly with two args and space."""
        slack_text = "testing; this is a test"
        query, meme_text = memeseeks.check_args(slack_text, "second arg")
        self.assertEqual(query, "testing")
        self.assertEqual(meme_text, "this is a test")

    def test_check_args_two_args_no_space(self):
        """Test that query and meme_test get set corectly with two args and space."""
        slack_text = "testing;this is a test"
        query, meme_text = memeseeks.check_args(slack_text, "second arg")
        self.assertEqual(query, "testing")
        self.assertEqual(meme_text, "this is a test")


class ImgSearchTests(unittest.TestCase):
    """Test img_search method from memeseeks.py."""

    @patch('memeseeks.ephemeral_response')
    def test_img_search_no_results(self, mock):
        """Check ephemeral_response is called when search gathers no results."""
        command = "mrmemeseeks"
        query = "doobens"  # I tested, and this doesn't exist in any of the api dbs.
        memeseeks.img_search(command, query, "fake arg 2")
        self.assertTrue(mock.called)


if __name__ == '__main__':
    unittest.main()
