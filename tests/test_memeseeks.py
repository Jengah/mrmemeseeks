"""Test memeseeks.py functionality."""

from memeseeks import check_args

test_response_url = "test_response_url"
# def test_check_args_empty_string():
#     """Test passing memeseeks with no args."""


def test_check_args_search_string_only():
    """Test check_args correctly handles query argument."""
    slack_text = "search_string"
    test_search_string_result = ("search_string", "")
    test_search_string = check_args(slack_text, test_response_url)
    assert test_search_string == test_search_string_result


def test_check_args_search_string_and_meme_text():
    """Test check_args correctly handles query and meme_text args."""
    slack_text = "testing; this is a test"
    test_search_and_query_result = ("testing", "this is a test")
    test_search_and_query = check_args(slack_text, test_response_url)
    assert test_search_and_query == test_search_and_query_result


def test_check_args_two_args_no_space():
    """Test check_args correctly handles query and meme_text args regardless of whitespace."""
    slack_text = "testing;this is a test"
    test_no_whitespace_result = ("testing", "this is a test")
    test_no_whitespace = check_args(slack_text, test_response_url)
    assert test_no_whitespace == test_no_whitespace_result
