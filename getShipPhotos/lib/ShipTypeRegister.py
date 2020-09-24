# -*- coding: utf-8 -*-

# @File     : ShipTypeRegister.py
# @Date     : 2020-09-11
# @Author   : 水张哲
# @Software : PyCharm

from lib.CountryRegister import CountryRegister
from conf.dictionary import TYPE_DICTIONARY


class ShipTypeRegister(CountryRegister):
    # 类初始化,继承CountryRegister类
    def __init__(self, countryName, simpleTypeName):
        CountryRegister.__init__(self, countryName)
        self.SimpleTypeName = simpleTypeName

    def getShipTypeCode(self):
        return TYPE_DICTIONARY[self.SimpleTypeName]

