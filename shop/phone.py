from shop.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        """Инициализирует новый атрибут - количество сим-карт"""
        super().__init__(name, price, quantity)
        self._number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self) -> int:
        """Возвращает количество сим-карт, если проходит проверку"""
        return self.check_number_of_sim()

    @number_of_sim.setter
    def number_of_sim(self, value: int) -> None:
        """Меняет значение количества сим-карт, если проходит проверку"""
        self._number_of_sim = value
        self.check_number_of_sim()

    def check_number_of_sim(self):
        """Проверяет на количество, если <= 0, выбрасывает исключение ValueError"""
        if self._number_of_sim > 0:
            return self._number_of_sim
        raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
