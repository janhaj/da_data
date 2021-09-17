import random

typy_karet = [str(cislo) for cislo in range(2,10)] + ['Kluk', 'Dama', 'Kral', 'Eso']
druh_karet = ['piky', 'krize', 'srdce', 'kary']

print(random.choice(typy_karet) + ' ' + random.choice(druh_karet))