from typing import Dict
from solutions.CHK.offers import Offers

class Checkout():
    def __init__(self, price_list: Dict[str, int], offers: Offers) -> None:
        self.price_list = price_list
        self.offers = offers

    def get_total_value(self, skus: str) -> int:
        sku_counts: Dict[str, int] = {}

        for sku in skus:
            if sku not in self.price_list:
                return -1

            if sku not in sku_counts:
                sku_counts[sku] = 1
            else:
                sku_counts[sku] += 1

        
