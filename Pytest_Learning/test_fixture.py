from asyncio import start_server
import pytest

@pytest.fixture
def setup():
    print("Open Browser")
    print("Login")
    print("Browse Items")
    yield   #After Excuting the test this will be exucuted
    print("Logout")
    print("Close browser")

def test_addtocart():
    print("Added to cart")

def test_removefromcart():
    print("Items removed from cart")

# @pytest.fixture
# def database_connection():
#     connection = create_database_connection()
#     yield connection
#     connection.close()
    
# def test_quary(database_connection):
#     result = database_connection.query("select * from users")
#     assert result is not None

#ex-02

@pytest.fixture
def user():
    return {"username": "testuser"}

@pytest.fixture
def user_profile(user):
    return {"user": user, "bio": "Test bio"}

def test_user_profile(user_profile):
    assert user_profile["user"]["username"] == "testuser"
    assert user_profile["bio"] == "Test bio"

@pytest.fixture
def config():
    return load_config("config.yml") # type: ignore

@pytest.fixture
def server():
    start_server()
    yield
    # stop_server()

# @pytest.fixture
# def user_session():
#     session = create_session() # type: ignore
#     yield session
#     session.logout()