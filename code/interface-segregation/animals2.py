from abc import abstractmethod


class Animal:
    def __init__(self, name):
        self.__name = name

    def description(self):
        self.__check_ability("walk")
        self.__check_ability("fly")

    def __check_ability(self, ability):
        if callable(getattr(self, ability, None)):
            print("a {} can {}".format(self.__name, ability))
        else:
            print("a {} can't {}".format(self.__name, ability))


class WalkingAnimal(Animal):
    @abstractmethod
    def walk(self):
        pass


class FlyingAnimal(Animal):
    @abstractmethod
    def fly(self):
        pass


class Dog(WalkingAnimal):
    def __init__(self):
        super().__init__("dog")

    def walk(self):
        print("dog walking")


class Duck(WalkingAnimal, FlyingAnimal):
    def __init__(self):
        super().__init__("duck")

    def walk(self):
        print("duck walking")

    def fly(self):
        print("duck flying")


dog = Dog()
dog.walk()
# dog.fly()  # AttributeError: 'Dog' object has no attribute 'fly'
dog.description()

duck = Duck()
duck.walk()
duck.fly()
duck.description()
