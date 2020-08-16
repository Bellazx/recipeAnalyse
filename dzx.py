# coding=utf-8

import mysql.connector
import pymysql
import xlrd
import numpy as np
import pandas as pd
import fetchCal


conn = mysql.connector.connect(user = 'root',password = 'root',database = 'dzx' )

cursor = conn.cursor()
# cursor.execute('select * from yk_foodnutrition limit 1;')
# value = cursor.fetchall()
# print(value)

fileName = 'recipe.xlsx'
xlx = pd.read_excel(fileName,header=None)
# df = xlx.parse('sheet1',dtype = 'object')
# print(xlx.head())
print(xlx.count(1).values)


number = xlx.count(1)[0]
for i in range(0,number):
    print(xlx[i][0],' ',fetchCal.fetchCal(xlx[i][0]))


# data = input().split(" ")
#
# def calCul(s):
#     cursor.execute("select nengliang from yk_foodnutrition where name LIKE '%" + s + "%';")
#     value = cursor.fetchall()
#     if (len(value) > 0):
#         return value[0][0];
#     cursor.execute("select nengliang from yk_foodnutrition_copy1 where name LIKE '%" + s + "%';")
#     value = cursor.fetchall()
#     if (len(value) > 0):
#         return value[0][0];
#     cursor.execute("select reliang from yk_yycfb where name LIKE '%" + s + "%';")
#     value = cursor.fetchall()
#     if (len(value) > 0):
#         return value[0][0];
#
# calSum = 0
# for i in data:
#     calSum += calCul(i)