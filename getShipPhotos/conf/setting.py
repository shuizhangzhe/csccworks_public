# -*- coding: utf-8 -*-

# @File     : setting.py
# @Date     : 2020-09-11
# @Author   : 水张哲
# @Software : PyCharm

import pymysql

HOST = 'localhost'
USER = 'root'
PASSWORD = ''
DB = ''
CHARSET = 'utf8mb4'

# mysql 配置信息、连接数据库
MYSQL_INFO = {
    'host': HOST,
    'user': USER,
    'password': PASSWORD,
    'db': DB,
    'charset': CHARSET,
    'cursorclass': pymysql.cursors.DictCursor
}

# 设定船舶所属国家
FLAG = ["Afghanistan", "Albania", "Algeria", "American Samoa", "Andorra", "Angola", "Anguilla", "Antarctica", "Antigua Barbuda", "Argentina", "Armenia", "Aruba", "Ascension Is", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "British Virgin Is", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cambodia", "Cameroon", "Canada", "Cape Verde", "Cayman Is", "Cen Afr Rep", "Chad", "Chile", "China", "Christmas Is", "Cocos Is", "Colombia", "Comoros", "Congo", "Cook Is", "Costa Rica", "Croatia", "Cuba", "Curacao", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Rep", "DPR Korea", "DR Congo", "Ecuador", "Egypt", "El Salvador", "Equ. Guinea", "Eritrea", "Estonia", "Ethiopia", "Faroe Is", "Fiji", "Finland", "France", "French Polynesia", "FYR Macedonia", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Gibraltar", "Greece", "Greenland", "Grenada", "Guadeloupe", "Guatemala", "Guiana", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hong Kong", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Isle of Man", "Israel", "Italy", "Ivory Coast", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea", "Kuwait", "Kyrgyz Republic", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Macao", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Is", "Martinique", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Montserrat", "Morocco", "Mozambique", "Myanmar", "N Mariana Is", "Namibia", "Nauru", "Nepal", "Netherlands", "New Caledonia", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Niue", "Norway", "Oman", "Pakistan", "Palau", "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Pitcairn Is", "Poland", "Portugal", "Puerto Rico", "Qatar", "Reunion", "Romania", "Russia", "Rwanda", "Samoa", "San Marino", "Sao Tome Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Is", "Somalia", "South Africa", "Spain", "Sri Lanka", "St Helena", "St Kitts Nevis", "St Lucia", "St Paul Amsterdam Is", "St Pierre Miquelon", "St Vincent Grenadines", "Sudan", "Suriname", "Swaziland", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan ", "Tanzania", "Thailand", "Togo", "Tonga", "Trinidad Tobago", "Tunisia", "Turkey", "Turkmenistan", "Turks Caicos Is", "Tuvalu", "UAE", "Uganda", "UK", "Ukraine", "United Kingdom", "Uruguay", "US Virgin Is", "USA", "Uzbekistan", "Vanuatu", "Vatican", "Venezuela", "Vietnam", "Wallis Futuna Is", "Yemen", "Zambia", "Zimbabwe"]

# 设定船舶所属分类
TYPE = ["Navigation Aids", "Fishing", "Tugs & Special Craft", "High Speed Craft", "Passenger Vessels", "Cargo Vessels", "Tankers", "Pleasure Craft", "Unspecified Ships"]

# 设定单只船舶图片最少张数
SHIP_PHOTOS_MIN_COUNT = 5
