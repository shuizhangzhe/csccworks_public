# -*- coding: utf-8 -*-

# @File     : setup.py
# @Date     : 2020-09-11
# @Author   : 水张哲
# @Software : PyCharm

import time

from bin.project.main import main
from itemInit import init_db
from conf.setting import *
from lib.ShipsRegister import ShipsRegister

if __name__ == '__main__':

    if HOST == '' or USER == '' or PASSWORD == '' or DB == '' or CHARSET == '':
        print('请先进入 【conf】 目录设置配置文件 【setting.py】 中的参数！')
    else:
        if not ShipsRegister.isSearched('found_shipids'):
            init_db()
            print(time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime(time.time())) + "已寻找的船只数据表初始化成功！")
        # 开始计时
        time_start = time.time()

        # 程序入口
        main()

        # 结束计时
        time_end = time.time()
        print(time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime(time.time())) + "总计耗时: " + str(time_end - time_start) + "s")

