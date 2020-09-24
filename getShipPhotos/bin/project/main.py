# -*- coding: utf-8 -*-

# @File     : main.py
# @Date     : 2020-09-11
# @Author   : 水张哲
# @Software : PyCharm
import time

from lib.ShipRegister import ShipRegister
from lib.ShipsRegister import ShipsRegister
from conf.setting import FLAG, TYPE, SHIP_PHOTOS_MIN_COUNT
from lib.PhotosRegister import PhotosRegister


# 主程序入口
def main():
    # 主函数
    for simpleType in TYPE:
        for flag in FLAG:
            # 注册ships对象
            _ships = ShipsRegister(flag, simpleType)

            # 获取ship对应的国家代号以及类型编号
            countryCode = _ships.getCountryCode()
            typeCode = _ships.getShipTypeCode()

            # 生成存储的数据表名称
            tableName = simpleType + "_" + flag

            print(time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime(time.time())) + "正在查询： [" + simpleType + "] 类型 - [" + flag + "] 国家 的船只...")
            # 判断该类型、国家的船只是否已经存储
            if not _ships.isSearched(tableName):
                # 获取船只列表
                shipsList = _ships.getShipsList(countryCode, typeCode)

                # 获取船只列表
                _ships.saveShipList(shipsList, tableName)

                # 控制台输出反馈
                print(time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime(time.time())) + "查询结果： [" + simpleType+ "] 类型 - " + "[" + flag  + "] 国家 的船只信息已存储，下面进行深度爬取,请耐心等待...")
            else:
                print(time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime(time.time())) + "查询结果： [" + simpleType+ "] 类型 - " + "[" + flag  + "] 国家 的船只信息已存在，下面进行深度爬取,请耐心等待...")

            # 获取符合要求的船只信息列表
            shipList = _ships.getShipList(tableName)

            # 检索船只图片
            for shipInfo in shipList:
                # 注册ship对象
                _ship = ShipRegister(shipInfo, flag, simpleType)

                # 检查船只是否已经检索
                if _ship.isSearched():
                    continue
                else:
                    shipNumb = 0
                    shipNameStr = _ship.getShipName()
                    shipCountPhotos = _ship.getShipPhotosCount()
                    if shipCountPhotos >= SHIP_PHOTOS_MIN_COUNT:
                        # 判断是否能获取船只类型，以防未响应耗时
                        getShipTypeTime = 0
                        shipType = _ship.getShipType()
                        while shipType == "" and getShipTypeTime < 3:
                            shipType = _ship.getShipType()
                            getShipTypeTime += 1
                        if shipType == "":
                            continue
                        # 获取图片列表
                        photoIdList = _ship.getShipPhotosList()
                        for photoId in photoIdList:
                            shipNumb += 1
                            # 注册船只图片
                            _photos = PhotosRegister(photoId, simpleType, shipNameStr, shipType, flag, str(shipNumb))
                            _photos.savePhotos()
                        _ship.addSearched()
                    else:
                        _ship.addSearched()
                        continue


