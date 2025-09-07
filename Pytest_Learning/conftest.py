import pytest

@pytest.fixture(autouse=False,scope="function") # function, class, module, package, session
def arange():
    print("Open Browser")
    print("Login")
    print("Browse Items")
    yield   #After Excuting the test this will be exucuted
    print("Logout")
    print("Close browser")

def pytest_runtest_setup(item):   # Hooks
    print("This is a Hook setup syntax",item)
def pytest_runtest_call(item):
    print("called when actual test exucuted ",item)
def pytest_runtest_teardown(item):
    print("This is Hook teardown fun",item)

# def pytest_collectstart(collect):
#     print("Collecter",collect)

# def pytest_runtest_logreport(report):
#     print("The report is",report)