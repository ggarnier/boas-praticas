class Burger:
    def description(self):
        return "Burger"

    def price(self):
        return 5


class BurgerWithCheese(Burger):
    def description(self):
        return "Burger with cheese"

    def price(self):
        return Burger.price(self) + 1


class BurgerWithBacon(Burger):
    def description(self):
        return "Burger with bacon"

    def price(self):
        return Burger.price(self) + 2


class BurgerWithCheeseAndBacon(BurgerWithCheese):
    def description(self):
        return "Burger with cheese and bacon"

    def price(self):
        return BurgerWithCheese.price(self) + 2


burger = Burger()
print("{}: ${}".format(burger.description(), burger.price()))

burger = BurgerWithCheese()
print("{}: ${}".format(burger.description(), burger.price()))

burger = BurgerWithBacon()
print("{}: ${}".format(burger.description(), burger.price()))

burger = BurgerWithCheeseAndBacon()
print("{}: ${}".format(burger.description(), burger.price()))
