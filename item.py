import csv


class Item:
    path_to_file_csv = 'data/items.csv'
    pay_rate = 0.85
    all = []

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"Item('name'={self.name}, 'price'={self.price}, 'quantity'={self.quantity})"

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """Считывает данные из csv-файла и создает экземпляры класса, инициализируя их данными из файла"""
        with open(cls.path_to_file_csv, 'r', encoding='cp1251') as file:
            reader = csv.DictReader(file)
            for row in reader:
                cls(name=row['name'], price=int(row['price']), quantity=int(row['quantity']))

    @property
    def name(self) -> str:
        """Возвращает название товара"""
        return self.check_name()

    @name.setter
    def name(self, new_name: str) -> None:
        """Меняет название товара"""
        self.__name = new_name
        self.check_name()

    def check_name(self) -> str:
        """Проверяет название товара на количество символов, должно быть не более 10"""
        if len(self.__name) <= 10:
            return self.__name
        raise Exception('Длина наименования товара превышает 10 символов.')

    def calculate_total_price(self) -> int or float:
        """Получает общую стоимость конкретного товара в магазине"""
        return self.quantity * self.price

    def apply_discount(self) -> None:
        """Применяет установленную скидку для конкретного товара"""
        self.price = self.price * self.pay_rate
