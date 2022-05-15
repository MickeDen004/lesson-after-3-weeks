import random
import datetime


def random_date(year):
    return datetime.datetime.strptime('{} {}'.format(random.randint(1, 366), year), '%j %Y')


class Person:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname
        self.birthday = random.randint(1945, 2004)
        self.id = id(self)
        self._blood_group = random.choice(["Group A",
                                        "Group B",
                                        "Group AB",
                                        "Group O"])

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Waiter(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
        self._year_of_employment = random.randint(2020, 2022)

    def serve(self, dish):
        print(f"This is your {dish}")

    def bill(self):
        print("this is your bill")
        return None




class Cook(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
        self._year_of_employment = random.randint(2015, 2022)
        self._country_of_origin = random.choice("Italy",
                                                "UK",
                                                "Belarus",
                                                "Canada",
                                                "USA")

    def cook(self, dish):
        print(f"Cooking {dish}...")
        return dish



class Visitor(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
        self._favorite_dish = random.choice(["Pizza Pepperoni", "Pizza Diabolo", "Roast chicken", "Waffles"])

    def make_an_order(self):
        return f"{self._favorite_dish}, please"




class Restaurant():
    def __init__(self, name, cuisine, cook: Cook, waiter: Waiter):
        self.name = name
        self.cuisine = cuisine
        self.cash = Box_Office()
        self.cook = cook
        self.waiter = waiter

    def greet_visitor(self, visitor: Visitor):
        print(f"Welcome {Visitor.full_name} to {self.name}")






class Delivery(Restaurant):
    def __init__(self, deliverer: Waiter):
        self.deliverer = deliverer
        self.cash_box = Box_Office()

    def print_delivery(self):
        return f"Delivery from {Restaurant.__name__}"


class Box_Office():
    counter = 2

    def __new__(cls, *args, **kwargs):
        if cls.counter:
            new_obj = object.__new__(cls)
            cls.counter -= 1
            return new_obj

    def __init__(self):
        self._storage = 100

    @property
    def storage(self):
        return self._storage

    @storage.setter
    def storage(self, val):
        self._storage = val

    @storage.getter
    def storage(self):
        return f"{float(self._storage)}$"

    def putm(self, amount: int):
        self.storage += amount

    def withdrawm(self, amount):
        if amount < self.storage:
            self.storage -= amount
        else:
            print("Ran ou of cash.")




x = Visitor("Jake", "Sutherland")
print(x.last_name)
print(x.birthday)
print(x.full_name)

y = Waiter("Usef", "Hussein")
