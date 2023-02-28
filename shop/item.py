import csv


class Item:
    path_to_file_csv = '../data/items.csv'
    pay_rate = 0.85
    all = []

    def __init__(self, name, price, quantity):
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.name}"

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """Считывает данные из csv-файла и создает экземпляры класса, инициализируя их данными из файла"""
        with open(cls.path_to_file_csv, 'r', encoding='cp1251') as file:
            reader = csv.DictReader(file)
            for row in reader:
                cls(name=row['name'], price=cls.get_int(row['price']), quantity=cls.get_int(row['quantity']))

    @staticmethod
    def is_integer(numb: int or float or str) -> bool:
        """Проверяет, является ли число целым."""
        if type(numb) is str:
            if '.' in numb:
                numb = float(numb)
                return numb == int(numb)
            return True
        return numb == int(numb)

    @staticmethod
    def get_int(numb: str) -> int:
        """Возвращает int"""
        return int(float(numb))

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
