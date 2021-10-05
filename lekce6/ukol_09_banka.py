with open('ukol_09_zustatky.txt') as vstupni_soubor:
    zustatky = [int(radek.strip()) for radek in vstupni_soubor]

# 1
print('cast 1:')
for zustatek in zustatky:
    print(zustatek * 1.025)

# 2
print('cast 2:')
for zustatek in zustatky:
    if zustatek >= 0:
        print(zustatek * 1.025)

# 3
print('cast 3:')
for index in range(len(zustatky)):
    print(str(index) + ': ' + str(zustatky[index] * 1.025))