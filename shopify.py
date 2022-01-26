
import requests
import json
# to create csv file
import pandas as pd

url = 'https://www.gymshark.com/products.json?limit=250&page=1'

#api get
request = requests.get(url)

#get shop data
shopData = request.json()

#stores list of returned products
product_list = []

#get data info
for item in shopData['products']:
    title = item["title"]
    handle = item["handle"]
    productType = item["product_type"]
    releaseDate = item["created_at"]
     
    #get images - catch error if no img
    for image in item['images']:
        try:
            imagesrc = image['src']
        except:
            imagesrc = 'None'

      #get variant data in products data
    for variant in item['variants']:
        price = variant['price']
        available = variant['available']
      
         

        #individual product 
        product = {
             'title': title,
             'handle': handle,
             'productType': productType,
             'releaseDate': releaseDate,
             'image': imagesrc,
             'price': price,
             'available': available

         }

        #add to list
        product_list.append(product)

#exports list to csv
df = pd.DataFrame(product_list)
df.to_csv('gym_shark_products.csv')
print('saved to file.')