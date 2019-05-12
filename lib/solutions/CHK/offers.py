from typing import Dict, Tuple

class Offers:
    MULTIBUYS = {
        "A": {"number": 3, "cost": 130},
        "B": {"number": 2, "cost": 45},
    }

    def apply(self, sku_counts: Dict[str, int]) -> Tuple[int, Dict[str, int]]:
        offer_value = 0

        for sku in sku_counts:
            if sku in self.MULTIBUYS:
                multibuy_count = sku_counts[sku] // self.MULTIBUYS[sku]["number"]
                multibuy_cost = multibuy_count * self.MULTIBUYS[sku]["cost"]
                offer_value += multibuy_cost

                sku_counts[sku] = sku_counts[sku] % self.MULTIBUYS[sku]["number"]

        return offer_value, sku_counts
