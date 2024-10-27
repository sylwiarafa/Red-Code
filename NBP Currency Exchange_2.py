import pandas as pd

import requests


def nbp_request(currency):
    api_base_address = 'https://api.nbp.pl/api/exchangerates/rates/a/'
    
    response_format = "json"
    
    api_request = api_base_address + currency + "/?format=" + response_format
    
    response = requests.get(api_request)

    response_json = response.json()

 
    response_df = pd.DataFrame(response_json)

    response_rate_series = response_df.loc[:,"rates"] 

    response_rate_dict = response_rate_series[0]

    rate = float(response_rate_dict["mid"])
   
    return rate



def calculate_exchange (rate, amount):
    return amount / rate



def main():
    currency = input('What currency do you want to exchange the money to? ').upper()
    file_path = r"C:\Users\sylwi\Downloads\Currency_code.xlsx"
    df = pd.read_excel(file_path)
    currency_code = df.loc[:,"Currency Code"]
    
    if currency not in currency_code:
       print("Please provide correct Currency Code e.g. 'USD'")
    else:
        rate = nbp_request(currency)
        amount = float(input('How much PLN do you want to exchange? '))
    
    
    if rate: 
            
            print(f"PLN to {currency} rate is: {rate:.4f} PLN")
            
            exchanged_amount = calculate_exchange(rate, amount)
            print(f"If you exchange {amount} PLN, you will get {exchanged_amount:.4f} {currency}")
    
if __name__ == "__main__":
    main()
