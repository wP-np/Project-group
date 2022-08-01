
from pathlib import Path
import requests
def api_function():
    """
    Function will give the real updated currency exchange rate from USD to SGD based on forex trading and create the text file summary_report
    """
    home = Path.home()
    file_path = home/"OneDrive"/"Documents"/"Project group"/"summary_report.txt"
    file_path.touch()
    api_key = "X5FP3K03TOE3ARUT"
    #Claiming api key from alphavantage
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey= {api_key}"
    #Using a variable to store the link to call from
    response = requests.get(url)
    #Calling the api about forex currency exchange rates from alphavantage
    data = response.json()
    #Retrieving the data from the API and storing it as JSON object
    rate = (data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
    #Retrieving the real time currency exchange rate data from the dictionary in the JSON object
    rate1 = float(rate)
    with file_path.open(mode = "w", encoding = "UTF-8", newline = "") as file:
        file.write(f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{rate1}")
        return rate1



api_function()

    




