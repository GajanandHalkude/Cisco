import pytest

@pytest.fixture(params=[1000, 2000, 3000, 4000])
def test_payments(request):
    print("Hi")
    return request.param

def test_items(test_payments):
    print(f"Payment amount",test_payments)
