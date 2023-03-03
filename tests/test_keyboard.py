import pytest
from shop.keyboard import KeyBoard


def test_repr(keyboard1):
    assert repr(keyboard1) == 'KeyBoard(KD87A, 9600, 5, EN)'


def test_get_attributes(keyboard1, keyboard3):
    """Ожидается получение атрибутов экземпляра"""
    assert keyboard1.name == 'KD87A'
    assert keyboard3.price == 9600
    assert keyboard1.quantity == 5
    assert keyboard1.language == 'EN'
    assert keyboard3.language == 'RU'


def test_change_language_attribute_error(keyboard1):
    """Ожидается исключение при замене языка на несуществующий"""
    with pytest.raises(AttributeError):
        keyboard1.language = 'FR'


def test_language_value_error():
    """Ожидается исключение при создании экземпляра класса с несуществующим языком"""
    with pytest.raises(ValueError):
        KeyBoard('KD87A', 9600, 5, "fr")


def test_change_lang(keyboard1, keyboard2, keyboard3):
    """Ожидается замена языка"""
    keyboard1.change_lang()
    assert keyboard1.language == 'RU'
    keyboard1.change_lang()
    assert keyboard1.language == 'EN'
    keyboard2.change_lang()
    assert keyboard2.language == 'RU'
    keyboard3.change_lang()
    assert keyboard3.language == 'EN'
