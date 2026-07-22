import requests

BASE_URL = 'https://api.exchangerate.host/convert?access_key='
API_KEY = '01c9ffc9cccf7e2337c506cb62e01c3a'

def fetchCurrency(self, base, target, value) -> str:
    url = f"{BASE_URL}{API_KEY}&from={base}&to={target}&amount={value}"
    print('URL-> ', url)
    response = requests.get(url=url)
    return response.content


# output
# {
#   "success": true,
#   "terms": "https://currencylayer.com/terms",
#   "privacy": "https://currencylayer.com/privacy",
#   "query": {
#     "from": "EUR",
#     "to": "USD",
#     "amount": 100
#   },
#   "info": {
#     "timestamp": 1784470324,
#     "quote": 1.144028
#   },
#   "result": 114.4028
# }