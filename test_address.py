from address import extract_city, \
    extract_state, extract_zipcode
import pytest


def test_extract_city():
    assert extract_city("4814 Timothy Lane, Wasilla, Ak 99687") == "Wasilla"


def test_extract_state():
    assert extract_state("4814 Timothy Lane, Wasilla, Ak 99687") == "Ak"


def test_extract_zipcode():
    assert extract_zipcode("4814 Timothy Lane, Wasilla, Ak 99687") == "99687"

# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", __file__])