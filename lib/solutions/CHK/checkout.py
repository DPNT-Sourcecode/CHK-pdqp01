from typing import Dict
from solutions.CHK.offers import Offers

class Checkout():
    def __init__(self, price_list: Dict[str, int], offers: Offers) -> None:
        self.price_list = price_list
        self.offers = offers

    