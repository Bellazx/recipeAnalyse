# coding=utf-8

import pandas as pd
import fetchCal

fileName1 = 'recipe.xlsx'
fileName2 = 'amount.xlsx'
xlx1 = pd.read_excel(fileName1, sheet_name='lunch', header=None)
xlx2 = pd.read_excel(fileName2, sheet_name='lunch', header=None)
# df = xlx.parse('sheet1',dtype = 'object')
# print(xlx.head())
# print(xlx.count(1).values)

for i in range(len(xlx1.index.values)):
    number = xlx1.count(1)[i]
    print('第' + str(i+1) + '天')
    calSum = 0
    for j in range(0,number):
        # print(xlx[j][i],' ',fetchCal.fetchCal(xlx[j][i]),fetchCal.fetchProtein(xlx[j][i]))
        result = fetchCal.fetchMain(xlx1[j][i])

        if (result):
            result.fetchOutPut()
            print('---------------------------------------------------------------')
    # print(calSum)
    print('***************************************************************')

def outputResult(foodIngredient, calSum, proSum, fatSum, saturatedSum, fattySum,
                 cholesterolSum, carbohydrateSum, sugarSum, fiberSum, natriumSum,
                 calciumSum, ironSum, seleniumSum, zincSum):
    if(foodIngredient.calory.split()[0]):
        calSum += float(result.calory.split()[0]) * (xlx2[j][i] / 100)


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