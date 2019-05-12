from typing import Dict
from solutions.CHK.checkout import Checkout
from solutions.CHK.offers import Offers

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:

    SKU_COSTS = {"A": 50, "B": 30, "C": 20, "D": 15}

    MULTIBUYS = {
        "A": {"number": 3, "total_cost": 130},
        "B": {"number": 2, "total_cost": 45},
    }

    if not isinstance(skus, str):
        return -1

    offers = Offers()
    checkout = Checkout(SKU_COSTS, offers)

    return checkout.get_total_value(skus)

