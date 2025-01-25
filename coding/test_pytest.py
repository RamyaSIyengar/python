import pytest

def test_addition():
    assert 1 + 1 == 2


"""
Fixtures

Fixtures provide a way to set up and tear down test state.
Define fixtures using the @pytest.fixture decorator and use them in tests by listing them as parameters.

"""
@pytest.fixture
def sample_data():
    return [1,2,3]


@pytest.mark.regression
def test_sum(sample_data):
    assert sum(sample_data) == 6

"""
Parameterization

Use @pytest.mark.parametrize to run a test function with multiple sets of arguments.
"""


@pytest.mark.parametrize("a,b,expected",[(1,2,3),(3,4,7),(4,5,9)])
def test_addition(a,b,expected):
    assert a+b == expected


"""
Assertions

Use standard Python assertions.
pytest provides detailed assertion introspection to help with debugging.
"""
@pytest.mark.regression
def test_equal():
    assert 'hello'== 'hello'

"""
Markers

Use markers to categorize tests and add metadata.
Run tests with a specific marker using pytest -m <marker>.

collected 5 items / 3 deselected / 2 selected                                                                                     
pytest -m regression .\test_pytest.py
"""

"""
Plugins

Extend pytest functionality with plugins (e.g., pytest-xdist for parallel test execution).
"""
