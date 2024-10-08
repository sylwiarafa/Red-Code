#Code Red Challenge - Exchange Currency
# 1st Step - Connecting to a Website
import requests

#GBP to other currencies
url = 'https://v6.exchangerate-api.com/v6/c148cea9d0debfb06b56eeb1/latest/GBP'
response = requests.get(url)
data = response.json()
conversion_rateGBP = data['conversion_rates']
print('GBP to other currencies:', conversion_rateGBP)


#GBP to PLN conversion rate
url = 'https://v6.exchangerate-api.com/v6/c148cea9d0debfb06b56eeb1/latest/GBP'
response = requests.get(url)
data = response.json()
gbp_to_pln = data['conversion_rates']['PLN']
print('GBP to PLN exchange rate:', gbp_to_pln)

import requests
#EUR to GBP conversion rate
response = requests.get("https://v6.exchangerate-api.com/v6/c148cea9d0debfb06b56eeb1/pair/EUR/GBP")
data = response.json()
eur_to_gbp = data['conversion_rate']
print('EUR to GBP conversion rate:', eur_to_gbp)

#How much is 1000 PLN in GBP?
response = requests.get("https://v6.exchangerate-api.com/v6/c148cea9d0debfb06b56eeb1/pair/PLN/GBP/1000")
data = response.json()
conversion_PLN_to_GBP= data['conversion_result']
print('How much is 1000 PLN in GBP? 1000 PLN equals:',  conversion_PLN_to_GBP)

#Please enter how many EUR you want to exchange to GBP?
response = requests.get("https://v6.exchangerate-api.com/v6/c148cea9d0debfb06b56eeb1/pair/EUR/GBP")
data = response.json()
eur_to_gbp1 = data.get('conversion_rate')
if eur_to_gbp1 is not None: #dlaczego tutaj jest None? a nie np. 0?
    euros = int(input('Please enter how much EUR you want to exchange:'))
    gbp = euros * eur_to_gbp1
print(f"{euros} EUR is equal to {gbp: } GBP at a conversion rate of {eur_to_gbp1:}.")
