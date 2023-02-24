Магазин электроники - разработка классов для представления товаров магазина для проекта по созданию системы управления магазином электроники.

Класс Item представляет товары в магазине.

Экземпляр класса должен содержать атрибуты:
- название товара (name)
- цена за единицу товара (price)
- количество товара в магазине (quantity)

У Item есть два атрибута класса:
pay_rate - для хранения уровня цен с учетом скидки (например, 0.85, при скидке 15%)
all - для хранения созданных экземпляров класса

Чтобы начать работу с кодом необходимо создать экземпляр класса в формате:
item = Item(name=<название товара>, price=<цена за единицу>, quantity=<количество>)

Или создать объекты из данных файла с расширением .csv:
Item.path_to_file_csv = '<имя файла>' 
Item.instantiate_from_csv()

Методы класса:
calculate_total_price() - получает общую стоимость конкретного товара в магазине 
apply_discount() - применяет установленную скидку для конкретного товара