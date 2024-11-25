#jour 1
print(10+3)

alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
print(alphabet)

alphabet.reverse()
print(alphabet)

ma_string = "Je suis une String"
print(ma_string)

num1 = 40
num2 = 2
print(num1+num2)

num1 = 3
num2 = 14
print(num1*num2)

nom = 'nom'
prix = 10.00
stock = 5
print("Le produit", nom, "coûte", prix, "€ et il en reste", stock)
qté = int(input("Combien souhaitez-vous en acheter ? "))
stock = stock-qté
print("Il en reste désormais", stock)

prix = prix*1.1
print("Le produit", nom, "coûte", prix, "€ et il en reste", stock)

#job 10
first_invest = int(input("Combien souhaitez-vous inverstir ? "))
rendement_annuel = 1.02
valeur = int(first_invest*rendement_annuel)
gain_perte = int(valeur-first_invest)
if gain_perte < 0:
    print("La perte est de", gain_perte, "€.")
else:
    print("Le profit est de", gain_perte, "€.")

new_invest = int(input("Nouvel investissement :"))
invest = first_invest+new_invest
rendement_annuel = rendement_annuel+0.02
valeur = int((valeur+new_invest)*rendement_annuel)
gain_perte = int(valeur-invest)
if gain_perte < 0:
    print("La perte est de", gain_perte, "€.")
else:
    print("Le profit est de", gain_perte, "€.")

print(valeur*.1)

new_invest = int(input("Souhaitez-vous continuer à investir ? Si oui, combien souhaitez ajouter ? "))
invest += new_invest
rendement_annuel = rendement_annuel-0.01
valeur = int((valeur+new_invest)*rendement_annuel)
gain_perte = int(valeur-invest)
if gain_perte < 0:
    print("La perte est de", gain_perte, "€.")
else:
    print("Le profit est de", gain_perte, "€.")
print("Vous avez investi au total", invest, "€.")
print("La valeur totale de votre investissement est de", valeur, "€.")

texte = input("Insérez votre texte :")
if 'e' in texte:
    print("Il y a un e dans ce texte.")
else:
    print("Il n'y a pas de e dans ce texte.")


#-------------

#jour 2
for i in range(21):
    print(i)

for i in range(0,21,2):
    print(i)

for i in range(1,21):
    print(i**2)

N = int(input("Entrez un entier supérieur à 0 : "))
for i in range(1,N+1):
    print(i, "x 1 =", i*1)
    print(i, "x 2 =", i*2)
    print(i, "x 3 =", i*3)
    print(i, "x 4 =", i*4)
    print(i, "x 5 =", i*5)
    print(i, "x 6 =", i*6)
    print(i, "x 7 =", i*7)
    print(i, "x 8 =", i*8)
    print(i, "x 9 =", i*9)
    print(i, "x 10 =", i*10)
    print( )

N = int(input("Entrez un entier supérieur à 0 : "))
i = 1
while i<N+1:
    print(i, "x 1 =", i*1)
    print(i, "x 2 =", i*2)
    print(i, "x 3 =", i*3)
    print(i, "x 4 =", i*4)
    print(i, "x 5 =", i*5)
    print(i, "x 6 =", i*6)
    print(i, "x 7 =", i*7)
    print(i, "x 8 =", i*8)
    print(i, "x 9 =", i*9)
    print(i, "x 10 =", i*10)
    print( )
    i += 1

#job 6
N = int(input("Entrez un entier supérieur à 0 : "))
i = 1
while i<N+1:
    result = 7*i
    print(f"7 x {i} = {result}")
    i += 1

i = 1
while i < 13:
    print("Tour", i, ":", i*3-2)
    i += 1


#---------

#jour 3
valeur1 = int(input("valeur1"))
valeur2 = int(input("valeur2"))
if valeur1 == valeur2:
    print("Les valeurs sont égales.")
else:
    print("Les valeurs ne sont pas égales.")

age = int(input("Quel âge as-tu (entre juste le nombre) ? "))
if age >= 18:
    print("Tu peux voter.")
else:
    print("Tu ne peux pas voter.")

for i in range(101):
    if i != 26 and i != 37 and i != 88:
        print(i)

for i in range(1,101):
    if i % 3 != 0 and i % 5 != 0:
        print(i)
    elif i % 3 == 0 and i %5!=0:
        print("Fizz")
    elif i%3!=0 and i%5==0:
        print("Buzz")
    else:
        print("FizzBuzz")

#INSERER JOB 5 QD IL SERA COMPRIS


num = int(input("Entrez un nombre : "))
if num % 2 == 0:
    print(f"Le nombre {num} est pair.")
else:
    print(f"Le nombre {num} est impair.")

alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]*10
str_alphabet = ''.join(alphabet)
j = 1
while j<=len(alphabet) :
        print(str_alphabet[slice(0,j)])
        j += 2


    

#-----------------

#j5

fruits = ['pomme', 'cerise', 'orange']
print (fruits)
print (fruits [1])
fruits.append("Melon")
fruits.insert(2, "mangue")

l = [1, 2, 3, 4, 5]
print(l)
print(l[1])
l[3] = l[2] + l[4]
print(l)
print(l[-1])
l[0], l[-1] = l[-1], l[0]

l=[8,24,48,2,16]
compte=0
for i in range(len(l)):
    if l[i]%3==0:
        compte+=1
if compte<2:
    print(f"Il y a {compte} multiple de 3 dans cette liste")
else:
    print(f"Il y a {compte} multiples de 3 dans cette liste")

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

liste=[8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
def maximum(liste):
    maxi = liste[0]
    for i in liste:
        if i >= maxi:
            maxi = i
    return maxi
def minimum(liste):
    mini = liste[0]
    for i in liste:
        if i <= mini:
            mini = i
    return mini
print("Vmax :", maximum(liste))
print("Vmin :", minimum(liste))

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

l = [7, 11, 42, 39, 2]
for i in range(len(l)):
    l[i] += 1
print(l)

l = [7, 11, 42, 39, 2]
print(l)
count = 0
for element in l:
	count += 1
for i in range(count):
	for j in range(count-1):
		if l[j]>l[j+1]:
			l[j], l[j+1] = l[j+1], l[j]
print(l)

l = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
print(l)
count = 0
for element in l:
	count += 1
for i in range(count**2):
	for j in range(count-1):
		if l[j]>l[j+1]:
			l[j], l[j+1] = l[j+1], l[j]
a=0
while a<count-1:
	if l[a]==l[a+1]:
		del l[a]
		count -= 1
	a+=1
print(l)