from shop.errors import InstantiateCSVError


def test_instantiate_csv_error():
    e = InstantiateCSVError()
    assert (str(e)) == "Неизвестная ошибка"
