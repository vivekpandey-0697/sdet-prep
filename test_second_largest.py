import pytest
from solution import second_largest

@pytest.mark.parametrize("nums, expected",[
    ([], None),
    ([1,2], 1),
    ([1,2,3], 2),
    ([3,2,1], 2),
    ([1,1,1], None),
    ([1,2,2], 1),
    ([5,5,4,4], 4) 
])

def test_second_largest(nums, expected):
    assert second_largest(nums) == expected