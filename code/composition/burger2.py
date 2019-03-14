class Burger:
    def __init__(self, extras=[]):
        self.__extras = extras

    def description(self):
        full_description = "Burger"
        extras = ", ".join(map(lambda extra: extra.description(), self.__extras))
        if len(extras) > 0:
            full_description += " with " + extras
        return full_description

    def price(self):
        full_price = 5
        for t in self.__extras:
            full_price += t.price()
        return full_price


class Cheese:
    def description(self):
        return "cheese"

    def price(self):
        return 1


class Bacon(Burger):
    def description(self):
        return "bacon"

    def price(self):
        return 2


burger = Burger()
print("{}: ${}".format(burger.description(), burger.price()))

burger = Burger(extras=[Cheese()])
print("{}: ${}".format(burger.description(), burger.price()))

burger = Burger(extras=[Bacon()])
print("{}: ${}".format(burger.description(), burger.price()))

burger = Burger(extras=[Cheese(), Bacon()])
print("{}: ${}".format(burger.description(), burger.price()))

triple_bacon = Burger(extras=[Bacon(), Bacon(), Bacon()])
print("{}: ${}".format(triple_bacon.description(), triple_bacon.price()))
