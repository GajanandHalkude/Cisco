import pytest
@pytest.fixture
def order():
    return []

@pytest.fixture
def outer(order, inner):
    order.append("outer")

class TestOne:

    @pytest.fixture
    def inner(self, order):
        order.append("one")

    def test_order(self, order, outer):
        assert order == ["one", "outer"]

class TestTwo:

    @pytest.fixture
    def inner(self, order):
            order.append("two")

    def test_order(self, order, outer):
        assert order == ["two", "outer"]


####

import pytest
@pytest.fixture
def order1():
    return []
@pytest.fixture
def a(order1):
    order1.append("a")
@pytest.fixture
def b(a, order1):
    order1.append("b")

@pytest.fixture(autouse=True)
def c(b, order1):
    order1.append("c")

@pytest.fixture
def d(b, order1):
    order1.append("d")

def test_order(order1,d):
    assert order1 == ["a","b","c","d"]
