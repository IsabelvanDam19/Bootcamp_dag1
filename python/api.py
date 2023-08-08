print('start api read')

import requests

paginaresults  = requests.get('https://catfact.ninja/facts')
print(paginaresults)

feitjes = paginaresults.json()
print(feitjes["data"][0])