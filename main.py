class SomeClass(object):
    attr1 = 42
    attr2 = "Hello, World"

    def method1(self, x):
        return 2*x


obj1 = SomeClass()
print(obj1.method1(6))
print(obj1.attr1)


class Point(object):
    def __init__(self, x, y, z):
        self.coord = (x, y, z)


p = Point(13, 14, 15)
print(p.coord)


# Динамическое изменение

class SomeClass2():
    pass


def squareMethod(self, x):
    return x*x

SomeClass2.square = squareMethod
obj = SomeClass2(object)
print(object.square(5))

# Static and Class methods

class SomeClass3(object):
    @staticmethod
    def hello():
        print("Hello, world")

    @classmethod
    def name(cls):
        print('I am, class {}'.format(cls.__name__))



print(SomeClass3.hello())
obj2 = SomeClass3()
print(obj2.hello())
print(SomeClass3.name)

# Специальные методы


class SomeClass4(object):
    def __new__(cls):
        print('new')
        return super(SomeClass4, cls).__new__(cls)

    def __init__(self):
        print('init')


obj4 = SomeClass4()

class Multiplier:
    def __call__(self, x, y):
        return x*y

multiply = Multiplier()
print(multiply.__call__(19, 19))



# Container imitation

class Collection:
    def __init__(self, list):
        self.list = list

    def __len__(self):
        return len(self.list)


collection = Collection([1, 2, 3])
print(len(collection))

# Принципы ООП

#Инкапсуляция

class SomeClass:
    def __init__(self, value):
        self._value = value

    def getvalue(self):
        return self._value

    def setvalue(self, value):
        self._value = value


    def delvalue(self):
        del self._value

    value = property(getvalue, setvalue, delvalue, "Value properties")

