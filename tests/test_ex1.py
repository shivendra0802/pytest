import pytest

@pytest.mark.slow
def test_example():
    print("test1")
    assert 1 == 1

@pytest.fixture(scope="session")
def fixture():
    print("run fixture 1")
    return 1

def test_example(fixture):
    print("run-example-1")
    num = fixture
    assert num == 1