from solutions.CHK import checkout_solution

import pytest

def test_checkout_single_item():
    assert checkout_solution.checkout("A") == 50
