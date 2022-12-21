from random import *


class Animal:
    animals = []
    weight_count = 0

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        Animal.animals.append(self)

    def count_class_weight(self):
        for animal in Animal.animals:
            if isinstance(self, type(animal)):
                Animal.weight_count += animal.weight

        return Animal.weight_count

    def feed(self):
        return f"'{self.name}' кушает."

    def make_sound(self):
        return f"Животное '{self.name}' издаёт звук"


class Bird(Animal):
    def __init__(self, name, weight):
        super().__init__(name, weight)

    def get_agg(self):
        return f"'{self.name}' приносит вам {randint(2, 4)} яйца"


class MilkingAnimal(Animal):
    def __init__(self, name, weight):
        super().__init__(name, weight)

    def get_milk(self):
        return f"'{self.name}'  сегодня в ударе. Удой составил {randint(6, 12)} л."


class Goose(Bird):
    def make_sound(self):
        return f"Гусь '{self.name}' {choice(['гогочет!', 'шипит!'])}"


class Chicken(Bird):
    def make_sound(self):
        return f"Курица '{self.name}' {choice(['кудахчет!', 'ко-ко-кокает!'])}"


class Duck(Bird):
    def make_sound(self):
        return f"Утка '{self.name}' крякает!"


class Cow(MilkingAnimal):
    def make_sound(self):
        return f"Корова '{self.name}' говорит Mу-ууу-уу!"


class Goat(MilkingAnimal):
    def make_sound(self):
        return f"Коза '{self.name}' говорит Me-eee-ee!"


class Sheep(Animal):
    def make_sound(self):
        return f"Баран '{self.name}' говорит Бе-еее-ее!"

    def cut(self):
        return f"Баран '{self.name}' пострижен под {choice(['ноль', 'пуделя'])}."
