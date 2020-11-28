import requests

capital = 'london'
url = "https://restcountries.eu/rest/v2/capital/%s" % capital

response = requests.get(url).json()

print("Capital: %s \nPaís: %s \n " % (response[0]['capital'], response[0]['name']))