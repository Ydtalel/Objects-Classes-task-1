from classes_form import *

goose_one = Goose("Серый", 5)
goose_two = Goose("Белый", 8)
cow = Cow("Манька", 250)
sheep_one = Sheep("Барашек", 40)
sheep_two = Sheep("Кудрявый", 38)
chicken_one = Chicken("Ко-Ко", 3)
chicken_two = Chicken("Кукареку", 2)
goat_one = Goat("Рога", 30)
goat_two = Goat("Копыта", 25)
duck = Duck("Кряква", 4)

animals_list = Animal.animals


def find_heaviest(list_):
    dict_ = {i.name: i.weight for i in list_}
    return f"Самое тяжелое животное - {max(dict_, key=dict_.get)}"


def get_weight_of_class():
    d = {}
    for animal in animals_list:
        class_name = (str(animal).split()[0].split(".")[1].lower())  # получаем название класса в формате строки
        d[class_name] = animal.count_class_weight()
        Animal.weight_count = 0
    return f"общий вес всех животных(экземпляров класса) в виде словаря:\n {d}"


print(find_heaviest(animals_list), "\n")
print(get_weight_of_class(), "\n")
for animal in animals_list:
    print(animal.make_sound())
    print(animal.feed(), "\n")
