"""Classes for melon orders."""

class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""

    # the following 2 lines can be included, but are not necessary because 
    # AbstractMelonOrder should never be instantiated directly

    order_type = None
    tax = 0

    def __init__(self, species, qty):

        # need species and qty to be passed in to 
        # be able to assign them as attributes
        # shipped we set a default val for, so no
        # need to pass in as argument
        self.species = species
        self.qty = qty
        self.shipped = False
    
    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

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

        # when we initialize domestic melon order
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


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

