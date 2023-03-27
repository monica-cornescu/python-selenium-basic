import pytest


def add_numbers(a, b):
    return a + b


@pytest.mark.math
def test_with_small_numbers():
    assert add_numbers(1, 3) == 44, "Adding 1 with 3 results 4"


@pytest.mark.math
def test_with_bigger_numbers():
    assert add_numbers(4000, 1234) == 5234, "Adding 4000 with 1234 results 5234"
