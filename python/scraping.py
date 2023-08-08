print("Hellooooooo")

import requests
from bs4 import BeautifulSoup

pagina = requests.get('https://coinmarketcap.com')

#print(pagina.content)

heeldehtml = BeautifulSoup(pagina.content, 'html.parser')

table = heeldehtml.find('table')
print(table.prettify())

