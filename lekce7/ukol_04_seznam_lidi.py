import requests
import json

response = requests.get('http://api.kodim.cz/python-data/people')
data = json.loads(response.text)

print('cast 1:')
print(len(data))

print('cast 2:')
# Metoda keys vraci zvlastni datovy typ "dict_keys", ktery nejde
# uplne snadno vypsat. Ale muzeme to obejit tim, ze si ho zmenime
# na obycejny seznam pomoci funkce list()
print(list(data[0].keys()))

print('cast 3:')
zen = 0
muzu = 0
for osoba in data:
    if osoba['gender'] == 'Female':
        zen += 1
    elif osoba['gender'] == 'Male':
        muzu += 1
print(f'Pocet zen: {zen}')
print(f'Pocet muzu: {muzu}')