# -*- coding: utf-8 -*-

# @File     : ShipsRegister.py
# @Date     : 2020-09-11
# @Author   : 水张哲
# @Software : PyCharm

import json
import time
from time import sleep
import requests

from lib.ShipTypeRegister import ShipTypeRegister
from lib.DbHelper import DbHelper
from conf.setting import DB


class ShipsRegister(ShipTypeRegister):
    # 类初始化,继承CountryRegister类
    def __init__(self, countryName, simpleTypeName):
        ShipTypeRegister.__init__(self, countryName, simpleTypeName)
        self.CountryName = countryName
        self.SimpleTypeName = simpleTypeName

    # 获取船舶列表
    @staticmethod
    def getShipsList(countryCode, typeCode):
        # 保障服务器安全，设定访问数据休眠时间
        sleep(2)
        # 拼接URL链接
        httpUrl = "https://www.marinetraffic.com/zh/reports?asset_type=vessels" \
                  "&columns=photo:desc,flag,shipname,mmsi,ship_type,show_on_live_map,notes"\
                  + "&flag_in=" + countryCode \
                  + "&ship_type_in=" + typeCode
        # 设定参数头
        headers = {
            "Accept": "*/*",
            "Cookie": "__cfduid=dd6fec40b2361c95b88391e2ce1f699f11598231632; _ga=GA1.2.1883957982.1598231634; _pbjs_userid_consent_data=%7B%22consentString%22%3Anull%2C%22gdprApplies%22%3Afalse%2C%22apiVersion%22%3A1%7D; _pubcid=aed761a9-68d2-42fe-8fa3-f7be9879f98c; hubspotutk=f61c4e9cb31bb5dc098b3b8c6284d598; __beaconTrackerID=z54dotdax; _fbp=fb.1.1598239099189.239181634; SKpbjs-id5id=%7B%22ID5ID%22%3A%22ID5-ZHMO6zaulheoiuBKYuHdNQcmXC0eEdGAu7VuxyHDMg%22%2C%22ID5ID_CREATED_AT%22%3A%222020-08-24T01%3A14%3A03Z%22%2C%22ID5_CONSENT%22%3Atrue%2C%22CASCADE_NEEDED%22%3Atrue%2C%22ID5ID_LOOKUP%22%3Atrue%2C%223PIDS%22%3A%5B%5D%7D; _hjid=88159aac-fb66-4e70-9408-804714e7ace2; _hjUserAttributesHash=886ab41b36f738cd93fc2a88dadde0d3; SKpbjs-id5id_last=Fri%2C%2004%20Sep%202020%2001%3A37%3A22%20GMT; SKpbjs-unifiedid=%7B%22TDID%22%3A%220f9b8482-e17f-4984-9d83-93fd47dd8696%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222020-08-04T01%3A37%3A22%22%7D; SKpbjs-unifiedid_last=Fri%2C%2004%20Sep%202020%2001%3A37%3A22%20GMT; __gads=ID=b42e21d3707a36e7:T=1599185471:S=ALNI_MZqSgC6iWYcWB3AoIOjM4Gk_IcLCA; SERVERID=app4; _gid=GA1.2.1763324860.1599439103; _cmpQcif3pcsupported=1; _hjIncludedInSessionSample=1; _hjTLDTest=1; _hjAbsoluteSessionInProgress=0; id5id.1st_last=Mon%2C%2007%20Sep%202020%2000%3A38%3A29%20GMT; id5id.1st=%7B%22created_at%22%3A%222020-08-24T01%3A14%3A03Z%22%2C%22id5_consent%22%3Atrue%2C%22original_uid%22%3A%22ID5-ZHMO6zaulheoiuBKYuHdNQcmXC0eEdGAu7VuxyHDMg%22%2C%22universal_uid%22%3A%22ID5-ZHMO6zaulheoiuBKYuHdNQcmXC0eEdGAu7VuxyHDMg%22%2C%22signature%22%3A%22ID5_Ac0gx4JSzvNI-3TUo8eNRexdCU_3jnBxEfJn8LeSw29gEDlgURwnTRrV-ATePiDZkJh-xCi_pbRecbQSQU2inkk%22%2C%22link_type%22%3A0%2C%22cascade_needed%22%3Atrue%7D; __hstc=153128807.f61c4e9cb31bb5dc098b3b8c6284d598.1598231686753.1599189553500.1599439118432.25; __hssrc=1; dmxRegion=false; __atuvc=1%7C37; id5id.1st_347_nb=36; cto_bidid=ylN04l9hMEd1WWUwSXZRbm40anJBRWdGcXFValJuRWw5M1VuaWgxdXdIT0dIN2oyb2xmN0dZSDN0OFJjaDVxQkdHWUViUCUyRjlHcW5QTE9WbFNzbnpJSzdyJTJGWkhtJTJCMTlGTjdOZ1U3WEZSdWhPWUZFRSUzRA; cto_bundle=2R9YrV9GRXdBJTJGR1VUWkJDY0FHMG9uTnlwcSUyQnRoOE1sdUxpYmtESDNpUW44cUJVT3MlMkIwWVBJJTJCTjB1bHR3c1V1SHJjWGRwMjNoZks2aUhFR2R5YXhzSjdqWjJoRjklMkJTaWl2U3hPMjRwJTJGNzN6M3BJNmFUZDdqREJYdkhEemlCbFFCTnZ6cVJoMWtlb05nVzFYUkFhaU1neXJWaGclM0QlM0Q; mp_017900c581ab83839036748f85e0877f_mixpanel=%7B%22distinct_id%22%3A%20%223085750%22%2C%22%24device_id%22%3A%20%2217428a311a957-01dbda1b5b375e-3323766-1fa400-17428a311aa90f%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22%24user_id%22%3A%20%223085750%22%7D; _gat=1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
            "vessel-image": "00c980ee3049ba195ab27c7a8ef0c7c00b14",
        }
        dictStr = "None"
        try:
            response = requests.get(url=httpUrl, headers=headers)
            dictStr = json.loads(response.text)
        except Exception as e:
            if hasattr(e, "code"):
                print(time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime(time.time())) + "Error Code:" + str(e.code))
            if hasattr(e, "reason"):
                print(time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime(time.time())) + "Error Reason:" + str(e.reason))
        finally:
            dataList = []
            if dictStr != "None":
                # 解析数据存入List
                dataList = ShipsRegister.__analyzingShipsList(dictStr)
            return dataList

    # 解析船舶列表
    @staticmethod
    def __analyzingShipsList(dictStr):
        # 定义列表
        dataList = []
        # 判断是否存在数据
        if len(dictStr["data"]) > 0:
            for row in range(len(dictStr["data"])):
                rowList = []
                # shipId
                shipId = str(dictStr["data"][row]["SHIP_ID"])
                rowList.append(shipId)
                # shipMMSI
                shipMMSI = str(dictStr["data"][row]["MMSI"])
                rowList.append(shipMMSI)
                # shipName
                shipName = str(dictStr["data"][row]["SHIPNAME"])
                rowList.append(shipName)
                # shipCountry
                shipCountry = str(dictStr["data"][row]["COUNTRY"])
                rowList.append(shipCountry)
                # shipTypeSummary
                shipTypeSummary = str(dictStr["data"][row]["TYPE_SUMMARY"])
                rowList.append(shipTypeSummary)
                # shipCountPhotos
                shipCountPhotos = str(dictStr["data"][row]["COUNT_PHOTOS"])
                rowList.append(shipCountPhotos)
                # 将每一条记录存入总列表
                dataList.append(rowList)
        else:
            print(time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime(time.time())) + "该国家暂无此类型船舶!")
        return dataList

    # 船舶列表是否已被查询
    @staticmethod
    def isSearched(tableName):
        select_ = "`TABLE_NAME`"
        from_ = "INFORMATION_SCHEMA`.`TABLES"
        where_ = "`TABLE_SCHEMA`='" + DB + "' and `TABLE_NAME`='" + tableName + "'"
        tableNameList = list(DbHelper.selectTable(select_, from_, where_))
        if len(tableNameList) > 0:
            return True
        else:
            return False

    # 存储船舶列表
    @staticmethod
    def saveShipList(shipsList, tableName):
        nowCount = 0
        addCount = 0
        keyString = " `Id` INT UNSIGNED AUTO_INCREMENT," \
                    "`shipId` varchar(50)," \
                    "`shipMMSI` varchar(50)," \
                    "`shipName` varchar(50)," \
                    "`shipCountry` varchar(50)," \
                    "`shipTypeSummary` varchar(50),"\
                    "`shipCountPhotos` varchar(50)," \
                    " PRIMARY KEY ( `Id` )"
        tbString = "`shipId`,`shipMMSI`,`shipName`,`shipCountry`,`shipTypeSummary`,`shipCountPhotos`"
        DbHelper.dbInit(tableName, keyString)
        for data in shipsList:
            # 是否为第一个数据，1是，0不是
            isFirstData = 1
            valueString = ""
            for index in range(len(data)):
                # 格式化数据
                data[index] = str(data[index])
                # valueString 字符串拼接
                if isFirstData == 1:
                    valueString = valueString + "'" + data[index] + "'"
                    isFirstData = 0
                else:
                    valueString = valueString + ",'" + data[index] + "'"
            try:
                DbHelper.insertTable(tableName, tbString, valueString)
                addCount = addCount + 1
            finally:
                nowCount = nowCount + 1
                print(time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime(time.time())) + "已添加/已处理： " + str(addCount) + " / " + str(nowCount) + " 条信息，请耐心等候完成！")
        print(time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime(time.time())) + "数据存储完成!")

    @staticmethod
    def getShipList(tableName):
        _select = "`shipId`,`shipName`,`shipMMSI`,`shipCountPhotos`"
        _from = tableName
        _where = "1=1"
        shipList = list(DbHelper.selectTable(_select, _from, _where))
        return shipList
