from shop.item import Item


class MixinKeyBoard:
    """Хранит и изменяет раскладки клавиатуры"""

    def __init__(self, name, price, quantity, language='EN'):
        super().__init__(name, price, quantity)
        if language.upper() in ['EN', 'RU']:
            self.__language = language.upper()
        else:
            raise ValueError('Нет такого языка в раскладке')

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


class KeyBoard(MixinKeyBoard, Item):

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.price}, {self.quantity}, {self.language})"
