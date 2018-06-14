import pytest
import main

from hypothesis import given  # define the inputs
import hypothesis.strategies as st

@given(k=st.integers(min_value=1)) # main decorator
def test_divisible_by_11(k):
    assert main.divisible_by_11(11*k)