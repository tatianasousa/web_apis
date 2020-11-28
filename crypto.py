import requests


url = "https://api.coinlore.net/api/ticker/?id=90"

response = requests.get(url).json()

print("Nome: %s \nSimbolo: %s \n " % (response[0]['name'], response[0]['symbol']))