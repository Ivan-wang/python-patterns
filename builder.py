#!/usr/bin/python
# -*- coding : utf-8 -*-

"""
@author: Diogenes Augusto Fernandes Herminio <diofeher@gmail.com>
https://gist.github.com/420905#file_builder_python.py
"""

#Builder模式
#把一个复杂的对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示
#适用性：
#当创建复杂对象的算法应该独立于该对象的组成部分以及他们的装配方式时
#当构造过程必须允许被构造的对象有不同的表示时
# Director
# Director是用来构造一个使用Build接口的对象

class Director(object):

    def __init__(self):
        self.builder = None

    # Director创建和装配对象过程
    def construct_building(self):
        #调用Abstract Build来build
        self.builder.new_building()
        #调用Concrete Builder来完成build的流程
        self.builder.build_floor()
        self.builder.build_size()

    def get_building(self):
        return self.builder.building


# Abstract Builder
class Builder(object):

    def __init__(self):
        self.building = None

    def new_building(self):
        self.building = Building()


# Concrete Builder
class BuilderHouse(Builder):
    #Concrete Build继承Abstract Builder来完成某一部分的build
    def build_floor(self):
        self.building.floor = 'One'

    def build_size(self):
        self.building.size = 'Big'


class BuilderFlat(Builder):

    def build_floor(self):
        self.building.floor = 'More than One'

    def build_size(self):
        self.building.size = 'Small'


# Product
# Build的产品
class Building(object):

    def __init__(self):
        self.floor = None
        self.size = None

    def __repr__(self):
        return 'Floor: {0.floor} | Size: {0.size}'.format(self)


# Client
if __name__ == "__main__":
    director = Director()
    #给Director一个builder
    director.builder = BuilderHouse()
    #进行build
    director.construct_building()
    building = director.get_building()
    print(building)
    director.builder = BuilderFlat()
    director.construct_building()
    building = director.get_building()
    print(building)

### OUTPUT ###
# Floor: One | Size: Big
# Floor: More than One | Size: Small
