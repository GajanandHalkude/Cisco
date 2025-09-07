import pytest

def test_zeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        1/0
def test_fileNotFoundError():
    with pytest.raises(FileNotFoundError):
        with open("records.txt",'r') as file:
            content = file.read()
            print(content)
def test_arrayOutOfBounds():
    with pytest.raises(IndexError):
        arr = []
        print(arr[3])
def test_assertionError():
    with pytest.raises(AssertionError):
        res = 2 + 3
        assert res == 6