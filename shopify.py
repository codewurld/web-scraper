from turtle import title
import requests
import json

url = 'https://www.gymshark.com/products.json?limit=250&page=1'

#api get
request = requests.get(url)

#get shop data
shopData = request.json()

#get data info
for item in shopData['products']:
    title = item["title"]
    handle = item["handle"]
    productType = item["product_type"]
    releaseDate = item["created_at"]
      #print(title, handle, productType, releaseDate)

      #get variant data in products data
    for variant in item['variants']:
        price = variant['price']
        available = variant['available']
        print(price, available)