# coding=utf-8

import xlrd
import numpy as np
import pandas as pd
import fetchCal

fileName = 'recipe.xlsx'
xlx = pd.read_excel(fileName,sheet_name='breakfast',header=None)
# df = xlx.parse('sheet1',dtype = 'object')
# print(xlx.head())
# print(xlx.count(1).values)

for i in range(len(xlx.index.values)):
    number = xlx.count(1)[i]
    print('第' + str(i+1) + '天')
    for j in range(0,number):
        # print(xlx[j][i],' ',fetchCal.fetchCal(xlx[j][i]),fetchCal.fetchProtein(xlx[j][i]))
        result = fetchCal.fetchMain(xlx[j][i])
        if (result):
            result.fetchOutPut()
            print('---------------------------------------------------------------')
    print('***************************************************************')


# cursor.execute('select * from yk_foodnutrition limit 1;')
# value = cursor.fetchall()
# print(value)
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