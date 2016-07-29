#!/bin/env python
"""
A data driven sample.
"""
from new import classobj


class Data(object):
    """ Data base class """

    def __init__(self, uid):
        self.uid = uid

    def __setattr__(self, key, value):
        # Data change callback place
        old_val = getattr(self, key, None)
        ret = object.__setattr__(self, key, value)
        print 'Callback: ', self.__class__.__name__, self.uid, key, old_val, "=>", value
        return ret

    @staticmethod
    def subtype(name, properties):
        """ Generate a subclass of Data"""
        subclass = classobj(name, (Data, ), {'__slots__': ("uid", ) + properties})
        return subclass


class Item(Data):
    """Example - Define data in class """
    __slots__ = ('name', 'price')


if __name__ == '__main__':

    Player = Data.subtype('Player', ('hp', 'name', 'coin'))
    p = Player(1001)
    p.hp = 100
    p.name = "Jack"
    p.coin = 100000

    a = Item(9001)
    a.name = 'Big Sword'
    a.price = 998

    p.hp += 1
    p.coin -= a.price




