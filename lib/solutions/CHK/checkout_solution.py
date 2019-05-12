from typing import Dict

SKU_COSTS = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15
}

MULTIBUYS = {
    "A": {
        "number": 3,
        "total_cost": 130
    },
    "B": {
        "number": 2,
        "total_cost": 45
    }
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    if not isinstance(skus, str) or not skus.isalpha() or not skus.isupper():
        return -1

    checkout_total = 0

    sku_counts: Dict[str, int] = {}
    
    for sku in skus:
        if sku not in SKU_COSTS:
            return -1

        if sku not in sku_counts:
            sku_counts[sku] = 1
        else:
            sku_counts[sku] += 1

    for sku in sku_counts:
        if sku in MULTIBUYS:
            multibuy_count = sku_counts[sku] // MULTIBUYS[sku]["number"]
            multibuy_cost = multibuy_count * MULTIBUYS[sku]["total_cost"]

            

    return checkout_total





