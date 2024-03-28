import requests,json

def details(s):
    print(s)
    url=f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={s}&apikey=R4ARAI1A8PPZ93QR'
    r = requests.get(url)
    return r.text


data=details("v")
with open("generate.json", "w") as file:
    json.dump(data, file)