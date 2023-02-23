import pytest
from item import Item


def test___repr__(item1):
    assert Item.__repr__(item1) == "Item(Смартфон, 10000, 20)"


def test__str__(item2):
    assert Item.__str__(item2) == "Ноутбук"


def test_calculate_total_price(item1):
    assert Item.calculate_total_price(item1) == 200000


def test_apply_discount(item1, item2):
    item1.apply_discount()
    assert item1.price == 8500
    assert item2.price == 20000


def test_instantiate_from_csv():
    Item.all = []
    Item.path_to_file_csv = 'tests/test.csv'
    Item.instantiate_from_csv()
    item = Item.all
    assert len(item) == 3
    assert item[0].name == 'Смартфон'
    assert item[1].price == 300
    assert item[2].quantity == 9


def test_is_integer():
    assert Item.is_integer(5.0) is True
    assert Item.is_integer(5.0) is True
    assert Item.is_integer(5.5) is False
    assert Item.is_integer('5.0') is True
    assert Item.is_integer('5.0') is True
    assert Item.is_integer('5.5') is False


def test_get_int():
    assert Item.get_int('5') == 5
    assert Item.get_int('5.7') == 5
    assert Item.get_int('5.0') == 5


def test_name(item2):
    assert item2.name == 'Ноутбук'
    item2.name = 'Смартфон'
    assert item2.name == 'Смартфон'


def test_exception_name(item1):
    with pytest.raises(Exception):
        item1.name = 'Длина наименования товара превышает 10 символов.'
