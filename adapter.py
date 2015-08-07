#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""http://ginstrom.com/scribbles/2008/11/06/generic-adapter-class-in-python/"""

#适配器模式 adapter pattern
#把一个类的结构变成客户端所期待的另外一种借口
#使原来因为接口不兼容的两个类现在可以协同工作
#分为两种
#1.类的适配器：适配器继承自已经实现的类
#2.对象适配器：适配器容纳一个它包裹的类的实例
#本代码实现的是第二种
class Dog(object):
    def __init__(self):
        self.name = "Dog"
        #add a common attribute for all objects
        self.age = 1

    def bark(self):
        return "woof!"


class Cat(object):
    def __init__(self):
        self.name = "Cat"
        self.age = 2

    def meow(self):
        return "meow!"


class Human(object):
    def __init__(self):
        self.name = "Human"
        self.age = 3

    def speak(self):
        return "'hello'"


class Car(object):
    def __init__(self):
        self.name = "Car"
        self.age = 4

    def make_noise(self, octane_level):
        return "vroom{0}".format("!" * octane_level)


class Adapter(object):
    """
    Adapts an object by replacing methods.
    Usage:
    dog = Dog
    dog = Adapter(dog, dict(make_noise=dog.bark))

    >>> objects = []
    >>> dog = Dog()
    >>> objects.append(Adapter(dog, make_noise=dog.bark))
    >>> cat = Cat()
    >>> objects.append(Adapter(cat, make_noise=cat.meow))
    >>> human = Human()
    >>> objects.append(Adapter(human, make_noise=human.speak))
    >>> car = Car()
    >>> car_noise = lambda: car.make_noise(3)
    >>> objects.append(Adapter(car, make_noise=car_noise))

    >>> for obj in objects:
    ...     print('A {} goes {}'.format(obj.name, obj.make_noise()))
    A Dog goes woof!
    A Cat goes meow!
    A Human goes 'hello'
    A Car goes vroom!!!
    """

    def __init__(self, obj, **adapted_methods):
        """We set the adapted methods in the object's dict"""
        self.obj = obj
        self.__dict__.update(adapted_methods)
        #执行过后
        #self.obj = obj
        #self.make_noise = obj.some_method

    def __getattr__(self, attr):
        """All non-adapted calls are passed to the object"""
        #getattr(obj, attr)
        #把attr当作一个变量去处理
        #return self.obj.attr
        #调用obj自身的attr的值
        return getattr(self.obj, attr)


def main():
    objects = []
    dog = Dog()
    objects.append(Adapter(dog, make_noise=dog.bark))
    print objects[-1].__dict__
    #obj.obj = dog
    #obj.make_noice() = dog.bark()
    #是之前实例化之后的dog的bark()
    cat = Cat()
    objects.append(Adapter(cat, make_noise=cat.meow))
    human = Human()
    objects.append(Adapter(human, make_noise=human.speak))
    car = Car()
    objects.append(Adapter(car, make_noise=lambda: car.make_noise(3)))

    for obj in objects:
        print("A {0} goes {1}, its age is {2}".format(obj.name, obj.make_noise(), obj.age))


if __name__ == "__main__":
    main()

### OUTPUT ###
# A Dog goes woof!
# A Cat goes meow!
# A Human goes 'hello'
# A Car goes vroom!!!
