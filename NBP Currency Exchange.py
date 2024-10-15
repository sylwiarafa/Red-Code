
import pandas as pd

import requests



api_base_address = 'https://api.nbp.pl/api/exchangerates/rates/a/'

#pytam użytkownika jaką walutę on chce wymienić i od razu wysyłam prośbę do servera o ta konkretną walutę

currency = input('What currency do you want to exchange the money to?')
uppercase_currency = currency.upper()

#stworzyłam, krótką listę z skrótami nazw walut. Jeśli uzytkownik źle wpisze to dostanie poniższy komunikat
currency_code = { 'USD', 'GBP', 'AUD', 'AED'}
if uppercase_currency not in currency_code:
    print("Please provide correct Currency Code e.g. 'USD'")

response_format = "json"

api_request = api_base_address + currency + "/?format=" + response_format

# Making our request

response = requests.get(api_request)

response_json = response.json()



# Making our request

response = requests.get(api_request)

response_json = response.json()


response_df = pd.DataFrame(response_json)



# get a rates element from data frame that is a dictionary with 3 keys: no, effectiveDate and mid (actual rate), it is of type series

response_rate_series = response_df.loc[: ,"rates"] # "Selects all rows from the column named "rates"

# assign element to dictionary that we can easily work

response_rate_dict = response_rate_series[0]



rate = int(response_rate_dict["mid"])



#podaję aktualną stawkę

print(f"PLN to {uppercase_currency} rate is: {rate} PLN")

#pytam użytkownika ile PLN chce wymienić

exchange = int(input("How much money do you want to exchange?"))

#tworzę funkcję kalkulującą

print(f"If you exchange {exchange} PLN, you will get {exchange / rate} {uppercase_currency}")



#ZADANIE
# create_npb_request wezmie jako parametr „currency” i zwroci nam jaki jest „rate” w PLNach dla zadanej currency.

# funkcja exchange wezmie jako parametry, „rate” i „amount” i zwroci nam ile mamy pieniędzy w nowej walucie.

# Majac dwie powyższe funkcje napisz program który zapyta: ile chcesz wymienić PLNow, na jaka walute i wyświetli ile dostajesz po wymianie.



