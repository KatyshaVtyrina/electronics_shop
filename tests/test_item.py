import pytest
from shop.item import Item


def test_get_item(item1):
    """Проверка инициализации экземпляра Item"""
    assert repr(item1) == "Item(Смартфон, 10000, 20)"


def test__str__(item2):
    """Проверка вывода информации для пользователя"""
    assert str(item2) == "Ноутбук"


def test_calculate_total_price(item1):
    """Ожидается общая стоимость конкретного товара в магазине"""
    assert Item.calculate_total_price(item1) == 200000


def test_apply_discount(item1, item2):
    """Ожидается применение установленной скидки для конкретного товара"""
    item1.apply_discount()
    assert item1.price == 8500
    assert item2.price == 20000


def test_instantiate_from_csv():
    """Ожидается инициализация экземпляра Item из файла .csv"""
    Item.all = []
    Item.PATH_TO_FILE_CSV = 'tests/data/test.csv'
    Item.instantiate_from_csv()
    item = Item.all
    assert len(item) == 3
    assert item[0].name == 'Смартфон'
    assert item[1].price == 300
    assert item[2].quantity == 9


def test_get_file_not_found_error():
    """Ожидается обработка исключения FileNotFoundError в связи с отсутствием файла"""
    Item.PATH_TO_FILE_CSV = 'tests/data/test3.csv'
    assert Item.instantiate_from_csv() == print(f"По указанному пути '{Item.PATH_TO_FILE_CSV}' файл item.csv отсутствует")


def test_get_instantiate_csv_error():
    """Ожидается обработка исключения InstantiateCSVError, так как файл поврежден"""
    Item.PATH_TO_FILE_CSV = 'tests/data/test2.csv'
    assert Item.instantiate_from_csv() == print("Файл item.csv поврежден")


def test_is_integer():
    """Проверка, является ли число целым, ожидается True или False"""
    assert Item.is_integer(5) is True
    assert Item.is_integer(5.0) is True
    assert Item.is_integer(5.5) is False
    assert Item.is_integer('5') is True
    assert Item.is_integer('5.0') is True
    assert Item.is_integer('5.5') is False


def test_get_int():
    """Ожидается int из str"""
    assert Item.get_int('5') == 5
    assert Item.get_int('5.7') == 5
    assert Item.get_int('5.0') == 5


def test_get_name(item2):
    """Ожидается получение значения name"""
    assert item2.name == 'Ноутбук'


def test_change_name(item2):
    """Ожидается замена значения name"""
    item2.name = 'Смартфон'
    assert item2.name == 'Смартфон'


def test_exception_name(item1):
    """Ожидается исключение Exception, если name более 10 символов """
    with pytest.raises(Exception):
        item1.name = 'Длина наименования товара превышает 10 символов.'


def test_add_(item1, item2):
    """Ожидается сложение экземпляров Item """
    assert item1 + item2 == 25


def test_value_error_add(item1: Item):
    """Ожидается исключение ValueError при сложении Item с экземплярами не Item класса"""
    with pytest.raises(ValueError):
        item1 + 10
