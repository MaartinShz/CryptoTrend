tab = []


from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'10',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '994352b1-f247-4a59-82e4-0f117bf65dbf',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

#recherche : 
# mcap < 100
# re nom

data["data"]

id =[data['id'] for data in data["data"]]
id

nom =[data['name'] for data in data["data"]]
nom

symbol =[data['symbol'] for data in data["data"]]
symbol

marketcap =[data["quote"]["USD"]["market_cap"] for data in data["data"]]
marketcap





