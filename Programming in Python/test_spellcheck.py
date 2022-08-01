import pytest
import spellcheck

# String variables to be tested
alpha = "Checking the length & structure of the sentence."
beta = "This sentence should fail the test"

# You may change the value assigned to input to test different inputs to your test functions
@pytest.fixture
def input_value():
    input = beta
    return input

# First test function test_length()
# Tests whether a string has fewer than 10 words and fewer than 50 chars
def test_length(input_value):
    assert spellcheck.word_count(input_value) < 10
    assert spellcheck.char_count(input_value) < 50

# Second test function test_struc()
# Tests whether a string begins with a capital letter and ends with a period
def test_struc(input_value):
    assert spellcheck.first_char(input_value).isupper()
    assert spellcheck.last_char(input_value) == "."