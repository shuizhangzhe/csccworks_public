# -*- coding: utf-8 -*-

# @File     : itemInit.py
# @Date     : 2020-09-17
# @Author   : 水张哲
# @Software : PyCharm

"""
* ！！！注意事项！！！
* 该表用来存放已经寻找的船只id！
* 请谨慎操作，若初始化表格将使程序从 【零】 开始重新爬取图片！
"""
import time
from lib.DbHelper import DbHelper


def init_db():
    tableName = "found_shipids"
    keyString = " `Id` INT UNSIGNED AUTO_INCREMENT," \
                "`shipId` varchar(50)," \
                " PRIMARY KEY ( `Id` )"
    try:
        DbHelper.dbInit(tableName, keyString)
        initCode = 1
    except:
        initCode = 0
    return initCode


if __name__ == "__main__":
    if init_db():
        print(time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime(time.time())) + "已寻找的船只数据表初始化成功！")
    else:
        print(time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime(time.time())) + "已寻找的船只数据表初始化失败！")
