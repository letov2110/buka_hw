import requests

r = requests.get("https://www.nbrb.by/api/exrates/rates/431?periodicity=0")
data = r.json()
price = data["Cur_OfficialRate"]
usd = int(input('поменять usd: '))
print(f"курс покупки: {price} byn\n{usd} usd = {usd*price} byn")