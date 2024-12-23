
class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species
    
    def eat(self):
        print(f"{self.name} їсть.")

    def sleep(self):
        print(f"{self.name} спить.")

    def make_sound(self):
        print(f"{self.name} видає звук.")


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, "Собака")
        self.breed = breed
    
    def make_sound(self):
        print(f"{self.name} гавкає: Гав-гав!")
    
    def fetch(self, item):
        print(f"{self.name} приносить {item}.")


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age, "Кіт")
        self.color = color
    
    def make_sound(self):
        print(f"{self.name} нявкає: Няв-няв!")
    
    def climb(self):
        print(f"{self.name} залазить на дерево.")


dog = Dog(name="Собака", age=3, breed="Лабрадор")
cat = Cat(name="Кішка", age=2, color="Сіра")

dog.eat()
dog.make_sound()
dog.fetch("м'яч")

cat.sleep()
cat.make_sound()
cat.climb()
