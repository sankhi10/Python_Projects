import pytest
from time import sleep

class TestSampleClass:
    def test_always_pass(self):
        sleep(10)
        assert True

    @pytest.mark.regression
    def test_always_fail(self):
        sleep(10)
        assert False

    @pytest.mark.smoke
    def test_upper(self):
        assert "loud noises".upper() == "LOUD NOISES"


@pytest.mark.smoke
@pytest.mark.regression
def test_list_palindrome():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]

def test_numbers():
    assert 37 in {
        num
        for num in range(1, 50)
        if num != 1 and not any([num % div == 0 for div in range(2, num)]) 
    }

@pytest.fixture
def sequence():
    return [1, 2, 3]


def test_sum(sequence):
    assert sum(sequence) == 6


def test_max(sequence):
    assert max(sequence) == 3


@pytest.mark.parametrize("palindrome", [
    ' ',
    'a',
    'abc',
    'never odd or even',
    ])
def test_palindrome(palindrome):
    assert palindrome[] == palindrome[::-1]