# CHeckng for key and rate to be input in the code

import requests #pip install requests

api_key = 'QL3CDBPHW04PXYMZ' #from alphavantage.io ('Access Key')

from_c = 'INR'
to_c = 'NPR'

amount = 100

base_url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE'
main_url = base_url + '&from_currency=' + from_c + '&to_currency=' + to_c + '&apikey=' + api_key

response = requests.get(main_url)
result = response.json()

print(response)
print(result)