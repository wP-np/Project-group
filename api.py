import requests 
import json
api_key = "X5FP3K03TOE3ARUT"
url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey= {api_key}"
response = requests.get(url)
data = response.json()
print(data)
print(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])

