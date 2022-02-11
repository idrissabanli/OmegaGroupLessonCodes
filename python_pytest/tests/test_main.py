import pytest
from codes.main import add


@pytest.mark.parametrize("a,b,expected", [(2,2,4), (6,3,9), (6,2,8)])
def test_add(a, b, expected):
    assert add(a,b) == expected


# def test_add2():
#     expected_result = 6
#     assert add(3,3) == expected_result
