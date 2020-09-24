# -*- coding: utf-8 -*-

# @File     : ShipRegister.py
# @Date     : 2020-09-15
# @Author   : 水张哲
# @Software : PyCharm

from lib.ShipsRegister import ShipsRegister

import time
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import requests
from bs4 import BeautifulSoup   # 网页解析，获取数据
import re   # 正则表达式，进行文字匹配
from lib.DbHelper import DbHelper


class ShipRegister(ShipsRegister):

    def __init__(self, shipInfo, countryName, simpleTypeName):
        ShipsRegister.__init__(self, countryName, simpleTypeName)
        self.ShipInfo = shipInfo
        self.CountryName = countryName
        self.SimpleTypeName = simpleTypeName

    def getShipId(self):
        return str(self.ShipInfo["shipId"])

    def getShipName(self):
        return str(self.ShipInfo["shipName"])

    def getShipPhotosCount(self):
        return int(self.ShipInfo["shipCountPhotos"])

    def getShipType(self):
        typeStr = ""
        url = r"https://www.marinetraffic.com/zn/ais/details/ships/shipid:" + ShipRegister.getShipId(self)

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
        chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
        chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化

        browser = webdriver.Chrome(chrome_options=chrome_options)
        browser.set_page_load_timeout(10)
        browser.set_script_timeout(10)
        try:
            browser.get(url)
            getTimes = 0
            while typeStr == "":
                sleep(1)
                getTimes += 1
                try:
                    typeTagP = browser.find_element_by_class_name("MuiTypography-body2")
                    typeStr = typeTagP.text.split("IMO")[0].split("MMSI")[0].split("ENI")[0].replace("/", " or ")
                except NoSuchElementException:
                    typeStr = ""
                if getTimes == 10:
                    break
        finally:
            browser.close()
            return typeStr

    def getShipPhotosList(self):
        sleep(2)
        findImgUrl = re.compile(r'<.*data-original="https://photos.marinetraffic.com/ais/showphoto.aspx\?photoid=(.*?)&amp;size=thumb300".*>')
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
        }
        url = "https://www.marinetraffic.com/zh/photos/of/ships/shipid:" + ShipRegister.getShipId(self)
        html = ""
        try:
            # 获取响应
            request = requests.get(url, headers=header)
            html = request.text
        except Exception as e:
            if hasattr(e, "code"):
                print(time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime(time.time())) + str(e.code))
            if hasattr(e, "reason"):
                print(time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime(time.time())) + str(e.reason))
        finally:
            soup = BeautifulSoup(html, "html.parser")
        dataList = []
        for item in soup.select("img"):
            # 保存一条记录所有信息
            item = str(item)
            # 获取行全部信息
            imgUrls = re.findall(findImgUrl, item)
            for imgUrl in imgUrls:
                dataList.append(imgUrl)
        print(time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime(time.time())) + "船舶图片ID已获取,正在根据ID下载图片中...")
        return dataList

    def isSearched(self):
        tableName = "found_shipids"
        select_ = "`shipId`"
        from_ = tableName
        where_ = "`shipId` = '" + ShipRegister.getShipId(self) + "'"
        results = DbHelper.selectTable(select_, from_, where_)
        dataList = list(results)
        if len(dataList) > 0:
            return True
        else:
            return False

    def addSearched(self):
        tableName = "found_shipids"
        keyString = "`shipId`"
        valueString = "'" + ShipRegister.getShipId(self) + "'"
        DbHelper.insertTable(tableName, keyString, valueString)
