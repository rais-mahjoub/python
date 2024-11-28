note = int(input('Note : '))
if note % 5 > 2:
    note = ((note//5)+1)*5
print(note)
if note<40:
    print('Vous avez échoué !')
else:
    print('Vous avez réussi !')