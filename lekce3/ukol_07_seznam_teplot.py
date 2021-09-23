teploty = [
  [2.1, 5.2, 6.1, -0.1],
  [2.2, 4.8, 5.6, -1.0],
  [3.3, 6.5, 5.9, 1.2],
  [2.9, 5.6, 6.0, 0.0],
  [2.0, 4.6, 5.5, -1.2],
  [1.0, 3.2, 2.1, -2.0],
  [0.4, 2.7, 1.3, -2.8]
]

# 1
print('prumerne teploty:')
prumerne_teploty = [sum(denni_teploty) / 4 for denni_teploty in teploty]
print(prumerne_teploty)

# 2
print('ranni teploty:')
ranni_teploty = [denni_teploty[0] for denni_teploty in teploty]
print(ranni_teploty)

# 3
print('nocni teploty:')
nocni_teploty = [denni_teploty[3] for denni_teploty in teploty]
print(nocni_teploty)

# 4
print('denni a nocni teploty:')
denni_nocni_teploty = [[denni_teploty[1], denni_teploty[3]] for denni_teploty in teploty]
print(denni_nocni_teploty)

# 5
print('prumer teplot za cely tyden:')
celkovy_soucet = sum([sum(radek) for radek in teploty])
pocet_hodnot = sum([len(radek) for radek in teploty])
print(celkovy_soucet / pocet_hodnot)