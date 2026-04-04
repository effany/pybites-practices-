from collections import defaultdict

# fake data from https://www.mockaroo.com
data = """last_name,first_name,country_code
Watsham,Husain,ID
Harrold,Alphonso,BR
Apdell,Margo,CN
Tomblings,Deerdre,RU
Wasielewski,Sula,ID
Jeffry,Rudolph,TD
Brenston,Luke,SE
Parrett,Ines,CN
Braunle,Kermit,PL
Halbard,Davie,CN"""


def group_names_by_country(data: str = data) -> defaultdict:
    countries = defaultdict(list)
    data_array = data.split()[1:]
    for data in data_array:
        individual = data.split(',')
        countries[individual[2]].append(individual[1] + " " + individual[0])
    return countries

def group_names_by_country(data: str) -> defaultdict:
    countries = defaultdict(list)
    for line in data.strip().split('\n')[1:]:
        last_name, first_name, country_code = line.split(',')
        countries[country_code].append(f"{first_name} {last_name}")
    return countries
