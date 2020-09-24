# -*- coding: utf-8 -*-

# @File     : PhotosRegister.py
# @Date     : 2020-09-17
# @Author   : 水张哲
# @Software : PyCharm
import time
import requests
import os
from time import sleep


class PhotosRegister:

    def __init__(self, photoId, shipSimpleType, shipName, shipType, shipFlag, shipNumb):
        self.PhotoId = photoId
        self.ShipSimpleType = shipSimpleType
        self.ShipName = shipName
        self.ShipType = shipType
        self.ShipFlag = shipFlag
        self.ShipNumb = shipNumb

    def savePhotos(self):
        fileUrl_simple_type = "./download/shipPhotos" + "/" + self.ShipSimpleType
        fileUrl_type = fileUrl_simple_type + "/" + self.ShipType
        fileUrl_flag = fileUrl_type + "/" + self.ShipFlag
        fileUrl_name = fileUrl_flag + "/" + self.ShipName
        sleep(2)
        header = {
            "Cookie": "__cfduid=d25be846f5c995310fbe1d09dea56db5f1599446764",
            "User-Agent": "PostmanRuntime/7.26.3"
        }
        url = "https://photos.marinetraffic.com/ais/showphoto.aspx?photoid=" + self.PhotoId + "&amp;size=thumb300"
        try:
            response = requests.get(url, headers=header, timeout=5)
            path = fileUrl_name + "/" + self.ShipName + "(" + self.ShipNumb + ").jpg"
            if not os.path.exists(fileUrl_simple_type):
                os.mkdir(fileUrl_simple_type)
            if not os.path.exists(fileUrl_type):
                os.mkdir(fileUrl_type)
            if not os.path.exists(fileUrl_flag):
                os.mkdir(fileUrl_flag)
            if not os.path.exists(fileUrl_name):
                os.mkdir(fileUrl_name)
            if not os.path.exists(path):
                if response.status_code == 200:
                    with open(path, "wb") as f:
                        f.write(response.content)
                    print(time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime(time.time())) + "正在保存船舶图片: " + path)
            else:
                print(time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime(time.time())) + "已经存在船舶图片: " + path)
        except Exception as e:
            if hasattr(e, "code"):
                print(time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime(time.time())) + str(e.code))
            if hasattr(e, "reason"):
                print(time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime(time.time())) + str(e.reason))
