#							Realtime currency converter

# service used : alphavantage api

import requests #pip install requests
import csv

api_key = 'QL3CDBPHW04PXYMZ'

with open('physical_currency_list.csv', 'r') as f:
    csv_reader = dict(csv.reader(f, delimiter= ','))

print('Available codes are: ')

for key, value in csv_reader.items():
    print(key,'\t\t', value)

from_c = input('Enter a country code you want to convert from: ')
to_c = input('Enter a country code you want to convert to: ')

amount = float(input('Enter amount you want to convert: '))

base_url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE'
main_url = base_url + '&from_currency=' + from_c + '&to_currency=' + to_c + '&apikey=' + api_key

response = requests.get(main_url)
result = response.json()

key = result['Realtime Currency Exchange Rate']
rate = key['5. Exchange Rate']

print('Realtime exchange rate')
print(f'1 {from_c} : {rate} {to_c}')

print()

print('Converted amount')
print(f'{amount} {from_c} : {float(rate) * amount} {to_c}')
