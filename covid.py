import requests

pais = 'Brazil'
status = 'Confirmed'
url = "https://covid-api.mmediagroup.fr/v1/history?country=%s&status=%s" % (pais, status)

response = requests.get(url).json()

print("País: %s \nQtd de casos (26/11/2020): %s \n " % (response['All']['country'], response['All']['dates']['2020-11-26']))