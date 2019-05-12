

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    if not skus.isalpha() and not skus.isupper():
        return -1

    checkout_total = 0
    
    for sku in skus:
        if sku == "A":
            checkout_total += 50
        elif sku == "B":
            checkout_total += 30
        elif sku == "C":
            checkout_total += 20
        elif sku == "D":
            checkout_total += 15

    return checkout_total



