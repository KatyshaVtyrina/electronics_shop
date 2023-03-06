from shop.item import Item


class MixinKeyBoard:
    """Хранит и изменяет раскладку клавиатуры"""
    def __init__(self):
        self.__language = "EN"

    @property
    def language(self) -> str:
        """Возвращает язык"""
        return self.__language

    def change_lang(self) -> None:
        """Меняет раскладку, либо 'EN', либо 'RU'"""
        if self.__language.upper() == 'EN':
            self.__language = "RU"
        else:
            self.__language = "EN"


class KeyBoard(Item, MixinKeyBoard):
    """Родительский класс - Item
       миксин-класс - MixinKeyBoard"""
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        MixinKeyBoard.__init__(self)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.price}, {self.quantity}, {self.language})"
