import requests

def fetchCal(foodName):
    url = 'https://food.boohee.com/fb/v1/search?q=' + foodName + '&page=1'
    data = requests.get(url).json()
    if (len(data['items']) > 0):
        return int(data['items'][0]['calory'])
    else:
        return None











#https://food.boohee.com/fb/v2/foods/hongshaorou/detail?tenant=null&token=ALyhQ6FytQUpnTRsGqQqSsmLxu4o24J1