"""Classes for melon orders."""

import random
from datetime import datetime

class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""

    # the following 2 lines can be included, but are not necessary because 
    # AbstractMelonOrder should never be instantiated directly

    order_type = None
    tax = 0
    flat_fee = 0

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        # need species and qty to be passed in to 
        # be able to assign them as attributes
        # shipped we set a default val for, so no
        # need to pass in as argument
        self.species = species
        self.qty = qty
        self.shipped = False

    def get_base_price(self):
        '''This method determines if it is rush hour and combines 
        base price if it is
        '''
        self.base_price = random.randint(5,9)
        current_datetime = datetime.now()
        current_weekday = datetime.weekday(current_datetime)
        current_hour = current_datetime.hour
        if current_weekday in range(0,5) and current_hour in range(8,11):
            self.base_price += 4
    
    def get_total(self):
        """Calculate price, including tax."""
        
        price_increase = 1
        if self.species == "Christmas":
            price_increase = 1.5
        total = (1 + self.tax) * self.qty * self.base_price * price_increase + self.flat_fee

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True



class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        # every time this class is instantiated it 
        # needs to be given species and qty args,
        # so we can set them

        # when we initialize DomesticMelonOrder
        # we need to tell it species, qty

        # instead of specifying species, qty, shipped
        # here we will use the super's
        # (AbstractMelonOrders)'s init 
        # constructor
        super().__init__(species, qty)

        # self.species = species
        # self.qty = qty
        # self.shipped = False
        self.order_type = "domestic"
        self.tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        super().__init__(species, qty)

        # self.species = species
        # self.qty = qty
        self.country_code = country_code
        # self.shipped = False
        self.order_type = "international"
        self.tax = 0.17
        if self.qty < 10:
            self.flat_fee = 3


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    
    def __init__(self, species, qty):
        
        super().__init__(species, qty)
        self.order_type = "domestic"
        self.tax = 0
        self.passed_inspection = False

    def mark_inspection(self, passed):

        self.passed_inspection = passed

if __name__ == '__main__':
    test_order = DomesticMelonOrder('crenshaw', 4)