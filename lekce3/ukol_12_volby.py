hlasy = [
  [78774, 43179, 225111, 144799, 242854],
  [91062, 22451, 17475, 53391, 46450],
  [179186, 216499, 4493, 156305, 61222],
  [9619, 53476, 926, 64737, 34566],
  [66904, 85730, 27271, 12964, 38041],
  [118755, 1929, 30426, 25178, 31952],
  [64467, 40993, 81181, 39392, 4335],
  [11221, 97970, 26179, 98539, 112578],
  [171064, 7638, 8752, 96666, 39738],
  [74235, 101680, 18920, 45904, 1922],
  [39309, 1505, 10531, 30458, 40228],
  [131584, 1812, 241122, 22267, 99326],
  [194133, 39985, 200997, 28229, 20780],
  [66188, 51607, 15977, 177272, 17664]
]

lide = ['Igor Rezek', 'Augustýn Doležal', 'Vladan Bednář', 'Ondřej Brotz', 'Radim Kašpar']
kraje = ['Hlavní město Praha', 'Jihočeský kraj', 'Jihomoravský kraj', 'Karlovarský kraj', 'Kraj Vysočina', 'Královéhradecký kraj', 'Liberecký kraj', 'Moravskoslezský kraj', 'Olomoucký kraj', 'Pardubický kraj', 'Plzeňský kraj', 'Středočeský kraj', 'Ústecký kraj', 'Zlínský kraj']

# 1
print('celkove hlasy kandidatu:')
hlasu_1 = sum([radek[0] for radek in hlasy])
hlasu_2 = sum([radek[1] for radek in hlasy])
hlasu_3 = sum([radek[2] for radek in hlasy])
hlasu_4 = sum([radek[3] for radek in hlasy])
hlasu_5 = sum([radek[4] for radek in hlasy])
celkem_hlasu = [hlasu_1, hlasu_2, hlasu_3, hlasu_4, hlasu_5]
print(celkem_hlasu)

# 2
print('prvni kolo voleb vyhral:')
index_kandidata = celkem_hlasu.index(max(celkem_hlasu))
print(lide[index_kandidata])

# 3
volebni_ucast_v_krajich = [sum(kraj) for kraj in hlasy]
minimalni_ucast_index = volebni_ucast_v_krajich.index(min(volebni_ucast_v_krajich))
print('minimalni ucast byla v kraji: ' + kraje[minimalni_ucast_index])
maximalni_ucast_index = volebni_ucast_v_krajich.index(max(volebni_ucast_v_krajich))
print('maximalni ucast byla v kraji: ' + kraje[maximalni_ucast_index])

# 4
vyhra_kandidata = [radek.index(max(radek)) for radek in hlasy]
print(vyhra_kandidata)

# 5
print('procenta hlasu:')
celkem_hlasu = sum([sum(radek) for radek in hlasy])
procenta_hlasu = [[(pocet_hlasu_kandidata / celkem_hlasu) * 100 for pocet_hlasu_kandidata in radek] for radek in hlasy]
print(procenta_hlasu)

# 6
print('vice nez 50% volicu?')
tabulka_z_cviceni_11 = [
  ['Hlavní město Praha', '1 280 508'],
  ['Jihočeský kraj', '638 782'],
  ['Jihomoravský kraj', '1 178 812'],
  ['Karlovarský kraj', '296 749'],
  ['Kraj Vysočina', '508 952'],
  ['Královéhradecký kraj', '550 804'],
  ['Liberecký kraj', '440 636'],
  ['Moravskoslezský kraj', '1 209 879'],
  ['Olomoucký kraj', '633 925'],
  ['Pardubický kraj', '517 087'],
  ['Plzeňský kraj', '578 629'],
  ['Středočeský kraj', '1 338 982'],
  ['Ústecký kraj', '821 377'],
  ['Zlínský kraj', '583 698']
]
opravneni_volici = [int(radek[1].replace(' ', '')) for radek in tabulka_z_cviceni_11]
procenta_hlasu = [sum(hlasy[index]) > opravneni_volici[index] / 2 for index in range(len(hlasy))]
print(procenta_hlasu)