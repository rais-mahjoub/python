l=[8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
multiples=[]
for i in range(len(l)):
    if l[i]>=25 and l[i]<= 90:
        multiples.append(l[i])
def somme(multiples):
    calcul = 1
    for j in range(len(multiples)):
        calcul *= multiples[j]
    return calcul
print(multiples)
print(somme(multiples))