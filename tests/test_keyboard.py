import pytest
from shop.keyboard import KeyBoard


def test_repr(keyboard1):
    assert repr(keyboard1) == 'KeyBoard(KD87A, 9600, 5, EN)'


def test_get_attributes(keyboard1):
    """Ожидается получение атрибутов экземпляра"""
    assert keyboard1.name == 'KD87A'
    assert keyboard1.price == 9600
    assert keyboard1.quantity == 5
    assert keyboard1.language == 'EN'


def test_change_language_attribute_error(keyboard1):
    """Ожидается исключение при замене языка на несуществующий"""
    with pytest.raises(AttributeError):
        keyboard1.language = 'FR'


def test_change_lang(keyboard1):
    """Ожидается замена языка раскладки"""
    keyboard1.change_lang()
    assert keyboard1.language == 'RU'
    keyboard1.change_lang()
    assert keyboard1.language == 'EN'
