print('cast 1:')
cisla = [3, 5, 8, 0, 4, 2, 0, 7, 6, 2, 0, 5]
sum = 0
for cislo in cisla:
  sum = sum + cislo
  if cislo == 0:
    print(sum)
    sum = 0

# program bude pocitat soucet hodnot v seznamu
# pokud bude zpracovavany prvek roven 0, vypise dosavadni soucet a bude
# pocitat znovu od nuly. Posledni soucet nebude vypsan, jestlize neni 
# posledni hodnota v seznamu 0

print('cast 2:')
cisla = [3, 5, 8, 0, 4, 2, 0, 7, 6, 2, 0, 5]
index = 0
for cislo in cisla:
  if index % 2 == 0:
    print(cislo)
  index +=  1

# vypise kazde cislo, jehoz index v seznamu je sudy -> vypise index 0, 2, 4, ..