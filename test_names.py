from names import make_full_name, \
    extract_given_name, extract_family_name
import pytest

def test_make_full_name():
    assert make_full_name("Constant", "Frankinburg") == "Frankinburg; Constant"
    assert make_full_name("Mary", "Smith") == "Smith; Mary"
    assert make_full_name("Daniel", "Walker-Reed") == "Walker-Reed; Daniel"


def test_extract_family_name():
    assert extract_family_name("Frankinburg; Constant") == "Frankinburg"
    assert extract_family_name("Smith; Mary") == "Smith"
    assert extract_family_name("Walker-Reed; Daniel") == "Walker-Reed"


def test_extract_given_name():
    assert extract_given_name("Frankinburg; Constant") == "Constant"
    assert extract_given_name("Smith; Mary") == "Mary"
    assert extract_given_name("Walker-Reed; Daniel") == "Daniel"



# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", __file__])