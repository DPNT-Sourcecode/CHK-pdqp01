SKU_COSTS = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    if not isinstance(skus, str) or not skus.isalpha() or not skus.isupper():
        return -1

    checkout_total = 0
    
    for sku in skus:
        if sku not in SKU_COSTS:
            return -1

        checkout_total += SKU_COSTS[sku]

    return checkout_total

