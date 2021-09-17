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

# 1
hlasu_1 = sum([radek[0] for radek in hlasy])
hlasu_2 = sum([radek[1] for radek in hlasy])
hlasu_3 = sum([radek[2] for radek in hlasy])
hlasu_4 = sum([radek[3] for radek in hlasy])
hlasu_5 = sum([radek[4] for radek in hlasy])
celkem_hlasu = [hlasu_1, hlasu_2, hlasu_3, hlasu_4, hlasu_5]
print(celkem_hlasu)

# 2
index_kandidata = celkem_hlasu.index(max(celkem_hlasu))
print(lide[index_kandidata])

# 3
volebni_ucast_v_krajich = [sum(kraj) for kraj in hlasy]
minimalni_ucast_index = volebni_ucast_v_krajich.index(min(volebni_ucast_v_krajich))
print(minimalni_ucast_index)
maximalni_ucast_index = volebni_ucast_v_krajich.index(max(volebni_ucast_v_krajich))
print(maximalni_ucast_index)

# 4
vyhra_kandidata = [radek.index(max(radek)) for radek in hlasy]
print(vyhra_kandidata)

# 5