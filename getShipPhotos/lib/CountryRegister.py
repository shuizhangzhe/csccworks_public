# -*- coding: utf-8 -*-

# @File     : CountryRegister.py
# @Date     : 2020-09-11
# @Author   : 水张哲
# @Software : PyCharm


from conf.dictionary import FLAG_DICTIONARY


class CountryRegister:

    # 类初始化
    def __init__(self, countryName):
        self.CountryName = countryName

    def getCountryCode(self):
        return FLAG_DICTIONARY[self.CountryName]

