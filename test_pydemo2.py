import pytest

@pytest.fixture()
def setup():
    print("before yield")
    yield
    print("After yield")

def test_method1(setup):
    print("Method 1")

def test_Method2():
    print("Method 2")