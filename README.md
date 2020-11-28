Web APIs:

1) Cryptocurrency API : Coinlore (https://www.coinlore.com/cryptocurrency-data-api)
    -> API para obter dados atuais sobre as criptomoedas.
    -> Exemplo: obter dados da moeda bitcoin (id=90)
    https://api.coinlore.net/api/ticker/?id=90
  
    Resultado :   [
                        {
                            "id": "90",
                            "symbol": "BTC",
                            "name": "Bitcoin",
                            "nameid": "bitcoin",
                            "rank": 1,
                            "price_usd": "17052.03",
                            "percent_change_24h": "-0.98",
                            "percent_change_1h": "-0.43",
                            "percent_change_7d": "-7.21",
                            "market_cap_usd": "315387110751.84",
                            "volume24": "24635090663.39",
                            "volume24_native": "1444701.45",
                            "csupply": "18495577.00",
                            "price_btc": "1.00",
                            "tsupply": "18495577",
                            "msupply": "21000000"
                        }
                    ]

2) Rest Countries (https://restcountries.eu/)
    -> API para obter dados sobre países.
    -> Exemplo: obter o país cuja capitça é Londres
    https://restcountries.eu/rest/v2/capital/london

    Resultado:  [
                    {
                        "name": "United Kingdom of Great Britain and Northern Ireland",
                        "topLevelDomain": [
                        ".uk"
                        ],
                        "alpha2Code": "GB",
                        "alpha3Code": "GBR",
                        "callingCodes": [
                        "44"
                        ],
                        "capital": "London",
                        "altSpellings": [
                        "GB",
                        "UK",
                        "Great Britain"
                        ],
                        "region": "Europe",
                        (...)
                    }

3) Covid-19-API (https://github.com/M-Media-Group/Covid-19-API)
    -> API para obter dados da epidemia de Covid-19
    -> Exemplo: obter a qUantidade de casos confirmados no Brasil
    https://covid-api.mmediagroup.fr/v1/history?country=Brazil&status=Confirmed

    Resultado:
    {
        "All": {
            "country": "Brazil",
            "population": 209288278,
            "sq_km_area": 8547403,
            "life_expectancy": "62.9",
            "elevation_in_meters": 320,
            "continent": "South America",
            "abbreviation": "BR",
            "location": "South America",
            "iso": 76,
            "capital_city": "Brasília",
            "dates": {
            "2020-11-26": 6204220,
            "2020-11-25": 6166606,
            "2020-11-24": 6118708,
            "2020-11-23": 6087608,
            "2020-11-22": 6071401,
            "2020-11-21": 6052786,
            "2020-11-20": 6020164,
            "2020-11-19": 5981767,
            "2020-11-18": 5945849, 
            (...)
            }
        (...)
        }
    }

4) Qrtag (https://www.qrtag.net/api/)
    -> API para gerar QRCodes.