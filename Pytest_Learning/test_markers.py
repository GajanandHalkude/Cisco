import pytest
def test_sum():
    assert 10 + 10 == 20

@pytest.mark.skip
def test_diff():
    assert 20-10 == 10

@pytest.mark.xfail
def test_mul():
    assert (10 * 10) == 100

@pytest.mark.xfail
def test_divide():
    assert (100 / 10) == 100

@pytest.mark.skipif(condition=True, reason="Skipping this test for demonstration")
def test_fun():
    res = 100/100
    assert res == 1

@pytest.mark.regression
@pytest.mark.smoke
def test_three():
    assert True

@pytest.mark.filterwarnings("ignore::UserWarning")
def test_logout():
    print("Logout successful")

@pytest.mark.sanity
def test_calculation():
    assert 4 + 4 == 8

@pytest.mark.regression
def test_zero():
    assert 4 - 4 == 0

@pytest.mark.smoke
def test_reminder():
    assert 2%5==2