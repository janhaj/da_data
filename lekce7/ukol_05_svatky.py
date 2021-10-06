import requests
import json
import sys

response = requests.get('http://svatky.adresa.info/json')
data = json.loads(response.text)

print(f'Dnes ma svatek: {data[0]["name"]}')

if len(sys.argv) < 3:
    exit()
den = sys.argv[1]
mesic = sys.argv[2]
datum = den.zfill(2) + mesic.zfill(2)
response = requests.get(f'http://svatky.adresa.info/json?date={datum}')
data = json.loads(response.text)
print(f'{den}.{mesic}. ma svatek: {data[0]["name"]}')