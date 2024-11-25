mot = str(input("Entrez un mot : "))
lettres = []
i=0
while i < len(mot):
    lettre = mot[i]
    lettres.append(lettre)
    i+=1
lettres.reverse()
mot_inversé = ''.join(lettres)
if mot == mot_inversé:
    print("Oh, un calenbour")
else:
    print(mot_inversé)