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
    checkout = Checkout(SKU_COSTS, Offers)

    return checkout.get_total_value(skus)

    # sku_counts: Dict[str, int] = {}

    # for sku in skus:
    #     if sku not in SKU_COSTS:
    #         return -1

    #     if sku not in sku_counts:
    #         sku_counts[sku] = 1
    #     else:
    #         sku_counts[sku] += 1

    # for sku in sku_counts:
    #     if sku in MULTIBUYS:
    #         multibuy_count = sku_counts[sku] // MULTIBUYS[sku]["number"]
    #         multibuy_cost = multibuy_count * MULTIBUYS[sku]["total_cost"]
    #         checkout_total += multibuy_cost

    #         indivdual_units = sku_counts[sku] % MULTIBUYS[sku]["number"]
    #         indivdual_cost = indivdual_units * SKU_COSTS[sku]
    #         checkout_total += indivdual_cost
    #     else:
    #         checkout_total += SKU_COSTS[sku] * sku_counts[sku]

    # return checkout_total

