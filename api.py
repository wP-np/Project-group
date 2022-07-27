
from cash_on_hand import list_diff
from overheads import overhead_list
from profit_loss import pl_list
import requests
def api():
    api_key = "X5FP3K03TOE3ARUT"
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey= {api_key}"
    response = requests.get(url)
    data = response.json()
    rate = (data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
    return(rate)

api()

    




