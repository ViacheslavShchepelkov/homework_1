from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity=0, number_of_sim=1):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return self.name

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        return None

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value: int):
        if not value < 1 or isinstance(value, int):
            raise ValueError("The number of physical SIM cards should be more than zero.")
        self.__number_of_sim = value