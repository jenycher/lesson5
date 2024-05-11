#Создать класс Store, в нем создать три магазина
#с разными названиями, адресами и ассортиментом товаров.
#Затем провести тесты методов одного выбранного магазина:
#добавление товара, обновление цены и удаление товара.
class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен в ассортимент магазина '{self.name}'.")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален из ассортимента магазина '{self.name}'.")
        else:
            print(f"Товар '{item_name}' отсутствует в ассортименте магазина '{self.name}'.")

    def get_item_price(self, item_name):
        return self.items.get(item_name)

    def update_item_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена на товар '{item_name}' в магазине '{self.name}' обновлена.")
        else:
            print(f"Товар {item_name} не найден.")


# Создание нескольких объектов класса Store
store1 = Store("Продуктовый магазин 'Челны-Хлеб", "ул. Мира, 1")
store1.add_item("Яблоки", 75.0)
store1.add_item("Бананы", 80.)
store1.add_item("Апельсины", 60.)
print("-" * 80)

store2 = Store("Магазин хоз.товаров 'Уютерра'", "пр. Ленина, 2")
store2.add_item("Посуда", 100.0)
store2.add_item("Пылесос", 5000.0)
print("-" * 80)

store3 = Store("Аптека 'Вита'", "пр. Победы, 3")
store3.add_item("Аспирин", 65.0)
store3.add_item("Анальгин", 45.0)
print("-" * 80)

# Тестирование методов выбранного магазина
print(f"Цена на яблоки в магазине '{store1.name}': {store1.get_item_price('Яблоки')}")
store1.update_item_price("Яблоки", 70.0)
print(f"Новая цена на яблоки в магазине '{store1.name}': {store1.get_item_price('Яблоки')}")
print("-" * 80)
store1.remove_item("Бананы")
print(f"Ассортимент в магазине '{store1.name}' после удаления товара:")
print(f"     {store1.items}")