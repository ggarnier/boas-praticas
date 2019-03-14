from abc import abstractmethod


class Animal:
    def __init__(self, name):
        self.__name = name

    @abstractmethod
    def walk(self):
        pass

    @abstractmethod
    def fly(self):
        pass

    def description(self):
        self.__check_ability("walk")
        self.__check_ability("fly")

    def __check_ability(self, ability):
        if callable(getattr(self, ability, None)):
            print("a {} can {}".format(self.__name, ability))
        else:
            print("a {} can't {}".format(self.__name, ability))


class Dog(Animal):
    def __init__(self):
        super().__init__("dog")

    def walk(self):
        print("dog walking")


dog = Dog()
dog.walk()
dog.fly()  # None
dog.description()
