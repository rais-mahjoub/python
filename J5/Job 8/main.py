l=[8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
multiples=[]
for i in range(len(l)):
    if l[i]%2==0:
        multiples.append(l[i])
def somme(multiples):
    calcul = 0
    for j in range(len(multiples)):
        calcul += multiples[j]
    return calcul
print(multiples)
print(somme(multiples))