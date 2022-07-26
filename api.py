import requests
url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey= X5FP3K03TOE3ARUT'
response = requests.get(url)
print(response)