from item import Item


def test___repr__(item2):
    assert Item.__repr__(item2) == "Item('name'=Ноутбук, 'price'=20000, 'quantity'=5)"


def test_calculate_total_price(item1):
    assert Item.calculate_total_price(item1) == 200000


def test_apply_discount(item1, item2):
    item1.apply_discount()
    assert item1.price == 8500
    assert item2.price == 20000
