import pytest
from shop.item import Item
from shop.keyboard import KeyBoard
from shop.phone import Phone


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def item2():
    return Item("Ноутбук", 20000, 5)


@pytest.fixture
def phone1():
    return Phone("iPhone 14", 120_000, 5, 2)


@pytest.fixture
def phone2():
    return Phone("iPhone 7", 30_000, 10, 1)


@pytest.fixture
def phone3():
    return Phone("iPhone 7", 30_000, 10, 0)


@pytest.fixture
def keyboard1():
    return KeyBoard('KD87A', 9600, 5)


@pytest.fixture
def keyboard2():
    return KeyBoard('KD87A', 9600, 5, "EN")


@pytest.fixture
def keyboard3():
    return KeyBoard('KD87A', 9600, 5, "ru")
