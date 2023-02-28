import pytest
from shop.phone import Phone


def test_get_phone(phone1):
    """Проверка инициализации экземпляра Phone с новым атрибутом"""
    assert repr(phone1) == 'Phone(iPhone 14, 120000, 5, 2)'


def test_get_number_of_sim(phone1):
    """Ожидается получение значения number_of_sim"""
    assert phone1.number_of_sim == 2


def test_change_test_get_number_of_sim(phone1):
    """Ожидается замена значения number_of_sim"""
    phone1.number_of_sim = 1
    assert phone1.number_of_sim == 1


def test_number_of_sim_value_error(phone1, phone3):
    """Ожидается исключение, если number_of_sim инициализировать или изменить значением <= 0 """
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0

    with pytest.raises(ValueError):
        phone3.number_of_sim()


def test_add(phone1, phone2, item1, item2):
    """Ожидается сложение экземпляров Phone и/или Item """
    assert phone1 + phone2 == 15
    assert phone1 + item1 == 25
    assert item2 + phone2 == 15


def test_value_error_add(phone1: Phone):
    """Ожидается исключение ValueError при сложении Phone с экземплярами не Phone или Item классов"""
    with pytest.raises(ValueError):
        phone1 + 10
