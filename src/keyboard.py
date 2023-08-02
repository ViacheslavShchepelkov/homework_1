from src.item import Item
from src.mixinkeyboard import MixinKeyboard


class Keyboard(Item, MixinKeyboard):
    def __init__(self, name, price, quantity):
        MixinKeyboard.__init__(self)
        super().__init__(name, price, quantity)