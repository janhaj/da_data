import math
recept = {
  'nazev': 'Batáty se šalvějí a pancettou',
  'narocnost': 'stredni',
  'doba': 30,
  'ingredience': [
    ['batát', '1', '15 kč'],
    ['olivový olej', '2 lžíce', '2 kč'],
    ['pancetta', '4-6 plátků', '21 kč'],
    ['přepuštěné máslo', '2 lžíce', '5 kč'],
    ['mletý černý pepř', '1/2 lžičky', '0.5 kč'],
    ['sůl', '1/2 lžičky', '0.1 kč'],
    ['muškátový oříšek', 'špetka', '1 kč'],
    ['česnek', '2 stroužky', '1 kč'],
    ['šalvějové lístky', '20-25', '12 kč']
  ]
}

cena = 0
for ingredience in recept['ingredience']:
    cena = cena + float(ingredience[2].split(' ')[0])
print(math.ceil(cena))