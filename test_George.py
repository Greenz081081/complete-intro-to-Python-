from py import test
from George import get_difficulty
import pytest


def test_get_difficulty():

    difficulty = "easy", "medium", "hard", "quit"

    assert get_difficulty() == "easy"



pytest.main(["-v", "--tb=line", "-rN", __file__])
    

