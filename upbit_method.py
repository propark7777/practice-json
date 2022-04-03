import requests
import json

tickers_krw =[]

def get_tickers_kwr():
    url = "https://api.upbit.com/v1/market/all?isDetails=false"

    headers = {"Accept": "application/json"}

    response = requests.request("GET", url, headers=headers)

    jsonObject = response.text

    info = json.loads(jsonObject)
    
    for i in range(0,len(info)):
        str = info[i]["market"]
        if str.startswith("KRW") :
            str = str[4:]
            tickers_krw.append(str)
    
    return tickers_krw

get_tickers_kwr()
