import pytest

@pytest.mark.parametrize("a,b,f",[(10,20,30),(20,30,50),(30,40,70)])
def test_add(a,b,f):
    assert a + b == f

@pytest.mark.parametrize("input_exp,expected", [("3+4",7),("10-10",0),("20/10",2)])
def test_eval(input_exp,expected):
    assert eval(input_exp) == expected

#Side effects of Mutuable Objects in python
@pytest.mark.parametrize("data", [
    [1, 2, 3],  # List
    {"key": "value"},  # Dictionary
])
def test_mutation(data):
    data.append(4)  # Mutate the list
    assert data == [1, 2, 3, 4]  # Check that the mutation happened

def test_another_case(data):
    assert data == [1, 2, 3]  # This might fail for the first case! bcz data is changed.

# Preventing side effects

import pytest
import copy

@pytest.mark.parametrize("data", [
    [1, 2, 3],
    {"key": "value"},
])
def test_mutation(data):
    local_data = copy.deepcopy(data)  # Create a deep copy
    local_data.append(4)
    assert local_data == [1, 2, 3, 4]

