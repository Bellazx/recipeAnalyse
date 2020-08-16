import requests
from numpy import double


def fetchCal(foodName):
    url = 'https://food.boohee.com/fb/v1/search?q=' + foodName + '&page=1'
    data = requests.get(url).json()
    if (len(data['items']) > 0):
        return int(data['items'][0]['calory'])
    else:
        return None


def fetchCode(foodName):
    url = 'https://food.boohee.com/fb/v1/search?q=' + foodName + '&page=1'
    data = requests.get(url).json()
    if (len(data['items']) > 0):
        return data['items'][0]['code']
    else:
        return None


def fetchProtein(foodName):
    if (fetchCode(foodName) != None):
        url = 'https://food.boohee.com/fb/v2/foods/' + fetchCode(
            foodName) + '/detail?tenant=null&token=5qqo4ATuwMiG9FbJzYA2BbtwgeXuTFcZ'
        data = requests.get(url).json()
        if (len(data['ingredient_section']['main_ingredient']['protein']) > 0):
            return double(data['ingredient_section']['main_ingredient']['protein'])
        else:
            return 0
    else:
        return None


class foodIngredient():
    def __init__(self, name=None, calory=None, protein=None, fat=None, saturated_fat=None, fatty_acid=None,
                 cholesterol=None, carbohydrate=None, sugar=None, fiber_dietary=None, natrium=None):
        self.calory = calory
        self.protein = protein
        self.fat = fat
        self.saturate_fat = saturated_fat
        self.fatty_acid = fatty_acid
        self.cholesterol = cholesterol
        self.carbohydarte = carbohydrate
        self.sugar = sugar
        self.fiber_dietary = fiber_dietary
        self.natrium = natrium
        self.name = name

    def fetchOutPut(self):
        if (self.name):
            print('菜名   : ', self.name)
        if (self.calory):
            print('热量   : ', self.calory)
        if (self.protein):
            print('蛋白质  : ', self.protein)
        if (self.fat):
            print('脂肪   : ', self.fat)
        if (self.sugar):
            print('糖     : ', self.sugar)
        if (self.saturate_fat):
            print('饱和脂肪 : ', self.saturate_fat)
        if (self.fatty_acid):
            print('反式脂肪 : ', self.fatty_acid)
        if (self.cholesterol):
            print('胆固醇  : ', self.cholesterol)
        if (self.carbohydarte):
            print('碳水   : ', self.carbohydarte)
        if (self.fiber_dietary):
            print('膳食纤维 : ', self.fiber_dietary)
        if (self.natrium):
            print('钠     : ', self.natrium)


def fetchMain(foodName):
    if (fetchCode(foodName) != None):
        url = 'https://food.boohee.com/fb/v2/foods/' + fetchCode(
            foodName) + '/detail?tenant=null&token=5qqo4ATuwMiG9FbJzYA2BbtwgeXuTFcZ'
        data = requests.get(url).json()
        foodIng = foodIngredient()
        ingredientDic = data['ingredient_section']['main_ingredient']
        foodIng.calory = ingredientDic['calory']
        foodIng.protein = ingredientDic['protein']
        foodIng.fat = ingredientDic['fat']
        foodIng.saturated_fat = ingredientDic['saturated_fat']
        foodIng.fatty_acid = ingredientDic['fatty_acid']
        foodIng.cholesterol = ingredientDic['cholesterol']
        foodIng.carbohydrate = ingredientDic['carbohydrate']
        foodIng.sugar = ingredientDic['sugar']
        foodIng.fiber_dietary = ingredientDic['fiber_dietary']
        foodIng.natrium = ingredientDic['natrium']
        foodIng.name = foodName
        return foodIng
    else:
        return None
