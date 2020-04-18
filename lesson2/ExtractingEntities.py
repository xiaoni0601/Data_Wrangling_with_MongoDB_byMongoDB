from bs4 import BeautifulSoup

def options(soup, id):
    option_values = []
    carrier_list = soup.find(id = id)
    for option in carrier_list.findall('option'):
        option_values.append(option['value'])
    return option_values

def print_list(label, codes):
    print("\n%s/:" % label)
    for c in codes:
        print(c)

def main():
    soup = BeautifulSoup(open('United_and_logan_airport.html'))
    
    codes = options(soup, 'CarrierList')
    print_list('Carriers', codes)

    codes = options(soup, 'Airportlist')
    print_list('Airports', codes)