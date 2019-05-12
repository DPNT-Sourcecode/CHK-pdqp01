from solutions.CHK import checkout_solution

import pytest

@pytest.mark.parametrize("sku, cost", [
    ("A", 50),
    ("B", 30),
    ("C", 20),
    ("D", 15)
])
def test_checkout_single_item(sku, cost):
    assert checkout_solution.checkout(sku) == cost

@pytest.mark.parametrize("invalid_input", [
    (123),
    ("a"),
    (""),
    ("F")
])
def test_checkout_with_invalid_input(invalid_input):
    assert checkout_solution.checkout(invalid_input) == -1

@pytest.mark.parametrize("skus, cost", [
    ("AAA", 130),
    ("BB", 45),
    ("AAAA", 180),
    ("BBB", 75)
])
def test_checkout_with_special_offer(skus, cost):
    assert checkout_solution.checkout(skus) == cost