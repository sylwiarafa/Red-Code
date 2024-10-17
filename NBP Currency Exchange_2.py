import pandas as pd

import requests

api_base_address = 'https://api.nbp.pl/api/exchangerates/rates/a/'

currency = input('What currency do you want to exchange the money to?')
uppercase_currency = currency.upper()

# file_path = r"C:\Users\sylwi\Downloads\Book.xlsx"
# df = pd.read_excel(file_path)


# currency_code = df.loc[:,"Currency Code"]

# print(currency_code)


# if uppercase_currency not in currency_code:
#  print("Please provide correct Currency Code e.g. 'USD'")

response_format = "json"

api_request = api_base_address + currency + "/?format=" + response_format

# Making our request

response = requests.get(api_request)

response_json = response.json()

response_df = pd.DataFrame(response_json)

# get a rates element from data frame that is a dictionary with 3 keys: no, effectiveDate and mid (actual rate), it is of type series

response_rate_series = response_df.loc[:, "rates"]  # "Selects all rows from the column named "rates"

# assign element to dictionary that we can easily work

response_rate_dict = response_rate_series[0]

rate = float(response_rate_dict["mid"])

print(f"PLN to {uppercase_currency} rate is: {rate} PLN")

exchange = float(input("How much money do you want to exchange?"))

print(f"If you exchange {exchange} PLN, you will get {exchange / rate:.4f} {uppercase_currency}")