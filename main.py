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
    calSum, proSum, fatSum, saturatedSum, fattySum,\
    cholesterolSum, carbohydrateSum, sugarSum, fiberSum, \
    natriumSum, calciumSum, ironSum, seleniumSum, zincSum = 0,0,0,0,0,0,0,0,0,0,0,0,0,0
    for j in range(0,number):
        # print(xlx[j][i],' ',fetchCal.fetchCal(xlx[j][i]),fetchCal.fetchProtein(xlx[j][i]))
        result = fetchCal.fetchMain(xlx1[j][i])
        if (result):
            result.fetchOutPut()
            if(result.calory):
                calSum += float(result.calory) * (xlx2[j][i] / 100)
            if(result.protein):
                proSum += float(result.protein) * (xlx2[j][i] / 100)
            if(result.fat):
                fatSum += float(result.fat) * (xlx2[j][i] / 100)
            if(result.saturated_fat):
                saturatedSum += float(result.saturated_fat) * (xlx2[j][i] / 100)
            if(result.fatty_acid):
                fattySum += float(result.fatty_acid) * (xlx2[j][i] / 100)
            if(result.cholesterol):
                cholesterolSum += float(result.cholesterol) * (xlx2[j][i] / 100)
            if(result.carbohydrate):
                carbohydrateSum += float(result.carbohydrate) * (xlx2[j][i] / 100)
            if(result.sugar):
                sugarSum += float(result.sugar) * (xlx2[j][i] / 100)
            if(result.fiber_dietary):
                fiberSum += float(result.fiber_dietary) * (xlx2[j][i] / 100)
            if(result.natrium):
                natriumSum += float(result.natrium) * (xlx2[j][i] / 100)
            if(result.calcium):
                calciumSum += float(result.calcium) * (xlx2[j][i] / 100)
            if(result.iron):
                ironSum += float(result.iron) * (xlx2[j][i] / 100)
            if(result.selenium):
                seleniumSum += float(result.selenium) * (xlx2[j][i] / 100)
            if(result.zinc):
                zincSum += float(result.zinc) * (xlx2[j][i] / 100)
            print('---------------------------------------------------------------')
    print('第' + str(i+1) + '天' + '热量: ', calSum)
    print('第' + str(i+1) + '天' + '蛋白质: ', proSum)
    print('第' + str(i+1) + '天' + '脂肪: ', fatSum)
    print('第' + str(i+1) + '天' + '饱和脂肪: ', saturatedSum)
    # print('第' + str(i+1) + '天' + '反式脂肪: ', fattySum)
    print('第' + str(i+1) + '天' + '胆固醇: ', cholesterolSum)
    print('第' + str(i+1) + '天' + '碳水: ', carbohydrateSum)
    # print('第' + str(i+1) + '天' + '糖: ', sugarSum)
    print('第' + str(i+1) + '天' + '膳食纤维: ', fiberSum)
    print('第' + str(i+1) + '天' + '钠: ', natriumSum)
    print('第' + str(i+1) + '天' + '钙: ', calciumSum)
    print('第' + str(i+1) + '天' + '铁: ', ironSum)
    print('第' + str(i+1) + '天' + '硒: ', seleniumSum)
    print('第' + str(i+1) + '天' + '锌: ', zincSum)
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