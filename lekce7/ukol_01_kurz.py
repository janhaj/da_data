kurz = {
  'nazev': 'Úvod do programování',
  'lektor': 'Martin Podloucký',
  'konani': [
    {
      'misto': 'T-Mobile',
      'koucove': [
        'Dan Vrátil',
        'Filip Kopecký',
        'Martina Nemčoková'
      ],
      'ucastnic': 30
    },
    {
      'misto': 'MSD IT',
      'koucove': [
        'Dan Vrátil',
        'Zuzana Tučková',
        'Martina Nemčoková'
      ],
      'ucastnic': 25
    },
    {
      'misto': 'Škoda DigiLab',
      'koucove': [
        'Dan Vrátil',
        'Filip Kopecký',
        'Kateřina Kalášková'
      ],
      'ucastnic': 41
    }
  ]
}


print('cast 1:')
print(kurz['konani'][-1]['ucastnic'])

print('cast 2:')
print(kurz['konani'][-1]['koucove'][-1])

print('cast 3:')
print(len(kurz['konani']))

print('cast 4:')
print([info_o_kurzu['misto'] for info_o_kurzu in kurz['konani']])