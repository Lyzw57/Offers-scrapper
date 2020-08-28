from bs4 import BeautifulSoup
from requests import get

min_price = 15000
max_price = 25000
is_damaged = "notdamaged"
gearbox_type = "automatic"

URL = f'https://www.olx.pl/motoryzacja/samochody/?search%5Bfilter_float_price%3Afrom%5D={min_price}&search%5Bfilter_float_price%3Ato%5D={max_price}&search%5Bfilter_enum_condition%5D%5B0%5D={is_damaged}&search%5Bfilter_enum_transmission%5D%5B0%5D={gearbox_type}'

page = get(URL)
bs = BeautifulSoup(page.content, 'html.parser')

for offer in bs.find_all('div', class_='offer-wrapper'):
    car_name = offer.find()
    price = offer.find('p', class_='price').get_text()
    footer = offer.find('td', class_='bottom-cell')
    location = footer.find('small', class_="breadcrumb").get_text().strip().split(',')[0]
    print(f"{location} - {price}")
