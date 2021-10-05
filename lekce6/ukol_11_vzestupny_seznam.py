seznam = [1, 3, 4, 9, 10, 18]

vzestupny = True
for i in range(1, len(seznam)):
    if seznam[i - 1] > seznam[i]:
        vzestupny = False

if vzestupny:
    print('Seznam je vzestupny')
else:
    print('Seznam neni vzestupny')