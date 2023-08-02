from src.keyboard import Keyboard
from src.mixinkeyboard import MixinKeyboard


def test_keyboard():
    key_bord = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(key_bord) == "Dark Project KD87A"
    assert str(key_bord.language) == "EN"

    key_bord.change_lang()
    assert str(key_bord.language) == "RU"

    key_bord.change_lang().change_lang()
    assert str(key_bord.language) == "RU"


def test_mixin():
    mixin = MixinKeyboard()
    assert str(mixin.language) == "EN"