import pytest
import main

def test_divisible_by_11():
    for k in range(10):
        assert main.divisible_by_11(11*k)
        assert main.divisible_by_11(121)
        assert main.divisible_by_11(12122)