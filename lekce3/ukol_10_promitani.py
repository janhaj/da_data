nazvy = [
  'Někdo to rád horké, extended edition',
  'Adéla ještě nevečeřela',
  'Kulový blesk'
]
delky = [136, 105, 82]

trvani = [str(delka // 60) + ':' + str(delka%60) for delka in delky]
print(trvani)