# -*- coding: utf-8 -*-

# @File     : DbHelper.py
# @Date     : 2020-09-11
# @Author   : 水张哲
# @Software : PyCharm

import time
import pymysql

from conf.setting import MYSQL_INFO


class DbHelper:
    # 数据库初始化
    @staticmethod
    def dbInit(tableName, keyString):
        try:
            DbHelper.dropTable(tableName)
            DbHelper.createTable(tableName, keyString)
        except Exception as e:
            if hasattr(e, "code"):
                print(time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime(time.time())) + "Error Code:" + str(e.code))
            if hasattr(e, "reason"):
                print(time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime(time.time())) + "Error Reason:" + str(e.reason))

    # 数据库增表
    @staticmethod
    def createTable(tableName, keyString):
        # 连接数据库
        conn = pymysql.connect(**MYSQL_INFO)
        try:
            sql = "create table `" + tableName + "` (" + keyString + ") ENGINE=InnoDB DEFAULT CHARSET=utf8mb4"
            cursor = conn.cursor()
            # 执行sql语句
            cursor.execute(sql)
            conn.commit()
        except Exception as e:
            if hasattr(e, "code"):
                print(time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime(time.time())) + "Error Code:" + str(e.code))
            if hasattr(e, "reason"):
                print(time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime(time.time())) + "Error Reason:" + str(e.reason))
            conn.rollback()
        finally:
            conn.close()

    # 数据库添加内容
    @staticmethod
    def insertTable(tableName, keyString, valueString):
        # 连接数据库
        conn = pymysql.connect(**MYSQL_INFO)
        try:
            sql = "insert into `" + tableName + "` (" + keyString + ") values (" + valueString + ")"
            cursor = conn.cursor()
            # 执行sql语句
            cursor.execute(sql)
            conn.commit()
        except Exception as e:
            if hasattr(e, "code"):
                print(time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime(time.time())) + "Error Code:" + str(e.code))
            if hasattr(e, "reason"):
                print(time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime(time.time())) + "Error Reason:" + str(e.reason))
            conn.rollback()
        finally:
            conn.close()

    # 数据库清表
    @staticmethod
    def dropTable(tableName):
        # 连接数据库
        conn = pymysql.connect(**MYSQL_INFO)
        try:
            sql = "drop table if exists `" + tableName + "`"
            cursor = conn.cursor()
            # 执行sql语句
            cursor.execute(sql)
            conn.commit()
        except Exception as e:
            if hasattr(e, "code"):
                print(time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime(time.time())) + "Error Code:" + str(e.code))
            if hasattr(e, "reason"):
                print(time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime(time.time())) + "Error Reason:" + str(e.reason))
            conn.rollback()
        finally:
            conn.close()

    # 数据库清表
    @staticmethod
    def selectTable(select_, from_, where_):
        # 连接数据库
        conn = pymysql.connect(**MYSQL_INFO)
        try:
            sql = "select " + select_ + " from `" + from_ + "` where " + where_
            cursor = conn.cursor()
            # 执行sql语句
            cursor.execute(sql)
            results = cursor.fetchall()
            return results
        except Exception as e:
            if hasattr(e, "code"):
                print(time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime(time.time())) + "Error Code:" + str(e.code))
            if hasattr(e, "reason"):
                print(time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime(time.time())) + "Error Reason:" + str(e.reason))
        finally:
            conn.close()


